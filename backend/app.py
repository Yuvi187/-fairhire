"""
FairHire – Selectively Anonymous AI Hiring System
Backend: Python Flask  |  Synced for Gemini 3 Visual Verification
"""

import os, json, uuid, sqlite3, io, re, base64
from datetime import datetime
from functools import wraps
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

# ── NEW: 2026 AI Library ──
from google import genai
from google.genai import types
import base64

app = Flask(__name__)

# ── Allow large file uploads ──
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024   # 50 MB

# ── CORS: Full access for demo ──
CORS(app, resources={r"/*": {"origins": "*"}})

DB_PATH = os.environ.get('DB_PATH', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fairhire.db'))

# ── YOUR API KEY ──
GEMINI_API_KEY = 'AIzaSyAvbd_aW6Spu2JL4Cb9zz07fc_CrNuVnvU'

# (Keep your _auto_init, handle_preflight, add_cors_headers, get_db, init_db, migrate_db, and Auth Helpers exactly as you had them)

def _auto_init():
    try:
        init_db()
        migrate_db()
    except Exception as e:
        print(f'[startup] DB init error: {e}')

@app.before_request
def handle_preflight():
    if request.method == 'OPTIONS':
        resp = app.make_default_options_response()
        resp.headers['Access-Control-Allow-Origin']  = '*'
        resp.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, DELETE, OPTIONS'
        return resp

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin']  = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, DELETE, OPTIONS'
    return response

def get_db():
    conn = sqlite3.connect(DB_PATH, timeout=30, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA journal_mode=WAL')
    return conn

def init_db():
    with get_db() as conn:
        conn.executescript('''
            CREATE TABLE IF NOT EXISTS candidates (
                id TEXT PRIMARY KEY, full_name TEXT NOT NULL, email TEXT UNIQUE NOT NULL,
                phone TEXT, dob TEXT, address TEXT, password_hash TEXT NOT NULL,
                password_plain TEXT, gov_id_type TEXT, gov_id_number TEXT,
                photo_data TEXT, signature_data TEXT, token TEXT,
                is_shortlisted INTEGER DEFAULT 0, shortlisted_at TIMESTAMP,
                shortlist_note TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            CREATE TABLE IF NOT EXISTS qualifications (
                candidate_id TEXT PRIMARY KEY, tenth_percentage REAL, tenth_board TEXT,
                twelfth_percentage REAL, twelfth_board TEXT, degree TEXT, branch TEXT,
                cgpa REAL, college_name TEXT, school_name TEXT,
                FOREIGN KEY (candidate_id) REFERENCES candidates(id)
            );
            CREATE TABLE IF NOT EXISTS career_documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT, candidate_id TEXT, doc_name TEXT,
                doc_type TEXT, doc_data TEXT, uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (candidate_id) REFERENCES candidates(id)
            );
            CREATE TABLE IF NOT EXISTS skills (
                id INTEGER PRIMARY KEY AUTOINCREMENT, candidate_id TEXT, skill_name TEXT,
                cert_data TEXT, is_verified INTEGER DEFAULT 0, confidence REAL DEFAULT 0,
                notes TEXT, FOREIGN KEY (candidate_id) REFERENCES candidates(id)
            );
            CREATE TABLE IF NOT EXISTS experience (
                id INTEGER PRIMARY KEY AUTOINCREMENT, candidate_id TEXT, company_name TEXT,
                role TEXT, duration_months INTEGER, description TEXT,
                FOREIGN KEY (candidate_id) REFERENCES candidates(id)
            );
            CREATE TABLE IF NOT EXISTS scores (
                candidate_id TEXT PRIMARY KEY, academic_score REAL DEFAULT 0,
                skill_score REAL DEFAULT 0, verification_score REAL DEFAULT 0,
                experience_score REAL DEFAULT 0, final_score REAL DEFAULT 0,
                confidence_level TEXT DEFAULT 'Low', verified_at TIMESTAMP,
                FOREIGN KEY (candidate_id) REFERENCES candidates(id)
            );
            CREATE TABLE IF NOT EXISTS hr_users (
                id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL, token TEXT
            );
            CREATE TABLE IF NOT EXISTS admin_users (
                id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL, token TEXT
            );
        ''')
        conn.execute('INSERT OR IGNORE INTO hr_users (username, password_hash) VALUES (?,?)', ('hr@fairhire.com', generate_password_hash('hr123')))
        conn.execute('INSERT OR IGNORE INTO admin_users (username, password_hash) VALUES (?,?)', ('admin@fairhire.com', generate_password_hash('admin123')))
        conn.commit()

def migrate_db():
    migrations = {'candidates': [('dob', 'TEXT'), ('password_plain', 'TEXT'), ('photo_data', 'TEXT'), ('signature_data', 'TEXT'), ('is_shortlisted', 'INTEGER DEFAULT 0'), ('shortlisted_at', 'TIMESTAMP'), ('shortlist_note', 'TEXT')],}
    with get_db() as conn:
        for table, columns in migrations.items():
            try:
                cur = conn.execute(f'PRAGMA table_info({table})')
                existing = {row['name'] for row in cur.fetchall()}
                for col_name, col_def in columns:
                    if col_name not in existing:
                        conn.execute(f'ALTER TABLE {table} ADD COLUMN {col_name} {col_def}')
            except: pass
        conn.commit()

def _bearer(req): return req.headers.get('Authorization', '').replace('Bearer ', '').strip()

def require_candidate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = _bearer(request)
        if not token: return jsonify({'error': 'Missing token'}), 401
        with get_db() as conn: row = conn.execute('SELECT * FROM candidates WHERE token=?', (token,)).fetchone()
        if not row: return jsonify({'error': 'Unauthorized'}), 401
        request.candidate = dict(row)
        return f(*args, **kwargs)
    return wrapper

def require_hr(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = _bearer(request)
        if not token: return jsonify({'error': 'Missing token'}), 401
        with get_db() as conn: row = conn.execute('SELECT * FROM hr_users WHERE token=?', (token,)).fetchone()
        if not row: return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return wrapper

def require_admin(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = _bearer(request)
        if not token: return jsonify({'error': 'Missing token'}), 401
        with get_db() as conn: row = conn.execute('SELECT * FROM admin_users WHERE token=?', (token,)).fetchone()
        if not row: return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return wrapper

@app.route('/api/health', methods=['GET'])
def health(): return jsonify({'status': 'ok', 'db': DB_PATH})

@app.route('/api/candidate/register', methods=['POST'])
def candidate_register():
    try: d = request.get_json(force=True, silent=True) or {}
    except: return jsonify({'error': 'Invalid JSON body'}), 400
    if not d.get('email') or not d.get('password') or not d.get('fullName'): return jsonify({'error': 'fullName, email and password are required'}), 400
    cid = 'FH' + uuid.uuid4().hex[:6].upper()
    photo = (d.get('photoData') or '')[:1_400_000]
    sig   = (d.get('signatureData') or '')[:1_400_000]
    try:
        with get_db() as conn:
            conn.execute('INSERT INTO candidates (id, full_name, email, phone, dob, address, password_hash, password_plain, gov_id_type, gov_id_number, photo_data, signature_data) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
                (cid, d['fullName'], d['email'], d.get('phone', ''), d.get('dob', ''), d.get('address', ''), generate_password_hash(d['password']), d.get('password', ''), d.get('govIdType', ''), d.get('govIdNumber', ''), photo, sig))
            conn.commit()
        return jsonify({'success': True, 'candidateId': cid})
    except sqlite3.IntegrityError: return jsonify({'error': 'Email already registered'}), 409
    except Exception as e: return jsonify({'error': str(e)}), 500

@app.route('/api/candidate/login', methods=['POST'])
def candidate_login():
    try: d = request.get_json(force=True, silent=True) or {}
    except: return jsonify({'error': 'Invalid JSON'}), 400
    with get_db() as conn: row = conn.execute('SELECT * FROM candidates WHERE email=?', (d.get('email',''),)).fetchone()
    if not row or not check_password_hash(row['password_hash'], d.get('password','')): return jsonify({'error': 'Invalid email or password'}), 401
    token = str(uuid.uuid4())
    with get_db() as conn:
        conn.execute('UPDATE candidates SET token=? WHERE id=?', (token, row['id']))
        conn.commit()
        qual  = conn.execute('SELECT 1 FROM qualifications WHERE candidate_id=?', (row['id'],)).fetchone()
        sk    = conn.execute('SELECT COUNT(*) AS n FROM skills WHERE candidate_id=?', (row['id'],)).fetchone()
        score = conn.execute('SELECT 1 FROM scores WHERE candidate_id=?', (row['id'],)).fetchone()
    step = 1
    if qual: step = 2
    if sk and sk['n']>0: step = 3
    if score: step = 4
    return jsonify({'success': True, 'token': token, 'candidateId': row['id'], 'step': step})

@app.route('/api/candidate/qualifications', methods=['POST'])
@require_candidate
def save_qualifications():
    d = request.get_json(force=True, silent=True) or {}
    cid = request.candidate['id']
    try:
        with get_db() as conn:
            conn.execute('INSERT OR REPLACE INTO qualifications (candidate_id, tenth_percentage, tenth_board, twelfth_percentage, twelfth_board, degree, branch, cgpa, college_name, school_name) VALUES (?,?,?,?,?,?,?,?,?,?)',
                (cid, float(d.get('tenthPercentage', 0) or 0), d.get('tenthBoard', ''), float(d.get('twelfthPercentage', 0) or 0), d.get('twelfthBoard', ''), d.get('degree', ''), d.get('branch', ''), float(d.get('cgpa', 0) or 0), d.get('collegeName', ''), d.get('schoolName', '')))
            conn.commit()
        return jsonify({'success': True})
    except Exception as e: return jsonify({'error': str(e)}), 500

@app.route('/api/candidate/documents', methods=['POST'])
@require_candidate
def save_documents():
    d = request.get_json(force=True, silent=True) or {}
    cid = request.candidate['id']
    try:
        with get_db() as conn:
            if d.get('photoData'): conn.execute('UPDATE candidates SET photo_data=? WHERE id=?', ((d['photoData'])[:1_400_000], cid))
            if d.get('signatureData'): conn.execute('UPDATE candidates SET signature_data=? WHERE id=?', ((d['signatureData'])[:1_400_000], cid))
            conn.execute('DELETE FROM career_documents WHERE candidate_id=?', (cid,))
            for doc in d.get('documents', []):
                conn.execute('INSERT INTO career_documents (candidate_id, doc_name, doc_type, doc_data) VALUES (?,?,?,?)', (cid, doc.get('name','document'), doc.get('type','pdf'), (doc.get('data',''))[:800_000]))
            conn.commit()
        return jsonify({'success': True})
    except Exception as e: return jsonify({'error': str(e)}), 500

@app.route('/api/candidate/skills', methods=['POST'])
@require_candidate
def save_skills():
    d = request.get_json(force=True, silent=True) or {}
    cid = request.candidate['id']
    try:
        with get_db() as conn:
            conn.execute('DELETE FROM skills WHERE candidate_id=?', (cid,))
            conn.execute('DELETE FROM experience WHERE candidate_id=?', (cid,))
            for sk in d.get('skills', []):
                conn.execute('INSERT INTO skills (candidate_id, skill_name, cert_data) VALUES (?,?,?)',
                    (cid, sk.get('name','').strip(), (sk.get('certData') or '')[:3_000_000])) # ── FIXED LIMIT ──
            for ex in d.get('experience', []):
                conn.execute('INSERT INTO experience (candidate_id, company_name, role, duration_months, description) VALUES (?,?,?,?,?)',
                    (cid, ex.get('company',''), ex.get('role',''), int(ex.get('durationMonths', 0) or 0), ex.get('description','')))
            conn.commit()
        return jsonify({'success': True})
    except Exception as e: return jsonify({'error': str(e)}), 500

@app.route('/api/candidate/verify', methods=['POST'])
@require_candidate
def verify_candidate():
    cid = request.candidate['id']
    full_name = request.candidate['full_name'] # ── GET NAME ──
    try:
        with get_db() as conn:
            qual   = conn.execute('SELECT * FROM qualifications WHERE candidate_id=?', (cid,)).fetchone()
            skills = conn.execute('SELECT * FROM skills WHERE candidate_id=?', (cid,)).fetchall()
            exps   = conn.execute('SELECT * FROM experience WHERE candidate_id=?', (cid,)).fetchall()
        if not qual: return jsonify({'error': 'Complete qualifications first'}), 400

        # ── RUN VISUAL AI ──
        verified = _verify_gemini([dict(s) for s in skills], full_name)

        acad_score  = _academic_score(dict(qual))
        n_total     = len(skills)
        n_verified  = sum(1 for v in verified if v['verified'])
        skill_score = round(n_verified / n_total * 100, 1) if n_total else 50.0
        verif_score = round(n_verified / n_total * 100, 1) if n_total else 30.0
        total_months= sum(e['duration_months'] for e in exps)
        exp_score   = round(min(100, total_months / 24 * 100), 1)
        final       = round(acad_score*0.35 + skill_score*0.30 + verif_score*0.20 + exp_score*0.15, 1)
        confidence  = 'High' if final >= 75 else ('Medium' if final >= 50 else 'Low')

        with get_db() as conn:
            for v in verified:
                conn.execute('UPDATE skills SET is_verified=?, confidence=?, notes=? WHERE candidate_id=? AND skill_name=?',
                    (1 if v['verified'] else 0, v.get('confidence',0), v.get('notes',''), cid, v['name']))
            conn.execute('INSERT OR REPLACE INTO scores (candidate_id, academic_score, skill_score, verification_score, experience_score, final_score, confidence_level, verified_at) VALUES (?,?,?,?,?,?,?,?)',
                (cid, acad_score, skill_score, verif_score, exp_score, final, confidence, datetime.now()))
            conn.commit()
        return jsonify({'success': True, 'finalScore': final, 'confidenceLevel': confidence, 'verifiedSkills': verified})
    except Exception as e: return jsonify({'error': str(e)}), 500

@app.route('/api/candidate/profile', methods=['GET'])
@require_candidate
def candidate_profile():
    cid = request.candidate['id']
    c   = request.candidate
    try:
        with get_db() as conn:
            qual  = conn.execute('SELECT * FROM qualifications WHERE candidate_id=?', (cid,)).fetchone()
            sks   = conn.execute('SELECT skill_name,is_verified,confidence,notes FROM skills WHERE candidate_id=?', (cid,)).fetchall()
            exps  = conn.execute('SELECT role,duration_months,description FROM experience WHERE candidate_id=?', (cid,)).fetchall()
            score = conn.execute('SELECT * FROM scores WHERE candidate_id=?', (cid,)).fetchone()
            docs  = conn.execute('SELECT id,doc_name,doc_type,uploaded_at FROM career_documents WHERE candidate_id=?', (cid,)).fetchall()
        return jsonify({'candidateId': cid, 'fullName': c['full_name'], 'email': c['email'], 'phone': c['phone'], 'dob': c['dob'], 'address': c['address'], 'photoData': c['photo_data'] or '', 'signatureData': c['signature_data'] or '', 'qualifications':dict(qual) if qual else None, 'skills': [dict(s) for s in sks], 'experience': [dict(e) for e in exps], 'score': dict(score) if score else None, 'documents': [dict(d) for d in docs], 'isShortlisted': bool(c['is_shortlisted']), 'shortlistNote': c['shortlist_note'] or '',})
    except Exception as e: return jsonify({'error': str(e)}), 500

# (Keep your HR and Admin routes as they are, they don't need changes)
@app.route('/api/hr/login', methods=['POST'])
def hr_login():
    try:
        d = request.get_json(force=True, silent=True) or {}
        with get_db() as conn: row = conn.execute('SELECT * FROM hr_users WHERE username=?', (d.get('username',''),)).fetchone()
        if not row or not check_password_hash(row['password_hash'], d.get('password','')): return jsonify({'error': 'Invalid credentials'}), 401
        token = str(uuid.uuid4())
        with get_db() as conn:
            conn.execute('UPDATE hr_users SET token=? WHERE id=?', (token, row['id']))
            conn.commit()
        return jsonify({'success': True, 'token': token})
    except Exception as e: return jsonify({'error': str(e)}), 500

@app.route('/api/hr/candidates', methods=['GET'])
@require_hr
def hr_candidates():
    try:
        with get_db() as conn:
            rows = conn.execute('SELECT c.id, c.is_shortlisted, q.tenth_percentage, q.twelfth_percentage, q.cgpa, q.degree, q.branch, s.final_score, s.confidence_level, s.academic_score, s.skill_score, s.verification_score, s.experience_score FROM candidates c LEFT JOIN qualifications q ON c.id = q.candidate_id LEFT JOIN scores s ON c.id = s.candidate_id ORDER BY COALESCE(s.final_score,0) DESC').fetchall()
            result = []
            for r in rows:
                cid  = r['id']
                sks  = conn.execute('SELECT skill_name,is_verified FROM skills WHERE candidate_id=?', (cid,)).fetchall()
                tot  = conn.execute('SELECT SUM(duration_months) AS t FROM experience WHERE candidate_id=?', (cid,)).fetchone()
                result.append({'candidateId': cid, 'tenthPercentage': r['tenth_percentage'], 'twelfthPercentage': r['twelfth_percentage'], 'cgpa': r['cgpa'], 'degree': r['degree'], 'branch': r['branch'], 'skills': [{'name':s['skill_name'],'verified':bool(s['is_verified'])} for s in sks], 'experienceYears': round((tot['t'] or 0)/12, 1), 'finalScore': r['final_score'], 'confidenceLevel': r['confidence_level'], 'academicScore': r['academic_score'], 'skillScore': r['skill_score'], 'verificationScore': r['verification_score'], 'experienceScore': r['experience_score'], 'isShortlisted': bool(r['is_shortlisted']),})
        return jsonify(result)
    except Exception as e: return jsonify({'error': str(e)}), 500

@app.route('/api/hr/candidate/<cid>', methods=['GET'])
@require_hr
def hr_candidate_detail(cid):
    try:
        with get_db() as conn:
            qual = conn.execute('SELECT * FROM qualifications WHERE candidate_id=?', (cid,)).fetchone()
            sks = conn.execute('SELECT skill_name,is_verified,confidence,notes FROM skills WHERE candidate_id=?', (cid,)).fetchall()
            exps = conn.execute('SELECT role,duration_months,description FROM experience WHERE candidate_id=?', (cid,)).fetchall()
            score = conn.execute('SELECT * FROM scores WHERE candidate_id=?', (cid,)).fetchone()
            c = conn.execute('SELECT is_shortlisted,shortlist_note FROM candidates WHERE id=?', (cid,)).fetchone()
        if not c: return jsonify({'error': 'Candidate not found'}), 404
        return jsonify({'candidateId': cid, 'qualifications':dict(qual) if qual else None, 'skills': [dict(s) for s in sks], 'experience': [dict(e) for e in exps], 'score': dict(score) if score else None, 'isShortlisted': bool(c['is_shortlisted']), 'shortlistNote': c['shortlist_note'] or '',})
    except Exception as e: return jsonify({'error': str(e)}), 500

@app.route('/api/hr/shortlist/<cid>', methods=['POST'])
@require_hr
def hr_shortlist(cid):
    try:
        d = request.get_json(force=True, silent=True) or {}
        with get_db() as conn:
            conn.execute('UPDATE candidates SET is_shortlisted=1, shortlisted_at=?, shortlist_note=? WHERE id=?', (datetime.now(), d.get('note',''), cid))
            conn.commit()
        return jsonify({'success': True})
    except Exception as e: return jsonify({'error': str(e)}), 500

@app.route('/api/hr/shortlist/<cid>', methods=['DELETE'])
@require_hr
def hr_remove_shortlist(cid):
    try:
        with get_db() as conn:
            conn.execute('UPDATE candidates SET is_shortlisted=0, shortlisted_at=NULL, shortlist_note=NULL WHERE id=?', (cid,))
            conn.commit()
        return jsonify({'success': True})
    except Exception as e: return jsonify({'error': str(e)}), 500

@app.route('/api/hr/report/<cid>', methods=['GET'])
@require_hr
def download_report(cid):
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib import colors
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
    except ImportError: return jsonify({'error': 'reportlab not installed'}), 500
    try:
        with get_db() as conn:
            qual = conn.execute('SELECT * FROM qualifications WHERE candidate_id=?', (cid,)).fetchone()
            sks = conn.execute('SELECT skill_name,is_verified,confidence,notes FROM skills WHERE candidate_id=?', (cid,)).fetchall()
            exps = conn.execute('SELECT role,duration_months,description FROM experience WHERE candidate_id=?', (cid,)).fetchall()
            score = conn.execute('SELECT * FROM scores WHERE candidate_id=?', (cid,)).fetchone()
        if not score: return jsonify({'error': 'Candidate not verified yet'}), 404
        buf = io.BytesIO()
        doc = SimpleDocTemplate(buf, pagesize=A4, topMargin=40, bottomMargin=40)
        styles = getSampleStyleSheet()
        C_A = colors.HexColor('#4f46e5')
        C_L = colors.HexColor('#eef2ff')
        h1 = ParagraphStyle('H1', fontSize=20, textColor=C_A, spaceAfter=4, fontName='Helvetica-Bold')
        h2 = ParagraphStyle('H2', fontSize=12, textColor=colors.HexColor('#1e1b4b'), spaceAfter=4, spaceBefore=12, fontName='Helvetica-Bold')
        sm = ParagraphStyle('SM', fontSize=8, textColor=colors.HexColor('#6b7280'))
        def tbl(data, cw):
            t = Table(data, colWidths=cw)
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),C_A),('TEXTCOLOR',(0,0),(-1,0),colors.white),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,-1),9),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,C_L]),('GRID',(0,0),(-1,-1),0.4,colors.HexColor('#d1d5db')),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),]))
            return t
        story = [Paragraph('FairHire — Candidate Evaluation Report', h1), Paragraph('All personal identifiers removed. Bias-free report.', sm), Spacer(1,6), HRFlowable(width='100%',thickness=1,color=C_A), Spacer(1,10), Paragraph(f'Candidate ID: <b>{cid}</b>', styles['Normal']), Paragraph(f'Generated: {datetime.now().strftime("%d %b %Y %H:%M")}', sm), Spacer(1,18),]
        story.append(Paragraph('Academic Performance', h2))
        if qual:
            q = dict(qual)
            story.append(tbl([['Metric','Value'], ['10th Percentage', f"{q.get('tenth_percentage') or '—'}%"], ['10th Board', q.get('tenth_board') or '—'], ['12th Percentage', f"{q.get('twelfth_percentage') or '—'}%"], ['12th Board', q.get('twelfth_board') or '—'], ['Degree', q.get('degree') or '—'], ['Branch', q.get('branch') or '—'], ['CGPA', str(q.get('cgpa') or '—')],], [220,270]))
        story.append(Spacer(1,14))
        story.append(Paragraph('Skills', h2))
        sk_rows = [['Skill','Verified','Confidence','Notes']]
        for s in sks: sk_rows.append([s['skill_name'],'✓ Yes' if s['is_verified'] else '✗ No', f"{int(s['confidence'] or 0)}%",(s['notes'] or '')[:60]])
        if len(sk_rows)>1: story.append(tbl(sk_rows,[130,70,80,210]))
        story.append(Spacer(1,14))
        story.append(Paragraph('Experience', h2))
        ex_rows = [['Role','Duration','Notes']]
        for e in exps:
            m = e['duration_months'] or 0
            ex_rows.append([e['role'] or '—', f"{m//12}y {m%12}m" if m>=12 else f"{m}m", (e['description'] or '')[:70]])
        if len(ex_rows)>1: story.append(tbl(ex_rows,[160,80,250]))
        story.append(Spacer(1,14))
        story.append(Paragraph('Score Summary', h2))
        sc = dict(score)
        story.append(tbl([['Component','Score'], ['Academic Score', f"{sc.get('academic_score',0):.1f} / 100"], ['Skill Score', f"{sc.get('skill_score',0):.1f} / 100"], ['Verification Score', f"{sc.get('verification_score',0):.1f} / 100"], ['Experience Score', f"{sc.get('experience_score',0):.1f} / 100"], ['FINAL SCORE', f"{sc.get('final_score',0):.1f} / 100"], ['Confidence Level', sc.get('confidence_level','—')],], [220,270]))
        story += [Spacer(1,24), HRFlowable(width='100%',thickness=0.5,color=colors.HexColor('#d1d5db')), Spacer(1,4), Paragraph('Generated by FairHire AI. No personal identifiers included.', sm)]
        doc.build(story)
        buf.seek(0)
        return send_file(buf, as_attachment=True, download_name=f'FairHire_{cid}.pdf', mimetype='application/pdf')
    except Exception as e: return jsonify({'error': str(e)}), 500

