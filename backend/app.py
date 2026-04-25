"""
FairHire – Selectively Anonymous AI Hiring System
Backend: Python Flask
Updated: Admin panel, photo/signature, career docs, HR shortlist, contact reveal
"""

import os
import json
import uuid
import sqlite3
import io
import re
from datetime import datetime
from functools import wraps
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
    return response

DB_PATH = os.path.join(os.path.dirname(__file__), 'fairhire.db')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')

# ─────────────────────────────────────────────
# DATABASE INIT
# ─────────────────────────────────────────────

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.executescript('''
            CREATE TABLE IF NOT EXISTS candidates (
                id              TEXT PRIMARY KEY,
                full_name       TEXT NOT NULL,
                email           TEXT UNIQUE NOT NULL,
                phone           TEXT,
                dob             TEXT,
                address         TEXT,
                password_hash   TEXT NOT NULL,
                password_plain  TEXT,
                gov_id_type     TEXT,
                gov_id_number   TEXT,
                photo_data      TEXT,
                signature_data  TEXT,
                token           TEXT,
                is_shortlisted  INTEGER DEFAULT 0,
                shortlisted_at  TIMESTAMP,
                shortlist_note  TEXT,
                created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS qualifications (
                candidate_id        TEXT PRIMARY KEY,
                tenth_percentage    REAL,
                tenth_board         TEXT,
                twelfth_percentage  REAL,
                twelfth_board       TEXT,
                degree              TEXT,
                branch              TEXT,
                cgpa                REAL,
                college_name        TEXT,
                school_name         TEXT,
                FOREIGN KEY (candidate_id) REFERENCES candidates(id)
            );

            CREATE TABLE IF NOT EXISTS career_documents (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                candidate_id    TEXT,
                doc_name        TEXT,
                doc_type        TEXT,
                doc_data        TEXT,
                uploaded_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (candidate_id) REFERENCES candidates(id)
            );

            CREATE TABLE IF NOT EXISTS skills (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                candidate_id TEXT,
                skill_name   TEXT,
                cert_data    TEXT,
                is_verified  INTEGER DEFAULT 0,
                confidence   REAL    DEFAULT 0,
                notes        TEXT,
                FOREIGN KEY (candidate_id) REFERENCES candidates(id)
            );

            CREATE TABLE IF NOT EXISTS experience (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                candidate_id    TEXT,
                company_name    TEXT,
                role            TEXT,
                duration_months INTEGER,
                description     TEXT,
                FOREIGN KEY (candidate_id) REFERENCES candidates(id)
            );

            CREATE TABLE IF NOT EXISTS scores (
                candidate_id        TEXT PRIMARY KEY,
                academic_score      REAL DEFAULT 0,
                skill_score         REAL DEFAULT 0,
                verification_score  REAL DEFAULT 0,
                experience_score    REAL DEFAULT 0,
                final_score         REAL DEFAULT 0,
                confidence_level    TEXT DEFAULT 'Low',
                verified_at         TIMESTAMP,
                FOREIGN KEY (candidate_id) REFERENCES candidates(id)
            );

            CREATE TABLE IF NOT EXISTS hr_users (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                username      TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                token         TEXT
            );

            CREATE TABLE IF NOT EXISTS admin_users (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                username      TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                token         TEXT
            );
        ''')

        # Seed default HR  →  hr@fairhire.com / hr123
        conn.execute(
            'INSERT OR IGNORE INTO hr_users (username, password_hash) VALUES (?, ?)',
            ('hr@fairhire.com', generate_password_hash('hr123'))
        )
        # Seed default Admin  →  admin@fairhire.com / admin123
        conn.execute(
            'INSERT OR IGNORE INTO admin_users (username, password_hash) VALUES (?, ?)',
            ('admin@fairhire.com', generate_password_hash('admin123'))
        )
        conn.commit()


# ─────────────────────────────────────────────
# AUTH HELPERS
# ─────────────────────────────────────────────

def _bearer(req):
    return req.headers.get('Authorization', '').replace('Bearer ', '').strip()


def require_candidate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = _bearer(request)
        if not token:
            return jsonify({'error': 'Missing token'}), 401
        with get_db() as conn:
            row = conn.execute('SELECT * FROM candidates WHERE token=?', (token,)).fetchone()
        if not row:
            return jsonify({'error': 'Unauthorized'}), 401
        request.candidate = dict(row)
        return f(*args, **kwargs)
    return wrapper