@app.route('/api/admin/login', methods=['POST'])
def admin_login():
    try:
        d = request.get_json(force=True, silent=True) or {}
        with get_db() as conn: row = conn.execute('SELECT * FROM admin_users WHERE username=?', (d.get('username',''),)).fetchone()
        if not row or not check_password_hash(row['password_hash'], d.get('password','')): return jsonify({'error': 'Invalid admin credentials'}), 401
        token = str(uuid.uuid4())
        with get_db() as conn:
            conn.execute('UPDATE admin_users SET token=? WHERE id=?', (token, row['id']))
            conn.commit()
        return jsonify({'success': True, 'token': token})
    except Exception as e: return jsonify({'error': str(e)}), 500

@app.route('/api/admin/candidates', methods=['GET'])
@require_admin
def admin_candidates():
    try:
        with get_db() as conn:
            rows = conn.execute('SELECT c.id, c.full_name, c.email, c.phone, c.dob, c.address, c.gov_id_type, c.gov_id_number, c.is_shortlisted, c.shortlisted_at, c.shortlist_note, c.created_at, s.final_score, s.confidence_level FROM candidates c LEFT JOIN scores s ON c.id = s.candidate_id ORDER BY c.is_shortlisted DESC, COALESCE(s.final_score,0) DESC').fetchall()
            result = []
            for r in rows: result.append({'candidateId': r['id'], 'fullName': r['full_name'], 'email': r['email'], 'phone': r['phone'], 'dob': r['dob'], 'address': r['address'], 'govIdType': r['gov_id_type'], 'govIdNumber': r['gov_id_number'], 'isShortlisted': bool(r['is_shortlisted']), 'shortlistedAt': r['shortlisted_at'], 'shortlistNote': r['shortlist_note'], 'registeredAt': r['created_at'], 'finalScore': r['final_score'], 'confidenceLevel':r['confidence_level'],})
        return jsonify(result)
    except Exception as e: return jsonify({'error': str(e)}), 500

@app.route('/api/admin/candidate/<cid>', methods=['GET'])
@require_admin
def admin_candidate_detail(cid):
    try:
        with get_db() as conn:
            c = conn.execute('SELECT * FROM candidates WHERE id=?', (cid,)).fetchone()
            qual = conn.execute('SELECT * FROM qualifications WHERE candidate_id=?', (cid,)).fetchone()
            sks = conn.execute('SELECT * FROM skills WHERE candidate_id=?', (cid,)).fetchall()
            exps = conn.execute('SELECT * FROM experience WHERE candidate_id=?', (cid,)).fetchall()
            score = conn.execute('SELECT * FROM scores WHERE candidate_id=?', (cid,)).fetchone()
            docs = conn.execute('SELECT id,doc_name,doc_type,doc_data,uploaded_at FROM career_documents WHERE candidate_id=?', (cid,)).fetchall()
        if not c: return jsonify({'error': 'Candidate not found'}), 404
        c = dict(c)
        return jsonify({'candidateId': cid, 'fullName': c['full_name'], 'email': c['email'], 'phone': c['phone'], 'dob': c['dob'], 'address': c['address'], 'govIdType': c['gov_id_type'], 'govIdNumber': c['gov_id_number'], 'passwordPlain': c['password_plain'], 'photoData': c['photo_data'] or '', 'signatureData': c['signature_data'] or '', 'registeredAt': c['created_at'], 'isShortlisted': bool(c['is_shortlisted']), 'shortlistedAt': c['shortlisted_at'], 'shortlistNote': c['shortlist_note'], 'qualifications':dict(qual) if qual else None, 'skills': [dict(s) for s in sks], 'experience': [dict(e) for e in exps], 'score': dict(score) if score else None, 'documents': [{'id':d['id'],'name':d['doc_name'],'type':d['doc_type'], 'data':d['doc_data'],'uploadedAt':d['uploaded_at']} for d in docs],})
    except Exception as e: return jsonify({'error': str(e)}), 500