def require_hr(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = _bearer(request)
        if not token:
            return jsonify({'error': 'Missing token'}), 401
        with get_db() as conn:
            row = conn.execute('SELECT * FROM hr_users WHERE token=?', (token,)).fetchone()
        if not row:
            return jsonify({'error': 'Unauthorized'}), 401
        request.hr = dict(row)
        return f(*args, **kwargs)
    return wrapper


def require_admin(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = _bearer(request)
        if not token:
            return jsonify({'error': 'Missing token'}), 401
        with get_db() as conn:
            row = conn.execute('SELECT * FROM admin_users WHERE token=?', (token,)).fetchone()
        if not row:
            return jsonify({'error': 'Unauthorized'}), 401
        request.admin = dict(row)
        return f(*args, **kwargs)
    return wrapper


# ─────────────────────────────────────────────
# CANDIDATE ENDPOINTS
# ─────────────────────────────────────────────

@app.route('/api/candidate/register', methods=['POST'])
def candidate_register():
    d = request.json or {}
    if not d.get('email') or not d.get('password') or not d.get('fullName'):
        return jsonify({'error': 'fullName, email and password are required'}), 400

    cid = 'FH' + uuid.uuid4().hex[:6].upper()
    try:
        with get_db() as conn:
            conn.execute(
                '''INSERT INTO candidates
                   (id, full_name, email, phone, dob, address,
                    password_hash, password_plain, gov_id_type, gov_id_number,
                    photo_data, signature_data)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',
                (
                    cid,
                    d['fullName'],
                    d['email'],
                    d.get('phone', ''),
                    d.get('dob', ''),
                    d.get('address', ''),
                    generate_password_hash(d['password']),
                    d.get('password', ''),          # stored plain for admin view
                    d.get('govIdType', ''),
                    d.get('govIdNumber', ''),
                    d.get('photoData', ''),          # base64 JPG
                    d.get('signatureData', ''),      # base64 JPG
                )
            )
            conn.commit()
        return jsonify({'success': True, 'candidateId': cid})
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Email already registered'}), 409


@app.route('/api/candidate/login', methods=['POST'])
def candidate_login():
    d = request.json or {}
    with get_db() as conn:
        row = conn.execute('SELECT * FROM candidates WHERE email=?', (d.get('email', ''),)).fetchone()
    if not row or not check_password_hash(row['password_hash'], d.get('password', '')):
        return jsonify({'error': 'Invalid email or password'}), 401

    token = str(uuid.uuid4())
    with get_db() as conn:
        conn.execute('UPDATE candidates SET token=? WHERE id=?', (token, row['id']))
        conn.commit()
        qual  = conn.execute('SELECT 1 FROM qualifications WHERE candidate_id=?', (row['id'],)).fetchone()
        sk    = conn.execute('SELECT COUNT(*) AS n FROM skills WHERE candidate_id=?', (row['id'],)).fetchone()
        score = conn.execute('SELECT 1 FROM scores WHERE candidate_id=?', (row['id'],)).fetchone()

    step = 1
    if qual:  step = 2
    if sk and sk['n'] > 0: step = 3
    if score: step = 4

    return jsonify({'success': True, 'token': token, 'candidateId': row['id'], 'step': step})


@app.route('/api/candidate/qualifications', methods=['POST'])
@require_candidate
def save_qualifications():
    d   = request.json or {}
    cid = request.candidate['id']
    with get_db() as conn:
        conn.execute(
            '''INSERT OR REPLACE INTO qualifications
               (candidate_id, tenth_percentage, tenth_board, twelfth_percentage, twelfth_board,
                degree, branch, cgpa, college_name, school_name)
               VALUES (?,?,?,?,?,?,?,?,?,?)''',
            (cid,
             float(d.get('tenthPercentage', 0) or 0),
             d.get('tenthBoard', ''),
             float(d.get('twelfthPercentage', 0) or 0),
             d.get('twelfthBoard', ''),
             d.get('degree', ''),
             d.get('branch', ''),
             float(d.get('cgpa', 0) or 0),
             d.get('collegeName', ''),
             d.get('schoolName', ''))
        )
        conn.commit()
    return jsonify({'success': True})


@app.route('/api/candidate/documents', methods=['POST'])
@require_candidate
def save_documents():
    """Upload career documents (PDF only). Also updates photo/signature if provided."""
    d   = request.json or {}
    cid = request.candidate['id']
    with get_db() as conn:
        # Update photo / signature if re-uploaded
        if d.get('photoData'):
            conn.execute('UPDATE candidates SET photo_data=? WHERE id=?', (d['photoData'], cid))
        if d.get('signatureData'):
            conn.execute('UPDATE candidates SET signature_data=? WHERE id=?', (d['signatureData'], cid))

        # Replace all career documents for this candidate
        conn.execute('DELETE FROM career_documents WHERE candidate_id=?', (cid,))
        for doc in d.get('documents', []):
            conn.execute(
                '''INSERT INTO career_documents (candidate_id, doc_name, doc_type, doc_data)
                   VALUES (?,?,?,?)''',
                (cid, doc.get('name', 'document'), doc.get('type', 'pdf'),
                 (doc.get('data', ''))[:500_000])
            )
        conn.commit()
    return jsonify({'success': True})


@app.route('/api/candidate/skills', methods=['POST'])
@require_candidate
def save_skills():
    d   = request.json or {}
    cid = request.candidate['id']
    with get_db() as conn:
        conn.execute('DELETE FROM skills WHERE candidate_id=?',     (cid,))
        conn.execute('DELETE FROM experience WHERE candidate_id=?', (cid,))

        for sk in d.get('skills', []):
            cert = (sk.get('certData') or '')[:200_000]
            conn.execute(
                'INSERT INTO skills (candidate_id, skill_name, cert_data) VALUES (?,?,?)',
                (cid, sk.get('name', '').strip(), cert)
            )
        for ex in d.get('experience', []):
            conn.execute(
                '''INSERT INTO experience (candidate_id, company_name, role, duration_months, description)
                   VALUES (?,?,?,?,?)''',
                (cid, ex.get('company', ''), ex.get('role', ''),
                 int(ex.get('durationMonths', 0) or 0), ex.get('description', ''))
            )
        conn.commit()
    return jsonify({'success': True})


@app.route('/api/candidate/verify', methods=['POST'])
@require_candidate
def verify_candidate():
    cid = request.candidate['id']
    with get_db() as conn:
        qual   = conn.execute('SELECT * FROM qualifications WHERE candidate_id=?', (cid,)).fetchone()
        skills = conn.execute('SELECT * FROM skills WHERE candidate_id=?', (cid,)).fetchall()
        exps   = conn.execute('SELECT * FROM experience WHERE candidate_id=?', (cid,)).fetchall()

    if not qual:
        return jsonify({'error': 'Complete qualifications first'}), 400

    if GEMINI_API_KEY:
        verified = _verify_gemini([dict(s) for s in skills])
    else:
        verified = _verify_basic([dict(s) for s in skills])

    acad_score = _academic_score(dict(qual))
    n_total    = len(skills)
    n_verified = sum(1 for v in verified if v['verified'])
    skill_score = round(n_verified / n_total * 100, 1) if n_total else 50.0
    verif_score = round(n_verified / n_total * 100, 1) if n_total else 30.0
    total_months = sum(e['duration_months'] for e in exps)
    exp_score    = round(min(100, total_months / 24 * 100), 1)
    final = round(acad_score * 0.35 + skill_score * 0.30 +
                  verif_score * 0.20 + exp_score  * 0.15, 1)
    confidence = 'High' if final >= 75 else ('Medium' if final >= 50 else 'Low')

    with get_db() as conn:
        for v in verified:
            conn.execute(
                '''UPDATE skills SET is_verified=?, confidence=?, notes=?
                   WHERE candidate_id=? AND skill_name=?''',
                (1 if v['verified'] else 0, v.get('confidence', 0),
                 v.get('notes', ''), cid, v['name'])
            )
        conn.execute(
            '''INSERT OR REPLACE INTO scores
               (candidate_id, academic_score, skill_score, verification_score,
                experience_score, final_score, confidence_level, verified_at)
               VALUES (?,?,?,?,?,?,?,?)''',
            (cid, acad_score, skill_score, verif_score, exp_score,
             final, confidence, datetime.now())
        )
        conn.commit()

    return jsonify({
        'success': True,
        'academicScore': acad_score, 'skillScore': skill_score,
        'verificationScore': verif_score, 'experienceScore': exp_score,
        'finalScore': final, 'confidenceLevel': confidence,
        'verifiedSkills': verified
    })


@app.route('/api/candidate/profile', methods=['GET'])
@require_candidate
def candidate_profile():
    cid = request.candidate['id']
    c   = request.candidate
    with get_db() as conn:
        qual   = conn.execute('SELECT * FROM qualifications WHERE candidate_id=?', (cid,)).fetchone()
        skills = conn.execute('SELECT skill_name, is_verified, confidence, notes FROM skills WHERE candidate_id=?', (cid,)).fetchall()
        exps   = conn.execute('SELECT role, duration_months, description FROM experience WHERE candidate_id=?', (cid,)).fetchall()
        score  = conn.execute('SELECT * FROM scores WHERE candidate_id=?', (cid,)).fetchone()
        docs   = conn.execute('SELECT id, doc_name, doc_type, uploaded_at FROM career_documents WHERE candidate_id=?', (cid,)).fetchall()

    return jsonify({
        'candidateId':    cid,
        'fullName':       c['full_name'],
        'email':          c['email'],
        'phone':          c['phone'],
        'dob':            c['dob'],
        'address':        c['address'],
        'hasPhoto':       bool(c['photo_data']),
        'hasSignature':   bool(c['signature_data']),
        'photoData':      c['photo_data'] or '',
        'signatureData':  c['signature_data'] or '',
        'qualifications': dict(qual) if qual else None,
        'skills':         [dict(s) for s in skills],
        'experience':     [dict(e) for e in exps],
        'score':          dict(score) if score else None,
        'documents':      [dict(d) for d in docs],
        'isShortlisted':  bool(c['is_shortlisted']),
        'shortlistNote':  c['shortlist_note'] or '',
    })


# ─────────────────────────────────────────────
# HR ENDPOINTS
# ─────────────────────────────────────────────

@app.route('/api/hr/login', methods=['POST'])
def hr_login():
    d = request.json or {}
    with get_db() as conn:
        row = conn.execute('SELECT * FROM hr_users WHERE username=?', (d.get('username', ''),)).fetchone()
    if not row or not check_password_hash(row['password_hash'], d.get('password', '')):
        return jsonify({'error': 'Invalid credentials'}), 401
    token = str(uuid.uuid4())
    with get_db() as conn:
        conn.execute('UPDATE hr_users SET token=? WHERE id=?', (token, row['id']))
        conn.commit()
    return jsonify({'success': True, 'token': token})


@app.route('/api/hr/candidates', methods=['GET'])
@require_hr
def hr_candidates():
    with get_db() as conn:
        rows = conn.execute('''
            SELECT c.id, c.is_shortlisted,
                   q.tenth_percentage, q.twelfth_percentage, q.cgpa, q.degree, q.branch,
                   s.final_score, s.confidence_level,
                   s.academic_score, s.skill_score, s.verification_score, s.experience_score
            FROM   candidates c
            LEFT JOIN qualifications q ON c.id = q.candidate_id
            LEFT JOIN scores         s ON c.id = s.candidate_id
            ORDER  BY COALESCE(s.final_score, 0) DESC
        ''').fetchall()

        result = []
        for r in rows:
            cid   = r['id']
            sks   = conn.execute('SELECT skill_name, is_verified FROM skills WHERE candidate_id=?', (cid,)).fetchall()
            total = conn.execute('SELECT SUM(duration_months) AS t FROM experience WHERE candidate_id=?', (cid,)).fetchone()
            exp_y = round((total['t'] or 0) / 12, 1)
            result.append({
                'candidateId':       cid,
                'tenthPercentage':   r['tenth_percentage'],
                'twelfthPercentage': r['twelfth_percentage'],
                'cgpa':              r['cgpa'],
                'degree':            r['degree'],
                'branch':            r['branch'],
                'skills':            [{'name': s['skill_name'], 'verified': bool(s['is_verified'])} for s in sks],
                'experienceYears':   exp_y,
                'finalScore':        r['final_score'],
                'confidenceLevel':   r['confidence_level'],
                'academicScore':     r['academic_score'],
                'skillScore':        r['skill_score'],
                'verificationScore': r['verification_score'],
                'experienceScore':   r['experience_score'],
                'isShortlisted':     bool(r['is_shortlisted']),
            })
    return jsonify(result)


@app.route('/api/hr/candidate/<cid>', methods=['GET'])
@require_hr
def hr_candidate_detail(cid):
    with get_db() as conn:
        qual   = conn.execute('SELECT * FROM qualifications WHERE candidate_id=?', (cid,)).fetchone()
        skills = conn.execute('SELECT skill_name, is_verified, confidence, notes FROM skills WHERE candidate_id=?', (cid,)).fetchall()
        exps   = conn.execute('SELECT role, duration_months, description FROM experience WHERE candidate_id=?', (cid,)).fetchall()
        score  = conn.execute('SELECT * FROM scores WHERE candidate_id=?', (cid,)).fetchone()
        cand   = conn.execute('SELECT is_shortlisted, shortlist_note FROM candidates WHERE id=?', (cid,)).fetchone()

    if not qual and not score:
        return jsonify({'error': 'Candidate not found'}), 404

    return jsonify({
        'candidateId':    cid,
        'qualifications': dict(qual)  if qual  else None,
        'skills':         [dict(s) for s in skills],
        'experience':     [dict(e) for e in exps],
        'score':          dict(score) if score else None,
        'isShortlisted':  bool(cand['is_shortlisted']) if cand else False,
        'shortlistNote':  cand['shortlist_note'] if cand else '',
    })


@app.route('/api/hr/shortlist/<cid>', methods=['POST'])
@require_hr
def hr_shortlist(cid):
    """HR shortlists a candidate. Admin can then see full contact info."""
    d = request.json or {}
    note = d.get('note', '')
    with get_db() as conn:
        row = conn.execute('SELECT id FROM candidates WHERE id=?', (cid,)).fetchone()
        if not row:
            return jsonify({'error': 'Candidate not found'}), 404
        conn.execute(
            'UPDATE candidates SET is_shortlisted=1, shortlisted_at=?, shortlist_note=? WHERE id=?',
            (datetime.now(), note, cid)
        )
        conn.commit()
    return jsonify({'success': True, 'message': f'Candidate {cid} shortlisted'})


@app.route('/api/hr/shortlist/<cid>', methods=['DELETE'])
@require_hr
def hr_remove_shortlist(cid):
    """HR removes a candidate from shortlist."""
    with get_db() as conn:
        conn.execute(
            'UPDATE candidates SET is_shortlisted=0, shortlisted_at=NULL, shortlist_note=NULL WHERE id=?',
            (cid,)
        )
        conn.commit()
    return jsonify({'success': True})


@app.route('/api/hr/report/<cid>', methods=['GET'])
@require_hr
def download_report(cid):
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib import colors
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    except ImportError:
        return jsonify({'error': 'reportlab not installed. Run: pip install reportlab'}), 500

    with get_db() as conn:
        qual   = conn.execute('SELECT * FROM qualifications WHERE candidate_id=?', (cid,)).fetchone()
        skills = conn.execute('SELECT skill_name, is_verified, confidence, notes FROM skills WHERE candidate_id=?', (cid,)).fetchall()
        exps   = conn.execute('SELECT role, duration_months, description FROM experience WHERE candidate_id=?', (cid,)).fetchall()
        score  = conn.execute('SELECT * FROM scores WHERE candidate_id=?', (cid,)).fetchone()

    if not score:
        return jsonify({'error': 'Candidate not verified yet'}), 404

    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, topMargin=40, bottomMargin=40)
    C_ACCENT = colors.HexColor('#4f46e5')
    C_LIGHT  = colors.HexColor('#eef2ff')
    C_TEXT   = colors.HexColor('#1e1b4b')
    styles = getSampleStyleSheet()
    h1 = ParagraphStyle('H1', fontSize=22, textColor=C_ACCENT, spaceAfter=4, fontName='Helvetica-Bold')
    h2 = ParagraphStyle('H2', fontSize=13, textColor=C_TEXT,   spaceAfter=4, spaceBefore=14, fontName='Helvetica-Bold')
    sm = ParagraphStyle('SM', fontSize=9,  textColor=colors.HexColor('#6b7280'))

    story = [
        Paragraph('FairHire — Candidate Evaluation Report', h1),
        Paragraph('All personal identifiers removed. Bias-free evaluation.', sm),
        Spacer(1, 6),
        HRFlowable(width='100%', thickness=1, color=C_ACCENT),
        Spacer(1, 12),
        Paragraph(f'Candidate ID: <b>{cid}</b>', styles['Normal']),
        Paragraph(f'Generated: {datetime.now().strftime("%d %b %Y, %H:%M")}', sm),
        Spacer(1, 20),
    ]

    def tbl(data, col_widths):
        t = Table(data, colWidths=col_widths)
        t.setStyle(TableStyle([
            ('BACKGROUND',  (0,0), (-1,0), C_ACCENT),
            ('TEXTCOLOR',   (0,0), (-1,0), colors.white),
            ('FONTNAME',    (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE',    (0,0), (-1,-1), 10),
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, C_LIGHT]),
            ('GRID',        (0,0), (-1,-1), 0.4, colors.HexColor('#d1d5db')),
            ('LEFTPADDING',  (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
            ('TOPPADDING',   (0,0), (-1,-1), 6),
            ('BOTTOMPADDING',(0,0), (-1,-1), 6),
        ]))
        return t

    story.append(Paragraph('Academic Performance', h2))
    if qual:
        q = dict(qual)
        story.append(tbl([
            ['Metric', 'Value'],
            ['10th Percentage', f"{q.get('tenth_percentage') or '—'}%"],
            ['10th Board',      q.get('tenth_board') or '—'],
            ['12th Percentage', f"{q.get('twelfth_percentage') or '—'}%"],
            ['12th Board',      q.get('twelfth_board') or '—'],
            ['Degree',          q.get('degree') or '—'],
            ['Branch / Major',  q.get('branch') or '—'],
            ['CGPA',            str(q.get('cgpa') or '—')],
        ], [220, 270]))
    story.append(Spacer(1, 16))

    story.append(Paragraph('Skills Assessment', h2))
    sk_rows = [['Skill', 'Verified', 'Confidence', 'Notes']]
    for s in skills:
        sk_rows.append([s['skill_name'], '✓ Yes' if s['is_verified'] else '✗ No',
                        f"{int(s['confidence'] or 0)}%", (s['notes'] or '')[:60]])
    if len(sk_rows) > 1:
        story.append(tbl(sk_rows, [130, 70, 80, 210]))
    story.append(Spacer(1, 16))

    story.append(Paragraph('Experience', h2))
    ex_rows = [['Role', 'Duration', 'Notes']]
    for e in exps:
        months = e['duration_months'] or 0
        ex_rows.append([e['role'] or '—',
                        f"{months // 12}y {months % 12}m" if months >= 12 else f"{months}m",
                        (e['description'] or '')[:70]])
    if len(ex_rows) > 1:
        story.append(tbl(ex_rows, [160, 80, 250]))
    story.append(Spacer(1, 16))

    story.append(Paragraph('Score Summary', h2))
    sc = dict(score)
    story.append(tbl([
        ['Component',          'Score'],
        ['Academic Score',     f"{sc.get('academic_score',0):.1f} / 100"],
        ['Skill Score',        f"{sc.get('skill_score',0):.1f} / 100"],
        ['Verification Score', f"{sc.get('verification_score',0):.1f} / 100"],
        ['Experience Score',   f"{sc.get('experience_score',0):.1f} / 100"],
        ['FINAL SCORE',        f"{sc.get('final_score',0):.1f} / 100"],
        ['Confidence Level',   sc.get('confidence_level','—')],
    ], [220, 270]))
    story += [
        Spacer(1, 30),
        HRFlowable(width='100%', thickness=0.5, color=colors.HexColor('#d1d5db')),
        Spacer(1, 6),
        Paragraph('Generated by FairHire AI. No personal identifiers included.', sm),
    ]

    doc.build(story)
    buf.seek(0)
    return send_file(buf, as_attachment=True,
                     download_name=f'FairHire_{cid}.pdf',
                     mimetype='application/pdf')


# ─────────────────────────────────────────────
# ADMIN ENDPOINTS  (full access to everything)
# ─────────────────────────────────────────────

@app.route('/api/admin/login', methods=['POST'])
def admin_login():
    d = request.json or {}
    with get_db() as conn:
        row = conn.execute('SELECT * FROM admin_users WHERE username=?', (d.get('username', ''),)).fetchone()
    if not row or not check_password_hash(row['password_hash'], d.get('password', '')):
        return jsonify({'error': 'Invalid admin credentials'}), 401
    token = str(uuid.uuid4())
    with get_db() as conn:
        conn.execute('UPDATE admin_users SET token=? WHERE id=?', (token, row['id']))
        conn.commit()
    return jsonify({'success': True, 'token': token})


@app.route('/api/admin/candidates', methods=['GET'])
@require_admin
def admin_candidates():
    """Admin sees ALL candidate data including shortlist status."""
    with get_db() as conn:
        rows = conn.execute('''
            SELECT c.id, c.full_name, c.email, c.phone, c.dob, c.address,
                   c.gov_id_type, c.gov_id_number,
                   c.is_shortlisted, c.shortlisted_at, c.shortlist_note, c.created_at,
                   s.final_score, s.confidence_level
            FROM   candidates c
            LEFT JOIN scores s ON c.id = s.candidate_id
            ORDER  BY c.is_shortlisted DESC, COALESCE(s.final_score, 0) DESC
        ''').fetchall()

        result = []
        for r in rows:
            result.append({
                'candidateId':    r['id'],
                'fullName':       r['full_name'],
                'email':          r['email'],
                'phone':          r['phone'],
                'dob':            r['dob'],
                'address':        r['address'],
                'govIdType':      r['gov_id_type'],
                'govIdNumber':    r['gov_id_number'],
                'isShortlisted':  bool(r['is_shortlisted']),
                'shortlistedAt':  r['shortlisted_at'],
                'shortlistNote':  r['shortlist_note'],
                'registeredAt':   r['created_at'],
                'finalScore':     r['final_score'],
                'confidenceLevel':r['confidence_level'],
            })
    return jsonify(result)


@app.route('/api/admin/candidate/<cid>', methods=['GET'])
@require_admin
def admin_candidate_detail(cid):
    """Admin gets EVERYTHING: photo, signature, documents, password, all data."""
    with get_db() as conn:
        c      = conn.execute('SELECT * FROM candidates WHERE id=?', (cid,)).fetchone()
        qual   = conn.execute('SELECT * FROM qualifications WHERE candidate_id=?', (cid,)).fetchone()
        skills = conn.execute('SELECT * FROM skills WHERE candidate_id=?', (cid,)).fetchall()
        exps   = conn.execute('SELECT * FROM experience WHERE candidate_id=?', (cid,)).fetchall()
        score  = conn.execute('SELECT * FROM scores WHERE candidate_id=?', (cid,)).fetchone()
        docs   = conn.execute('SELECT id, doc_name, doc_type, doc_data, uploaded_at FROM career_documents WHERE candidate_id=?', (cid,)).fetchall()

    if not c:
        return jsonify({'error': 'Candidate not found'}), 404

    c = dict(c)
    return jsonify({
        'candidateId':    cid,
        # Full identity — admin only
        'fullName':       c['full_name'],
        'email':          c['email'],
        'phone':          c['phone'],
        'dob':            c['dob'],
        'address':        c['address'],
        'govIdType':      c['gov_id_type'],
        'govIdNumber':    c['gov_id_number'],
        'passwordPlain':  c['password_plain'],    # plain text — admin only
        'photoData':      c['photo_data'] or '',
        'signatureData':  c['signature_data'] or '',
        'registeredAt':   c['created_at'],
        'isShortlisted':  bool(c['is_shortlisted']),
        'shortlistedAt':  c['shortlisted_at'],
        'shortlistNote':  c['shortlist_note'],
        # Qualifications
        'qualifications': dict(qual) if qual else None,
        # Skills
        'skills':         [dict(s) for s in skills],
        # Experience (with company names)
        'experience':     [dict(e) for e in exps],
        # Scores
        'score':          dict(score) if score else None,
        # Career documents — full data
        'documents':      [{
            'id':       d['id'],
            'name':     d['doc_name'],
            'type':     d['doc_type'],
            'data':     d['doc_data'],
            'uploadedAt': d['uploaded_at'],
        } for d in docs],
    })


@app.route('/api/admin/shortlisted', methods=['GET'])
@require_admin
def admin_shortlisted():
    """Admin sees all shortlisted candidates with full contact for outreach."""
    with get_db() as conn:
        rows = conn.execute('''
            SELECT c.id, c.full_name, c.email, c.phone, c.address,
                   c.shortlisted_at, c.shortlist_note,
                   s.final_score, s.confidence_level
            FROM   candidates c
            LEFT JOIN scores s ON c.id = s.candidate_id
            WHERE  c.is_shortlisted = 1
            ORDER  BY COALESCE(s.final_score, 0) DESC
        ''').fetchall()
        result = []
        for r in rows:
            cid  = r['id']
            sks  = conn.execute('SELECT skill_name, is_verified FROM skills WHERE candidate_id=?', (cid,)).fetchall()
            result.append({
                'candidateId':   cid,
                'fullName':      r['full_name'],
                'email':         r['email'],
                'phone':         r['phone'],
                'address':       r['address'],
                'shortlistedAt': r['shortlisted_at'],
                'shortlistNote': r['shortlist_note'],
                'finalScore':    r['final_score'],
                'confidenceLevel': r['confidence_level'],
                'skills':        [{'name': s['skill_name'], 'verified': bool(s['is_verified'])} for s in sks],
            })
    return jsonify(result)


@app.route('/api/admin/stats', methods=['GET'])
@require_admin
def admin_stats():
    with get_db() as conn:
        total      = conn.execute('SELECT COUNT(*) AS n FROM candidates').fetchone()['n']
        shortlisted= conn.execute('SELECT COUNT(*) AS n FROM candidates WHERE is_shortlisted=1').fetchone()['n']
        verified   = conn.execute('SELECT COUNT(*) AS n FROM scores').fetchone()['n']
        avg_score  = conn.execute('SELECT AVG(final_score) AS a FROM scores').fetchone()['a']
    return jsonify({
        'totalCandidates':    total,
        'shortlisted':        shortlisted,
        'verified':           verified,
        'avgScore':           round(avg_score or 0, 1),
    })


# ─────────────────────────────────────────────
# SCORING / AI HELPERS
# ─────────────────────────────────────────────

def _academic_score(q):
    tenth   = float(q.get('tenth_percentage')  or 0)
    twelfth = float(q.get('twelfth_percentage') or 0)
    cgpa    = float(q.get('cgpa') or 0) * 10
    return round(tenth * 0.25 + twelfth * 0.25 + cgpa * 0.50, 1)


def _verify_basic(skills):
    results = []
    for s in skills:
        has_cert = bool(s.get('cert_data', '').strip())
        results.append({
            'name':       s['skill_name'],
            'verified':   has_cert,
            'confidence': 72 if has_cert else 28,
            'notes':      'Certificate uploaded — basic check passed.' if has_cert
                          else 'No certificate provided; marked unverified.',
        })
    return results


def _verify_gemini(skills):
    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
    except ImportError:
        return _verify_basic(skills)

    results = []
    for s in skills:
        name     = s['skill_name']
        has_cert = bool(s.get('cert_data', '').strip())
        prompt = f"""You are an AI recruiter reviewing a skill claim.
Skill declared: "{name}"
Certificate uploaded: {"Yes" if has_cert else "No"}
Evaluate: 1) Is this a real industry-recognised skill? 2) Verification confidence 0-100? 3) Any concerns?
Reply ONLY with valid JSON, no markdown:
{{"verified": true or false, "confidence": 0-100, "notes": "one sentence"}}"""
        try:
            resp = model.generate_content(prompt)
            text = resp.text.strip()
            m    = re.search(r'\{.*?\}', text, re.DOTALL)
            if m:
                obj = json.loads(m.group())
                results.append({
                    'name':       name,
                    'verified':   bool(obj.get('verified', False)),
                    'confidence': int(obj.get('confidence', 50)),
                    'notes':      str(obj.get('notes', '')),
                })
                continue
        except Exception:
            pass
        results.append({
            'name': name, 'verified': has_cert,
            'confidence': 60 if has_cert else 25,
            'notes': 'Certificate present.' if has_cert else 'No certificate.',
        })
    return results


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == '__main__':
    init_db()
    print('\n' + '='*55)
    print('  FairHire Backend  →  http://localhost:5000')
    print('  HR Login     →  hr@fairhire.com    / hr123')
    print('  Admin Login  →  admin@fairhire.com / admin123')
    print('='*55 + '\n')
    app.run(host='0.0.0.0', port=5000, debug=True)