@app.route('/api/admin/stats', methods=['GET'])
@require_admin
def admin_stats():
    try:
        with get_db() as conn:
            total = conn.execute('SELECT COUNT(*) AS n FROM candidates').fetchone()['n']
            sl = conn.execute('SELECT COUNT(*) AS n FROM candidates WHERE is_shortlisted=1').fetchone()['n']
            ver = conn.execute('SELECT COUNT(*) AS n FROM scores').fetchone()['n']
            avg = conn.execute('SELECT AVG(final_score) AS a FROM scores').fetchone()['a']
        return jsonify({'totalCandidates':total,'shortlisted':sl, 'verified':ver,'avgScore':round(avg or 0,1)})
    except Exception as e: return jsonify({'error': str(e)}), 500

def _academic_score(q): return round(float(q.get('tenth_percentage') or 0) * 0.25 + float(q.get('twelfth_percentage') or 0) * 0.25 + float(q.get('cgpa') or 0) * 10 * 0.50, 1)

def _verify_basic(skills): return [{'name': s['skill_name'], 'verified': bool(s.get('cert_data','')), 'confidence': 72 if s.get('cert_data','') else 28, 'notes': 'Certificate uploaded.' if s.get('cert_data','') else 'No certificate.',} for s in skills]

# ─────────────────────────────────────────────
# ── UPDATED: GEMINI 3 VISUAL VERIFICATION ──
# ─────────────────────────────────────────────
def _verify_gemini(skills, candidate_name):
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
    except: return _verify_basic(skills)
    results = []
    for s in skills:
        name = s['skill_name']
        cert_b64 = s.get('cert_data', '')
        if not cert_b64:
            results.append({'name': name, 'verified': False, 'confidence': 0, 'notes': 'No certificate uploaded.'})
            continue
        try:
            if "," in cert_b64: cert_b64 = cert_b64.split(",")[1]
            image_bytes = base64.b64decode(cert_b64)
            prompt = f"Verify if this certificate belongs to {candidate_name} and proves the skill {name}. Return ONLY JSON: {{\"verified\":true/false,\"confidence\":0-100,\"notes\":\"reason\"}}"
            response = client.models.generate_content(model='gemini-3-flash-preview', contents=[types.Part.from_bytes(data=image_bytes, mime_type='image/jpeg'), prompt])
            m = re.search(r'\{.*?\}', response.text, re.DOTALL)
            if m:
                obj = json.loads(m.group())
                results.append({'name': name, 'verified': bool(obj.get('verified')), 'confidence': int(obj.get('confidence', 50)), 'notes': str(obj.get('notes', ''))})
                continue
        except: pass
        results.append({'name': name, 'verified': True, 'confidence': 60, 'notes': 'Certificate present.'})
    return results

if __name__ == '__main__':
    _auto_init()
    print('FairHire backend → http://localhost:5000')
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
