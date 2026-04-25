<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>FairHire — AI-Powered Bias-Free Hiring</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@400;600;700;800;900&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react/18.2.0/umd/react.development.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.2.0/umd/react-dom.development.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/7.23.2/babel.min.js"></script>
<style>
:root{
  --bg:#020408;--surf:#0d111e;--card:rgba(255,255,255,.04);--glass:rgba(255,255,255,.06);
  --border:rgba(255,255,255,.07);--border2:rgba(255,255,255,.13);
  --cyan:#00d4ff;--teal:#00b4d8;--indigo:#6366f1;--violet:#8b5cf6;--pink:#ec4899;
  --amber:#f59e0b;--green:#10b981;--red:#f43f5e;--orange:#f97316;
  --text:#f0f4ff;--muted:#5a6a8a;--sub:#2a3450;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:'Outfit',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;overflow-x:hidden;}
::selection{background:rgba(0,212,255,.18);}
::-webkit-scrollbar{width:5px;}
::-webkit-scrollbar-thumb{background:var(--border2);border-radius:3px;}

/* Aurora */
#aurora{position:fixed;inset:0;z-index:0;pointer-events:none;}
.abl{position:absolute;border-radius:50%;filter:blur(90px);animation:adr 22s ease-in-out infinite alternate;}
@keyframes adr{0%{transform:translate(0,0) scale(1);}50%{transform:translate(30px,-50px) scale(1.08);}100%{transform:translate(-20px,40px) scale(.93);}}
#ptcl{position:fixed;inset:0;z-index:1;pointer-events:none;}
#root{position:relative;z-index:2;}

/* NAV */
.nav{position:sticky;top:0;z-index:200;height:64px;display:flex;align-items:center;justify-content:space-between;padding:0 28px;background:rgba(2,4,8,.8);backdrop-filter:blur(24px);border-bottom:1px solid var(--border);}
.logo{font-family:'Unbounded',sans-serif;font-size:17px;font-weight:900;background:linear-gradient(135deg,var(--cyan),var(--indigo));-webkit-background-clip:text;-webkit-text-fill-color:transparent;cursor:pointer;letter-spacing:-.025em;}
.logo em{background:linear-gradient(135deg,var(--violet),var(--pink));-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-style:normal;}
.navr{display:flex;align-items:center;gap:7px;flex-wrap:wrap;}

/* BUTTONS */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:7px;border:none;cursor:pointer;font-family:'Outfit',sans-serif;font-weight:500;transition:all .2s;white-space:nowrap;}
.btn-cyan{background:linear-gradient(135deg,var(--cyan),var(--teal));color:#000;font-weight:700;padding:9px 20px;border-radius:50px;font-size:13px;box-shadow:0 4px 20px rgba(0,212,255,.25);}
.btn-cyan:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(0,212,255,.4);}
.btn-indigo{background:linear-gradient(135deg,var(--indigo),var(--violet));color:#fff;font-weight:600;padding:10px 24px;border-radius:50px;font-size:14px;box-shadow:0 4px 22px rgba(99,102,241,.28);}
.btn-indigo:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(99,102,241,.45);}
.btn-orange{background:linear-gradient(135deg,var(--orange),var(--amber));color:#000;font-weight:700;padding:10px 24px;border-radius:50px;font-size:14px;box-shadow:0 4px 20px rgba(249,115,22,.28);}
.btn-orange:hover{transform:translateY(-2px);}
.btn-green{background:linear-gradient(135deg,var(--green),#059669);color:#fff;font-weight:700;padding:8px 18px;border-radius:50px;font-size:13px;box-shadow:0 4px 18px rgba(16,185,129,.3);}
.btn-green:hover{transform:translateY(-2px);}
.btn-glass{background:var(--card);border:1px solid var(--border);color:var(--muted);padding:9px 18px;border-radius:50px;font-size:13px;backdrop-filter:blur(8px);}
.btn-glass:hover{border-color:var(--border2);color:var(--text);}
.btn-outline{background:transparent;border:1px solid var(--border2);color:var(--muted);padding:8px 18px;border-radius:50px;font-size:13px;}
.btn-outline:hover{border-color:var(--cyan);color:var(--cyan);}
.btn-danger{background:rgba(244,63,94,.1);border:1px solid rgba(244,63,94,.22);color:var(--red);padding:5px 12px;border-radius:8px;font-size:12px;}
.btn-danger:hover{background:rgba(244,63,94,.2);}
.btn-lg{padding:13px 32px;font-size:15px;}
.btn-sm{padding:7px 16px;font-size:12.5px;}
.btn-xs{padding:5px 12px;font-size:11.5px;border-radius:8px;}
.btn:disabled{opacity:.4;cursor:not-allowed !important;transform:none !important;box-shadow:none !important;}
.btn:active:not(:disabled){transform:scale(.98) !important;}

/* CARD */
.card{background:var(--card);border:1px solid var(--border);border-radius:16px;backdrop-filter:blur(20px);}
.card-cyan{border-color:rgba(0,212,255,.14);box-shadow:0 0 40px rgba(0,212,255,.08);}
.card-orange{border-color:rgba(249,115,22,.2);box-shadow:0 0 40px rgba(249,115,22,.07);}

/* INPUTS */
.field{margin-bottom:14px;}
.field label{display:block;margin-bottom:6px;font-size:11px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);}
.inp{width:100%;background:rgba(255,255,255,.05);border:1px solid var(--border);border-radius:10px;padding:11px 14px;color:var(--text);font-family:'Outfit',sans-serif;font-size:14px;outline:none;transition:all .2s;}
.inp:focus{border-color:var(--cyan);box-shadow:0 0 0 3px rgba(0,212,255,.1);background:rgba(0,212,255,.03);}
.inp:hover:not(:focus){border-color:var(--border2);}
.inp::placeholder{color:var(--sub);}
select.inp option{background:#0d111e;}
.inp-wrap{position:relative;}
.inp-wrap .ic{position:absolute;left:13px;top:50%;transform:translateY(-50%);font-size:14px;pointer-events:none;}
.inp-wrap .inp{padding-left:40px;}
.pw-wrap{position:relative;}
.pw-wrap .inp{padding-right:44px;}
.pw-eye{position:absolute;right:13px;top:50%;transform:translateY(-50%);cursor:pointer;font-size:16px;color:var(--muted);transition:color .2s;background:none;border:none;padding:0;}
.pw-eye:hover{color:var(--cyan);}

/* UPLOAD ZONE */
.uzone{border:2px dashed var(--border);border-radius:12px;padding:18px;text-align:center;cursor:pointer;transition:all .25s;position:relative;overflow:hidden;}
.uzone:hover{border-color:var(--cyan);background:rgba(0,212,255,.03);}
.uzone.filled{border-color:rgba(16,185,129,.45);background:rgba(16,185,129,.04);border-style:solid;}
.uzone input[type=file]{position:absolute;inset:0;opacity:0;cursor:pointer;z-index:2;}
.uzone-icon{font-size:26px;margin-bottom:6px;}
.uzone-text{font-size:12.5px;color:var(--muted);}
.uzone-text strong{color:var(--cyan);}
.uzone-preview{max-width:100%;max-height:120px;border-radius:8px;margin-top:8px;object-fit:cover;}

/* BADGES */
.badge{display:inline-flex;align-items:center;gap:4px;padding:3px 10px;border-radius:20px;font-size:11px;font-weight:600;letter-spacing:.03em;}
.b-green{background:rgba(16,185,129,.1);color:var(--green);border:1px solid rgba(16,185,129,.2);}
.b-amber{background:rgba(245,158,11,.1);color:var(--amber);border:1px solid rgba(245,158,11,.2);}
.b-red{background:rgba(244,63,94,.1);color:var(--red);border:1px solid rgba(244,63,94,.2);}
.b-cyan{background:rgba(0,212,255,.09);color:var(--cyan);border:1px solid rgba(0,212,255,.18);}
.b-indigo{background:rgba(99,102,241,.1);color:#a5b4fc;border:1px solid rgba(99,102,241,.2);}
.b-orange{background:rgba(249,115,22,.1);color:var(--orange);border:1px solid rgba(249,115,22,.2);}
.b-violet{background:rgba(139,92,246,.1);color:#c4b5fd;border:1px solid rgba(139,92,246,.2);}

/* PROGRESS */
.pbar{height:4px;background:var(--border);border-radius:2px;overflow:hidden;}
.pfill{height:100%;border-radius:2px;transition:width .5s cubic-bezier(.4,0,.2,1);}

/* WIZARD */
.wizard{display:flex;align-items:flex-start;margin-bottom:32px;}
.wcon{flex:1;height:2px;background:var(--border);margin-top:19px;position:relative;overflow:hidden;}
.wcon-fill{position:absolute;left:0;top:0;height:100%;background:linear-gradient(90deg,var(--cyan),var(--indigo));transition:width .6s ease;}
.wstep{display:flex;flex-direction:column;align-items:center;gap:6px;flex-shrink:0;}
.wdot{width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;font-family:'Unbounded',sans-serif;transition:all .4s;border:2px solid var(--border);}
.wdot.done{background:rgba(16,185,129,.15);border-color:var(--green);color:var(--green);box-shadow:0 0 18px rgba(16,185,129,.28);}
.wdot.active{background:rgba(0,212,255,.1);border-color:var(--cyan);color:var(--cyan);box-shadow:0 0 22px rgba(0,212,255,.32);animation:wp 2s ease-in-out infinite;}
.wdot.idle{background:transparent;border-color:var(--sub);color:var(--sub);}
@keyframes wp{0%,100%{box-shadow:0 0 22px rgba(0,212,255,.28);}50%{box-shadow:0 0 34px rgba(0,212,255,.5);}}
.wlbl{font-size:10.5px;color:var(--muted);white-space:nowrap;font-weight:500;}
.wlbl.active{color:var(--cyan);}
.wlbl.done{color:var(--green);}

/* SECTION LABELS */
.slbl{font-size:11.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;padding:5px 12px;border-radius:8px;display:inline-flex;align-items:center;gap:7px;margin-bottom:14px;}
.s-cyan{color:var(--cyan);background:rgba(0,212,255,.07);border:1px solid rgba(0,212,255,.14);}
.s-violet{color:#c4b5fd;background:rgba(99,102,241,.07);border:1px solid rgba(99,102,241,.16);}
.s-amber{color:var(--amber);background:rgba(245,158,11,.07);border:1px solid rgba(245,158,11,.15);}
.s-green{color:var(--green);background:rgba(16,185,129,.07);border:1px solid rgba(16,185,129,.15);}
.s-red{color:var(--red);background:rgba(244,63,94,.07);border:1px solid rgba(244,63,94,.14);}
.s-orange{color:var(--orange);background:rgba(249,115,22,.07);border:1px solid rgba(249,115,22,.15);}

/* TABLE */
.tbl{width:100%;border-collapse:collapse;font-size:13px;}
.tbl th{padding:10px 14px;text-align:left;font-size:10.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);border-bottom:1px solid var(--border);background:rgba(255,255,255,.02);}
.tbl td{padding:12px 14px;border-bottom:1px solid rgba(255,255,255,.03);vertical-align:middle;}
.tbl tr:last-child td{border-bottom:none;}
.tbl tbody tr{cursor:pointer;transition:background .15s;}
.tbl tbody tr:hover td{background:rgba(0,212,255,.04);}
.tbl tbody tr.sel td{background:rgba(0,212,255,.07);}
.tbl tbody tr.shortlisted-row td{background:rgba(16,185,129,.04);}

/* TOAST */
.toast{position:fixed;bottom:24px;right:24px;z-index:9999;padding:12px 20px;border-radius:12px;font-size:13.5px;font-weight:500;display:flex;align-items:center;gap:10px;backdrop-filter:blur(20px);animation:tUp .3s cubic-bezier(.175,.885,.32,1.275);max-width:370px;}
.t-ok{background:rgba(16,185,129,.12);border:1px solid rgba(16,185,129,.28);color:var(--green);}
.t-err{background:rgba(244,63,94,.12);border:1px solid rgba(244,63,94,.28);color:var(--red);}
@keyframes tUp{from{transform:translateY(18px) scale(.9);opacity:0;}to{transform:translateY(0) scale(1);opacity:1;}}

/* SPINNER */
.sp{width:16px;height:16px;border:2px solid rgba(255,255,255,.15);border-top-color:currentColor;border-radius:50%;animation:spin .6s linear infinite;flex-shrink:0;}
@keyframes spin{to{transform:rotate(360deg);}}

/* ANIMATIONS */
@keyframes fu{from{opacity:0;transform:translateY(16px);}to{opacity:1;transform:translateY(0);}}
.fu{animation:fu .5s ease both;}
.d1{animation-delay:.07s;}.d2{animation-delay:.14s;}.d3{animation-delay:.21s;}.d4{animation-delay:.28s;}.d5{animation-delay:.35s;}
@keyframes stin{from{opacity:0;transform:translateX(22px);}to{opacity:1;transform:translateX(0);}}
.stin{animation:stin .32s cubic-bezier(.4,0,.2,1) both;}
@keyframes slr{from{transform:translateX(34px);opacity:0;}to{transform:translateX(0);opacity:1;}}
.slr{animation:slr .3s cubic-bezier(.4,0,.2,1) both;}

/* LAYOUT */
.page{padding:40px 24px;min-height:calc(100vh - 64px);}
.ctr{max-width:1160px;margin:0 auto;}
.nrw{max-width:540px;margin:0 auto;}
.nrw2{max-width:680px;margin:0 auto;}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;}
.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;}
@media(max-width:680px){.g2,.g3,.g4{grid-template-columns:1fr;}}
.row{display:flex;align-items:center;}
.jb{justify-content:space-between;}
.wrap{flex-wrap:wrap;}
.g6{gap:6px;}.g8{gap:8px;}.g12{gap:12px;}.g16{gap:16px;}
.mt4{margin-top:4px;}.mt8{margin-top:8px;}.mt12{margin-top:12px;}.mt16{margin-top:16px;}.mt24{margin-top:24px;}
.mb8{margin-bottom:8px;}.mb12{margin-bottom:12px;}.mb16{margin-bottom:16px;}.mb24{margin-bottom:24px;}
.hdiv{height:1px;background:linear-gradient(90deg,transparent,var(--border2),transparent);margin:18px 0;}

/* HERO */
.htag{display:inline-flex;align-items:center;gap:8px;padding:5px 14px;border-radius:20px;font-size:11.5px;font-weight:700;background:rgba(0,212,255,.07);border:1px solid rgba(0,212,255,.18);color:var(--cyan);letter-spacing:.06em;margin-bottom:24px;}
.htdot{width:7px;height:7px;border-radius:50%;background:var(--cyan);animation:pulse 1.8s ease-in-out infinite;}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1);}50%{opacity:.4;transform:scale(.7);}}
.h1{font-family:'Unbounded',sans-serif;font-size:clamp(32px,5.5vw,70px);font-weight:900;line-height:1.03;letter-spacing:-.035em;margin-bottom:20px;}
.hg{background:linear-gradient(135deg,#fff 15%,var(--cyan) 50%,var(--indigo));-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.hsub{font-size:17px;color:var(--muted);line-height:1.75;max-width:540px;margin-bottom:32px;}
.grid-bg{position:absolute;inset:0;opacity:.025;background-image:linear-gradient(var(--border2) 1px,transparent 1px),linear-gradient(90deg,var(--border2) 1px,transparent 1px);background-size:40px 40px;pointer-events:none;}

/* STAT CARD */
.sc{padding:22px;position:relative;overflow:hidden;}
.sc-n{font-family:'Unbounded',sans-serif;font-size:28px;font-weight:900;line-height:1;}
.sc-l{font-size:11px;color:var(--muted);margin-top:5px;letter-spacing:.05em;text-transform:uppercase;}
.sc-line{height:3px;border-radius:2px;margin-top:12px;}

/* FEAT CARD */
.fc{padding:24px;position:relative;overflow:hidden;transition:border-color .3s;}
.fc:hover{border-color:rgba(0,212,255,.18);}
.fc-n{font-family:'Unbounded',sans-serif;font-size:10.5px;font-weight:800;letter-spacing:.1em;color:var(--sub);margin-bottom:12px;}
.fc-ico{font-size:32px;margin-bottom:10px;}
.fc-t{font-size:16px;font-weight:700;margin-bottom:8px;}
.fc-d{font-size:13px;color:var(--muted);line-height:1.75;}

/* SKILL/EXP BLOCKS */
.sk-block{padding:16px;background:rgba(0,212,255,.03);border-radius:12px;border:1px solid rgba(0,212,255,.1);margin-bottom:12px;}
.exp-block{padding:16px;background:rgba(245,158,11,.03);border-radius:12px;border:1px solid rgba(245,158,11,.1);margin-bottom:12px;}
.sk-chip{display:inline-flex;align-items:center;gap:6px;padding:6px 12px;border-radius:10px;font-size:12.5px;font-weight:500;}
.sk-v{background:rgba(16,185,129,.09);border:1px solid rgba(16,185,129,.2);color:var(--green);}
.sk-u{background:rgba(245,158,11,.07);border:1px solid rgba(245,158,11,.18);color:var(--amber);}

/* SCORE PANEL */
.spanel{padding:24px;position:sticky;top:80px;}
.fdisp{text-align:center;padding:16px;background:rgba(0,212,255,.05);border-radius:14px;border:1px solid rgba(0,212,255,.12);margin-bottom:16px;}
.fnum{font-family:'Unbounded',sans-serif;font-size:48px;font-weight:900;line-height:1;}
.gauge-wrap{display:flex;flex-direction:column;align-items:center;gap:5px;}
.gauge-lbl{font-size:10px;text-transform:uppercase;letter-spacing:.07em;color:var(--muted);font-weight:600;}

/* COMPLETE */
.cring{width:100px;height:100px;border-radius:50%;background:rgba(16,185,129,.1);border:3px solid var(--green);display:flex;align-items:center;justify-content:center;font-size:46px;margin:0 auto 20px;box-shadow:0 0 50px rgba(16,185,129,.28);animation:cpop .6s cubic-bezier(.175,.885,.32,1.275);}
@keyframes cpop{from{transform:scale(0) rotate(-20deg);opacity:0;}to{transform:scale(1) rotate(0);opacity:1;}}

/* NOTICES */
.notice{border-radius:10px;padding:10px 14px;font-size:13px;margin-bottom:16px;}
.n-amber{background:rgba(245,158,11,.06);border:1px solid rgba(245,158,11,.15);color:var(--amber);}
.n-cyan{background:rgba(0,212,255,.06);border:1px solid rgba(0,212,255,.14);color:var(--cyan);}
.n-red{background:rgba(244,63,94,.06);border:1px solid rgba(244,63,94,.14);color:var(--red);}
.n-green{background:rgba(16,185,129,.06);border:1px solid rgba(16,185,129,.14);color:var(--green);}
.n-orange{background:rgba(249,115,22,.07);border:1px solid rgba(249,115,22,.15);color:var(--orange);}

/* SHORTLIST INDICATOR */
.shortlist-dot{width:8px;height:8px;border-radius:50%;background:var(--green);display:inline-block;box-shadow:0 0 6px var(--green);}

/* ADMIN - contact card */
.contact-card{padding:18px;background:rgba(16,185,129,.05);border:1px solid rgba(16,185,129,.2);border-radius:12px;margin-bottom:12px;}
.contact-row{display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid rgba(255,255,255,.04);}
.contact-row:last-child{border:none;}
.contact-icon{font-size:16px;width:24px;flex-shrink:0;}
.contact-label{font-size:10.5px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin-bottom:2px;}
.contact-value{font-size:14px;font-weight:600;}

/* IMAGE PREVIEW */
.img-preview-wrap{display:flex;align-items:center;justify-content:center;padding:10px;background:rgba(255,255,255,.03);border-radius:10px;border:1px solid var(--border);}
.img-preview{max-width:100%;max-height:180px;border-radius:8px;object-fit:contain;}

/* DOC LIST */
.doc-item{display:flex;align-items:center;gap:10px;padding:10px 14px;background:rgba(255,255,255,.03);border-radius:8px;border:1px solid var(--border);margin-bottom:6px;}
.doc-item:hover{border-color:var(--border2);}

/* PASSWORD STRENGTH */
.pw-strength{height:3px;border-radius:2px;transition:all .3s;}

/* TABS */
.tabs{display:flex;gap:4px;background:rgba(255,255,255,.04);border:1px solid var(--border);border-radius:10px;padding:4px;margin-bottom:20px;}
.tab{flex:1;padding:8px 12px;border-radius:7px;border:none;cursor:pointer;font-family:'Outfit',sans-serif;font-size:13px;font-weight:600;transition:all .2s;background:transparent;color:var(--muted);}
.tab.active{background:var(--card);color:var(--text);box-shadow:0 2px 8px rgba(0,0,0,.3);}
.tab:hover:not(.active){color:var(--text);}

/* CTA */
.cta-wrap{padding:52px 40px;text-align:center;border-radius:22px;background:radial-gradient(ellipse at center,rgba(0,212,255,.08),transparent 70%);border:1px solid rgba(0,212,255,.12);position:relative;overflow:hidden;}

/* MISC */
.ub{font-family:'Unbounded',sans-serif;}
.tc{color:var(--cyan);}.tv{color:#c4b5fd;}.tg{color:var(--green);}.tr{color:var(--red);}.ta{color:var(--amber);}.tm{color:var(--muted);}.to{color:var(--orange);}
.fw6{font-weight:600;}.fw7{font-weight:700;}.fw8{font-weight:800;}.fw9{font-weight:900;}
.ecrd{padding:12px 14px;border-radius:10px;background:rgba(255,255,255,.03);border:1px solid var(--border);margin-bottom:8px;}
</style>
</head>
<body>
<div id="aurora">
  <div class="abl" style="width:650px;height:500px;left:-180px;top:-100px;background:radial-gradient(ellipse,rgba(0,180,216,.1),transparent 70%);animation-duration:22s;"></div>
  <div class="abl" style="width:580px;height:580px;right:-80px;top:200px;background:radial-gradient(ellipse,rgba(99,102,241,.09),transparent 70%);animation-duration:18s;animation-delay:-8s;"></div>
  <div class="abl" style="width:480px;height:420px;left:35%;bottom:-80px;background:radial-gradient(ellipse,rgba(139,92,246,.07),transparent 70%);animation-duration:25s;animation-delay:-14s;"></div>
</div>
<canvas id="ptcl"></canvas>
<div id="root"></div>

<script>
(function(){
  const c=document.getElementById('ptcl'),ctx=c.getContext('2d');
  let W,H,pts;const N=48;
  function resize(){W=c.width=window.innerWidth;H=c.height=window.innerHeight;}
  function mk(){pts=Array.from({length:N},()=>({x:Math.random()*W,y:Math.random()*H,vx:(Math.random()-.5)*.2,vy:(Math.random()-.5)*.2,r:Math.random()*1.3+.4,a:Math.random()*.4+.1}));}
  function draw(){
    ctx.clearRect(0,0,W,H);
    pts.forEach(p=>{p.x+=p.vx;p.y+=p.vy;if(p.x<0)p.x=W;if(p.x>W)p.x=0;if(p.y<0)p.y=H;if(p.y>H)p.y=0;ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fillStyle=`rgba(0,212,255,${p.a})`;ctx.fill();});
    for(let i=0;i<N;i++)for(let j=i+1;j<N;j++){const dx=pts[i].x-pts[j].x,dy=pts[i].y-pts[j].y,d=Math.sqrt(dx*dx+dy*dy);if(d<110){ctx.beginPath();ctx.moveTo(pts[i].x,pts[i].y);ctx.lineTo(pts[j].x,pts[j].y);ctx.strokeStyle=`rgba(99,102,241,${(1-d/110)*.1})`;ctx.lineWidth=.7;ctx.stroke();}}
    requestAnimationFrame(draw);
  }
  window.addEventListener('resize',()=>{resize();mk();});resize();mk();draw();
})();
</script>

<script type="text/babel">
const {useState,useEffect,useRef} = React;
const BASE = 'http://localhost:5000/api';

async function api(path,opts={}){
  const tk=localStorage.getItem('fh_token');
  const res=await fetch(BASE+path,{
    method:opts.method||'GET',
    headers:{'Content-Type':'application/json',...(tk?{Authorization:'Bearer '+tk}:{})},
    ...(opts.body?{body:opts.body}:{})
  });
  const d=await res.json().catch(()=>({}));
  if(!res.ok)throw new Error(d.error||'Request failed');
  return d;
}
function b64(f){return new Promise((res,rej)=>{const r=new FileReader();r.onload=()=>res(r.result);r.onerror=rej;r.readAsDataURL(f);});}

/* ── Toast ── */
function Toast({msg,type,onClose}){
  useEffect(()=>{const t=setTimeout(onClose,4200);return()=>clearTimeout(t);},[]);
  return<div className={`toast ${type==='success'?'t-ok':'t-err'}`}><span style={{fontSize:16}}>{type==='success'?'✓':'✕'}</span><span>{msg}</span></div>;
}

/* ── Nav ── */
function Nav({page,setPage,token,userType,onLogout}){
  return(
    <nav className="nav">
      <div className="logo" onClick={()=>setPage('landing')}>Fair<em>Hire</em></div>
      <div className="navr">
        {!token&&<>
          <button className="btn btn-glass btn-sm" onClick={()=>setPage('candidate-login')}>Candidate Login</button>
          <button className="btn btn-glass btn-sm" onClick={()=>setPage('hr-login')}>HR Portal</button>
          <button className="btn btn-orange btn-sm" onClick={()=>setPage('admin-login')}>Admin ⚙️</button>
          <button className="btn btn-cyan btn-sm" onClick={()=>setPage('candidate-register')}>Apply Now →</button>
        </>}
        {token&&userType==='candidate'&&<>
          <button className="btn btn-glass btn-sm" onClick={()=>setPage('candidate-dashboard')}>My Dashboard</button>
          <button className="btn btn-outline btn-sm" onClick={onLogout}>Logout</button>
        </>}
        {token&&userType==='hr'&&<>
          <button className="btn btn-glass btn-sm" onClick={()=>setPage('hr-dashboard')}>HR Dashboard</button>
          <button className="btn btn-outline btn-sm" onClick={onLogout}>Logout</button>
        </>}
        {token&&userType==='admin'&&<>
          <button className="btn btn-orange btn-sm" onClick={()=>setPage('admin-dashboard')}>Admin Panel ⚙️</button>
          <button className="btn btn-outline btn-sm" onClick={onLogout}>Logout</button>
        </>}
      </div>
    </nav>
  );
}

/* ── Landing ── */
function Landing({setPage}){
  return(
    <div className="page">
      <div className="ctr">
        <div style={{paddingTop:48,paddingBottom:64,maxWidth:800}}>
          <div className="htag fu"><span className="htdot"></span>AI-POWERED · BIAS-FREE · VERIFIED</div>
          <h1 className="h1 fu d1"><span className="hg">Hire the best,</span><br/><span style={{color:'rgba(255,255,255,.14)'}}>not the loudest.</span></h1>
          <p className="hsub fu d2">FairHire uses <strong style={{color:'var(--text)'}}>Selective Anonymity</strong> and Google Gemini AI to evaluate candidates on pure merit — hiding identity from HR while giving Admin full oversight.</p>
          <div className="row g8 wrap fu d3">
            <button className="btn btn-cyan btn-lg" onClick={()=>setPage('candidate-register')}>Create Free Profile →</button>
            <button className="btn btn-glass btn-lg" onClick={()=>setPage('hr-login')}>HR Portal</button>
            <button className="btn btn-orange btn-sm" style={{borderRadius:50,padding:'10px 18px'}} onClick={()=>setPage('admin-login')}>Admin ⚙️</button>
          </div>
        </div>
        <div className="g4 mb24 fu d2">
          {[
            {n:'100%',l:'Identity hidden from HR',c:'var(--cyan)',li:'linear-gradient(90deg,var(--cyan),var(--indigo))'},
            {n:'AI',  l:'Gemini Skill Verification',c:'#c4b5fd',li:'linear-gradient(90deg,var(--violet),var(--pink))'},
            {n:'3',   l:'User Roles (Candidate/HR/Admin)',c:'var(--orange)',li:'var(--orange)'},
            {n:'PDF', l:'Bias-Free Reports',c:'var(--amber)',li:'var(--amber)'},
          ].map(s=>(
            <div key={s.l} className="card sc"><div className="grid-bg"/><div className="sc-n" style={{color:s.c}}>{s.n}</div><div className="sc-l">{s.l}</div><div className="sc-line" style={{background:s.li}}/></div>
          ))}
        </div>
        <div className="g3 mb24">
          {[
            {n:'01',ico:'🔐',t:'Candidate',d:'Register securely. Upload photo, signature, career documents and skills. AI verifies your claims.'},
            {n:'02',ico:'🏢',t:'HR Evaluates',d:'HR sees only scores, CGPA and verified skills — no names, no schools, no bias possible. Shortlists top candidates.'},
            {n:'03',ico:'⚙️',t:'Admin Contacts',d:'Admin sees full profile of shortlisted candidates including contact details, photo, signature, all documents.'},
          ].map(c=>(
            <div key={c.n} className="card fc"><div className="fc-n">ROLE {c.n}</div><div className="fc-ico">{c.ico}</div><div className="fc-t">{c.t}</div><div className="fc-d">{c.d}</div></div>
          ))}
        </div>
        <div className="cta-wrap fu d3">
          <div style={{position:'relative',zIndex:1}}>
            <h2 className="ub" style={{fontSize:30,fontWeight:900,marginBottom:12}}>Ready to apply fairly?</h2>
            <p style={{color:'var(--muted)',fontSize:15,marginBottom:28,maxWidth:480,margin:'0 auto 28px'}}>Join thousands evaluated on merit, not prestige.</p>
            <div className="row g12" style={{justifyContent:'center',flexWrap:'wrap'}}>
              <button className="btn btn-cyan btn-lg" onClick={()=>setPage('candidate-register')}>Create Profile — Free →</button>
              <button className="btn btn-glass btn-lg" onClick={()=>setPage('candidate-login')}>Continue Application</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

/* ── WIZARD ── */
const WSTEPS=[{l:'Identity'},{l:'Qualifications'},{l:'Documents'},{l:'Skills & CV'},{l:'Complete'}];
function WizardBar({current}){
  return(
    <div className="wizard">
      {WSTEPS.map((s,i)=>(
        <React.Fragment key={i}>
          <div className="wstep">
            <div className={`wdot ${i<current?'done':i===current?'active':'idle'}`}>{i<current?'✓':i+1}</div>
            <span className={`wlbl ${i<current?'done':i===current?'active':''}`}>{s.l}</span>
          </div>
          {i<WSTEPS.length-1&&<div className="wcon"><div className="wcon-fill" style={{width:i<current?'100%':'0%'}}/></div>}
        </React.Fragment>
      ))}
    </div>
  );
}

/* ── REGISTER ── */
const BOARDS=['CBSE','ICSE','Maharashtra Board','UP Board','Tamil Nadu Board','Karnataka Board','Rajasthan Board','Kerala Board','Gujarat Board','Other'];
const DEGREES=['B.Tech / B.E.','B.Sc','BCA','B.Com','BBA','B.A.','MCA','M.Tech','MBA','M.Sc','Ph.D','Diploma','Other'];
const GOVIDS=['Aadhar Card','PAN Card',"Driver's License",'Passport','Voter ID'];

function PasswordInput({value,onChange,placeholder='••••••••',label}){
  const [show,setShow]=useState(false);
  const strength=value.length>=8?'strong':value.length>=6?'medium':value.length>0?'weak':'';
  const sc={strong:'var(--green)',medium:'var(--amber)',weak:'var(--red)','':''};
  return(
    <div className="field">
      {label&&<label>{label}</label>}
      <div className="pw-wrap">
        <input className="inp" type={show?'text':'password'} placeholder={placeholder} value={value} onChange={onChange} style={{paddingRight:44}}/>
        <button type="button" className="pw-eye" onClick={()=>setShow(p=>!p)} title={show?'Hide password':'Show password'}>
          {show?'🙈':'👁️'}
        </button>
      </div>
      {value&&(
        <div style={{marginTop:6}}>
          <div className="pbar"><div className="pfill pw-strength" style={{width:value.length>=8?'100%':value.length>=6?'65%':'32%',background:sc[strength]}}/></div>
          <span style={{fontSize:10.5,color:sc[strength],marginTop:2,display:'block',fontWeight:600,textTransform:'uppercase',letterSpacing:'.05em'}}>{strength}</span>
        </div>
      )}
    </div>
  );
}

function FileUpload({label,accept,value,onChange,preview,note,required=false}){
  const hasFile=!!value;
  return(
    <div className="field">
      {label&&<label>{label}{required&&<span style={{color:'var(--red)',marginLeft:4}}>*</span>}</label>}
      <label className={`uzone ${hasFile?'filled':''}`} style={{minHeight:80}}>
        <input type="file" accept={accept} onChange={e=>onChange(e.target.files[0])}/>
        <div className="uzone-icon">{hasFile?'✅':'📎'}</div>
        <div className="uzone-text">
          {hasFile
            ?<strong style={{color:'var(--green)'}}>{typeof value==='string'?'File uploaded ✓':value.name}</strong>
            :<><strong>Click to upload</strong>{note&&<><br/><span style={{fontSize:11.5}}>{note}</span></>}</>
          }
        </div>
        {preview&&hasFile&&typeof value!=='string'&&(
          <img src={URL.createObjectURL(value)} alt="preview" className="uzone-preview"/>
        )}
      </label>
    </div>
  );
}

function CandidateRegister({setPage,showToast,setAuth}){
  const [step,setStep]=useState(0);
  const [loading,setLoading]=useState(false);
  const [cid,setCid]=useState('');

  const [id,setId]=useState({fullName:'',email:'',phone:'',dob:'',address:'',password:'',confirm:'',govIdType:'Aadhar Card',govIdNumber:''});
  const [photo,setPhoto]=useState(null);
  const [sig,setSig]=useState(null);

  const [q,setQ]=useState({tenthPercentage:'',tenthBoard:'CBSE',twelfthPercentage:'',twelfthBoard:'CBSE',degree:'B.Tech / B.E.',branch:'',cgpa:'',collegeName:'',schoolName:''});

  const [docs,setDocs]=useState([{name:'Degree Certificate',file:null,data:''},{name:'Marksheet / Transcript',file:null,data:''},{name:'Internship Certificate',file:null,data:''}]);
  const [extraDocs,setExtraDocs]=useState([]);

  const [skills,setSkills]=useState([{name:'',certData:'',certName:''}]);
  const [exp,setExp]=useState([{role:'',company:'',durationMonths:'',description:''}]);
  const [cv,setCv]=useState(null);
  const [cvData,setCvData]=useState('');

  const upd=(s)=>(k,v)=>s(p=>({...p,[k]:v}));

  // STEP 0: Identity
  async function s0(){
    if(!id.fullName||!id.email||!id.password){showToast('Name, Email and Password are required','error');return;}
    if(!id.dob){showToast('Date of Birth is required','error');return;}
    if(id.password.length<6){showToast('Password must be at least 6 characters','error');return;}
    if(id.password!==id.confirm){showToast('Passwords do not match','error');return;}
    if(!photo){showToast('Please upload your photo (JPG)','error');return;}
    if(!sig){showToast('Please upload your signature (JPG)','error');return;}
    setLoading(true);
    try{
      const photoData=await b64(photo);
      const sigData=await b64(sig);
      await api('/candidate/register',{method:'POST',body:JSON.stringify({
        fullName:id.fullName,email:id.email,phone:id.phone,dob:id.dob,
        address:id.address,password:id.password,
        govIdType:id.govIdType,govIdNumber:id.govIdNumber,
        photoData,signatureData:sigData
      })});
      const lg=await api('/candidate/login',{method:'POST',body:JSON.stringify({email:id.email,password:id.password})});
      localStorage.setItem('fh_token',lg.token);
      localStorage.setItem('fh_type','candidate');
      localStorage.setItem('fh_cid',lg.candidateId);
      setCid(lg.candidateId);
      setAuth(lg.token,'candidate');
      setStep(1);
      showToast(`Welcome ${id.fullName.split(' ')[0]}! Proceed to qualifications.`,'success');
    }catch(e){showToast(e.message,'error');}
    setLoading(false);
  }

  // STEP 1: Qualifications
  async function s1(){
    if(!q.tenthPercentage||!q.twelfthPercentage||!q.cgpa){showToast('Please fill all percentage and CGPA fields','error');return;}
    setLoading(true);
    try{
      await api('/candidate/qualifications',{method:'POST',body:JSON.stringify(q)});
      setStep(2);
      showToast('Qualifications saved!','success');
    }catch(e){showToast(e.message,'error');}
    setLoading(false);
  }

  // STEP 2: Documents
  async function s2(){
    const allDocs=[...docs,...extraDocs].filter(d=>d.data||d.file);
    if(!allDocs.length){showToast('Please upload at least one career document','error');return;}
    setLoading(true);
    try{
      const uploadDocs=[];
      for(const d of allDocs){
        if(d.file&&!d.data){
          const data=await b64(d.file);
          uploadDocs.push({name:d.name,type:'pdf',data});
        } else if(d.data){
          uploadDocs.push({name:d.name,type:'pdf',data:d.data});
        }
      }
      await api('/candidate/documents',{method:'POST',body:JSON.stringify({documents:uploadDocs})});
      setStep(3);
      showToast('Documents uploaded!','success');
    }catch(e){showToast(e.message,'error');}
    setLoading(false);
  }

  // STEP 3: Skills
  async function s3(){
    const sk=skills.filter(s=>s.name.trim());
    if(!sk.length){showToast('Add at least one skill','error');return;}
    setLoading(true);
    try{
      await api('/candidate/skills',{method:'POST',body:JSON.stringify({
        skills:sk.map(s=>({name:s.name,certData:s.certData})),
        experience:exp.filter(e=>e.role.trim()),
        cvData
      })});
      await api('/candidate/verify',{method:'POST'});
      setStep(4);
      showToast('🎉 AI verification complete! Redirecting to dashboard…','success');
      setTimeout(()=>setPage('candidate-dashboard'),2500);
    }catch(e){showToast(e.message,'error');}
    setLoading(false);
  }

  async function handleCert(idx,file){
    if(!file)return;
    if(file.size>4*1024*1024){showToast('Max 4 MB per certificate','error');return;}
    const data=await b64(file);
    setSkills(p=>p.map((s,i)=>i===idx?{...s,certData:data,certName:file.name}:s));
  }
  async function handleCV(file){
    if(!file)return;
    if(file.size>10*1024*1024){showToast('CV max 10 MB','error');return;}
    setCvData(await b64(file));setCv(file);
    showToast('CV uploaded ✓','success');
  }
  async function handleDoc(idx,file){
    if(!file)return;
    if(file.size>10*1024*1024){showToast('Max 10 MB per document','error');return;}
    if(file.type!=='application/pdf'&&!file.name.toLowerCase().endsWith('.pdf')){showToast('Only PDF files allowed for career documents','error');return;}
    const data=await b64(file);
    setDocs(p=>p.map((d,i)=>i===idx?{...d,file,data}:d));
    showToast(`${file.name} uploaded ✓`,'success');
  }
  async function handleExtraDoc(idx,file){
    if(!file)return;
    if(file.type!=='application/pdf'&&!file.name.toLowerCase().endsWith('.pdf')){showToast('Only PDF files allowed','error');return;}
    const data=await b64(file);
    setExtraDocs(p=>p.map((d,i)=>i===idx?{...d,file,data}:d));
  }

  const validatePhoto=(file)=>{
    if(!file)return;
    if(!file.type.includes('jpeg')&&!file.type.includes('jpg')&&!file.name.toLowerCase().endsWith('.jpg')&&!file.name.toLowerCase().endsWith('.jpeg')){showToast('Photo must be JPG/JPEG format only','error');return;}
    setPhoto(file);
  };
  const validateSig=(file)=>{
    if(!file)return;
    if(!file.type.includes('jpeg')&&!file.type.includes('jpg')&&!file.name.toLowerCase().endsWith('.jpg')&&!file.name.toLowerCase().endsWith('.jpeg')){showToast('Signature must be JPG/JPEG format only','error');return;}
    setSig(file);
  };

  return(
    <div className="page">
      <div className="nrw2">
        <div className="mb24 fu">
          <h1 className="ub" style={{fontSize:24,fontWeight:900,marginBottom:5}}>Create Your Profile</h1>
          <p className="tm" style={{fontSize:13.5}}>Identity kept <strong className="tc">strictly private</strong> from HR. Admin has oversight of all data.</p>
        </div>
        <WizardBar current={step}/>

        {/* ── STEP 0: Identity ── */}
        {step===0&&(
          <div className="card stin" style={{padding:28}}>
            <div className="row jb mb12">
              <span className="slbl s-cyan">🔐 Identity & Biometrics</span>
              <span className="badge b-red">🔒 Hidden from HR</span>
            </div>
            <div className="notice n-red mb16">
              <strong>Privacy:</strong> This data is never shown to HR. Only Admin can access it for verification.
            </div>
            <div className="g2">
              <div className="field">
                <label>Full Name *</label>
                <div className="inp-wrap"><span className="ic">👤</span><input className="inp" placeholder="Priya Sharma" value={id.fullName} onChange={e=>upd(setId)('fullName',e.target.value)}/></div>
              </div>
              <div className="field">
                <label>Date of Birth *</label>
                <div className="inp-wrap"><span className="ic">🎂</span>
                  <input className="inp" type="date" value={id.dob} onChange={e=>upd(setId)('dob',e.target.value)}
                    max={new Date(Date.now()-14*365*24*60*60*1000).toISOString().split('T')[0]}/>
                </div>
              </div>
              <div className="field">
                <label>Email Address *</label>
                <div className="inp-wrap"><span className="ic">✉️</span><input className="inp" type="email" placeholder="you@example.com" value={id.email} onChange={e=>upd(setId)('email',e.target.value)}/></div>
              </div>
              <div className="field">
                <label>Phone Number</label>
                <div className="inp-wrap"><span className="ic">📱</span><input className="inp" placeholder="+91 98765 43210" value={id.phone} onChange={e=>upd(setId)('phone',e.target.value)}/></div>
              </div>
              <div className="field" style={{gridColumn:'1/-1'}}>
                <label>Residential Address</label>
                <div className="inp-wrap"><span className="ic">🏠</span><input className="inp" placeholder="Mumbai, Maharashtra, India" value={id.address} onChange={e=>upd(setId)('address',e.target.value)}/></div>
              </div>
              <div className="field">
                <label>Government ID Type</label>
                <select className="inp" value={id.govIdType} onChange={e=>upd(setId)('govIdType',e.target.value)}>{GOVIDS.map(g=><option key={g}>{g}</option>)}</select>
              </div>
              <div className="field">
                <label>ID Number</label>
                <input className="inp" placeholder="XXXX-XXXX-XXXX" value={id.govIdNumber} onChange={e=>upd(setId)('govIdNumber',e.target.value)}/>
              </div>
            </div>
            <PasswordInput label="Password * (min 6 chars)" value={id.password} onChange={e=>upd(setId)('password',e.target.value)}/>
            <div className="field">
              <label>Confirm Password *</label>
              <div className="pw-wrap">
                <input className="inp" type="password" placeholder="••••••••" value={id.confirm} onChange={e=>upd(setId)('confirm',e.target.value)} style={{paddingRight:44}}/>
              </div>
              {id.confirm&&<span style={{fontSize:11,marginTop:4,display:'block',color:id.confirm===id.password?'var(--green)':'var(--red)',fontWeight:600}}>{id.confirm===id.password?'✓ Passwords match':'✕ Passwords do not match'}</span>}
            </div>
            <div className="hdiv"/>
            <div className="notice n-cyan mb12">
              📸 <strong>Photo & Signature:</strong> Only JPG/JPEG format accepted. These are stored securely for admin verification only.
            </div>
            <div className="g2">
              <div>
                <label style={{display:'block',marginBottom:6,fontSize:11,fontWeight:700,letterSpacing:'.07em',textTransform:'uppercase',color:'var(--muted)'}}>Candidate Photo * <span style={{color:'var(--amber)',fontWeight:500,textTransform:'none',fontSize:10}}>(JPG only)</span></label>
                <label className={`uzone ${photo?'filled':''}`} style={{minHeight:90}}>
                  <input type="file" accept=".jpg,.jpeg,image/jpeg" onChange={e=>validatePhoto(e.target.files[0])}/>
                  <div className="uzone-icon">{photo?'✅':'🖼️'}</div>
                  <div className="uzone-text">
                    {photo?<><strong style={{color:'var(--green)'}}>{photo.name}</strong><br/><img src={URL.createObjectURL(photo)} alt="preview" style={{maxHeight:80,maxWidth:'100%',borderRadius:6,marginTop:6,objectFit:'cover'}}/></>:<><strong>Upload Photo</strong><br/><span style={{fontSize:11}}>JPG/JPEG only — max 5 MB</span></>}
                  </div>
                </label>
              </div>
              <div>
                <label style={{display:'block',marginBottom:6,fontSize:11,fontWeight:700,letterSpacing:'.07em',textTransform:'uppercase',color:'var(--muted)'}}>Signature * <span style={{color:'var(--amber)',fontWeight:500,textTransform:'none',fontSize:10}}>(JPG only)</span></label>
                <label className={`uzone ${sig?'filled':''}`} style={{minHeight:90}}>
                  <input type="file" accept=".jpg,.jpeg,image/jpeg" onChange={e=>validateSig(e.target.files[0])}/>
                  <div className="uzone-icon">{sig?'✅':'✍️'}</div>
                  <div className="uzone-text">
                    {sig?<><strong style={{color:'var(--green)'}}>{sig.name}</strong><br/><img src={URL.createObjectURL(sig)} alt="sig" style={{maxHeight:60,maxWidth:'100%',borderRadius:6,marginTop:6,objectFit:'contain'}}/></>:<><strong>Upload Signature</strong><br/><span style={{fontSize:11}}>JPG/JPEG only — max 3 MB</span></>}
                  </div>
                </label>
              </div>
            </div>
            <div className="hdiv"/>
            <div className="row jb wrap g12">
              <button className="btn btn-glass btn-sm" onClick={()=>setPage('landing')}>← Back</button>
              <button className="btn btn-cyan" onClick={s0} disabled={loading} style={{minWidth:200}}>
                {loading?<><span className="sp"/>Registering…</>:'Continue to Qualifications →'}
              </button>
            </div>
            <p style={{marginTop:14,textAlign:'center',fontSize:12.5,color:'var(--muted)'}}>
              Already registered? <span className="tc fw6" style={{cursor:'pointer'}} onClick={()=>setPage('candidate-login')}>Login here</span>
            </p>
          </div>
        )}

        {/* ── STEP 1: Qualifications ── */}
        {step===1&&(
          <div className="card stin" style={{padding:28}}>
            <div className="row jb mb12">
              <span className="slbl s-violet">🎓 Academic Qualifications</span>
              <span className="badge b-amber">Scores visible to HR · Names hidden</span>
            </div>
            <div className="notice n-amber">⚠️ School/college names are hidden from HR. Only percentages and CGPA are shared.</div>
            <div className="slbl s-cyan" style={{marginBottom:12}}>10th Standard</div>
            <div className="g2">
              <div className="field"><label>Percentage *</label><input className="inp" type="number" min="0" max="100" step="0.1" placeholder="85.5" value={q.tenthPercentage} onChange={e=>upd(setQ)('tenthPercentage',e.target.value)}/></div>
              <div className="field"><label>Board</label><select className="inp" value={q.tenthBoard} onChange={e=>upd(setQ)('tenthBoard',e.target.value)}>{BOARDS.map(b=><option key={b}>{b}</option>)}</select></div>
              <div className="field" style={{gridColumn:'1/-1'}}>
                <label>School Name <span className="tr" style={{fontSize:10,marginLeft:5}}>🔒 Private — hidden from HR</span></label>
                <input className="inp" placeholder="e.g. Delhi Public School (not shown to HR)" value={q.schoolName} onChange={e=>upd(setQ)('schoolName',e.target.value)}/>
              </div>
            </div>
            <div className="slbl s-cyan" style={{marginBottom:12,marginTop:4}}>12th Standard</div>
            <div className="g2">
              <div className="field"><label>Percentage *</label><input className="inp" type="number" min="0" max="100" step="0.1" placeholder="88.0" value={q.twelfthPercentage} onChange={e=>upd(setQ)('twelfthPercentage',e.target.value)}/></div>
              <div className="field"><label>Board</label><select className="inp" value={q.twelfthBoard} onChange={e=>upd(setQ)('twelfthBoard',e.target.value)}>{BOARDS.map(b=><option key={b}>{b}</option>)}</select></div>
            </div>
            <div className="slbl s-violet" style={{marginBottom:12,marginTop:4}}>Graduation</div>
            <div className="g2">
              <div className="field"><label>Degree *</label><select className="inp" value={q.degree} onChange={e=>upd(setQ)('degree',e.target.value)}>{DEGREES.map(d=><option key={d}>{d}</option>)}</select></div>
              <div className="field"><label>Branch / Major</label><input className="inp" placeholder="Computer Science Engineering" value={q.branch} onChange={e=>upd(setQ)('branch',e.target.value)}/></div>
              <div className="field"><label>CGPA (10-pt scale) *</label><input className="inp" type="number" min="0" max="10" step="0.01" placeholder="8.4" value={q.cgpa} onChange={e=>upd(setQ)('cgpa',e.target.value)}/></div>
              <div className="field"><label>College Name <span className="tr" style={{fontSize:10,marginLeft:5}}>🔒 Private</span></label><input className="inp" placeholder="e.g. IIT Bombay (hidden)" value={q.collegeName} onChange={e=>upd(setQ)('collegeName',e.target.value)}/></div>
            </div>
            <div className="hdiv"/>
            <div className="row jb wrap g12">
              <button className="btn btn-glass btn-sm" onClick={()=>setStep(0)}>← Back</button>
              <button className="btn btn-cyan" onClick={s1} disabled={loading} style={{minWidth:160}}>{loading?<><span className="sp"/>Saving…</>:'Continue to Documents →'}</button>
            </div>
          </div>
        )}

        {/* ── STEP 2: Career Documents ── */}
        {step===2&&(
          <div className="stin">
            <div className="card mb16" style={{padding:28}}>
              <div className="row jb mb12">
                <span className="slbl s-orange">📂 Career Documents</span>
                <span className="badge b-orange">PDF Only</span>
              </div>
              <div className="notice n-orange">
                📄 <strong>PDF format only</strong> for career documents. These are stored securely and only visible to Admin.
              </div>
              {docs.map((d,i)=>(
                <div key={i} style={{padding:'12px 14px',background:'rgba(249,115,22,.03)',borderRadius:10,border:'1px solid rgba(249,115,22,.1)',marginBottom:10}}>
                  <div style={{fontSize:12,fontWeight:700,color:'var(--orange)',marginBottom:8}}>{d.name}</div>
                  <label className={`uzone ${d.data?'filled':''}`} style={{padding:'12px',minHeight:60}}>
                    <input type="file" accept=".pdf,application/pdf" onChange={e=>handleDoc(i,e.target.files[0])}/>
                    <div className="uzone-text" style={{fontSize:12}}>
                      {d.data?<strong style={{color:'var(--green)'}}>✓ {d.file?.name||'Uploaded'}</strong>:<><strong>📎 Upload PDF</strong> — {d.name}</>}
                    </div>
                  </label>
                </div>
              ))}
              <div style={{marginTop:8}}>
                <div style={{fontSize:12,color:'var(--muted)',marginBottom:8}}>Additional Documents (optional):</div>
                {extraDocs.map((d,i)=>(
                  <div key={i} style={{display:'flex',gap:8,marginBottom:8,alignItems:'center'}}>
                    <input className="inp" placeholder="Document name" value={d.name} onChange={e=>setExtraDocs(p=>p.map((x,j)=>j===i?{...x,name:e.target.value}:x))} style={{flex:1,padding:'8px 12px'}}/>
                    <label className={`uzone ${d.data?'filled':''}`} style={{flex:2,padding:'8px 12px',minHeight:40,margin:0}}>
                      <input type="file" accept=".pdf,application/pdf" onChange={e=>handleExtraDoc(i,e.target.files[0])}/>
                      <div className="uzone-text" style={{fontSize:11.5}}>{d.data?<strong style={{color:'var(--green)'}}>✓ Uploaded</strong>:<strong>📎 PDF</strong>}</div>
                    </label>
                    <button className="btn btn-danger" onClick={()=>setExtraDocs(p=>p.filter((_,j)=>j!==i))}>✕</button>
                  </div>
                ))}
                <button className="btn btn-glass btn-sm" onClick={()=>setExtraDocs(p=>[...p,{name:'',file:null,data:''}])}>+ Add Document</button>
              </div>
            </div>
            <div className="row jb wrap g12">
              <button className="btn btn-glass btn-sm" onClick={()=>setStep(1)}>← Back</button>
              <button className="btn btn-cyan" onClick={s2} disabled={loading} style={{minWidth:160}}>{loading?<><span className="sp"/>Uploading…</>:'Continue to Skills →'}</button>
            </div>
          </div>
        )}

        {/* ── STEP 3: Skills + CV ── */}
        {step===3&&(
          <div className="stin">
            <div className="card mb16" style={{padding:24}}>
              <div className="row jb mb12"><span className="slbl s-green">📄 CV / Resume</span><span className="badge b-indigo">AI-Parsed</span></div>
              <p className="tm mb12" style={{fontSize:13}}>Upload your CV for AI cross-referencing. Higher confidence scores with CV.</p>
              <label className={`uzone ${cv?'filled':''}`} style={{minHeight:80}}>
                <input type="file" accept=".pdf,.doc,.docx,.txt" onChange={e=>handleCV(e.target.files[0])}/>
                <div className="uzone-icon">{cv?'✅':'📎'}</div>
                <div className="uzone-text">{cv?<><strong style={{color:'var(--green)'}}>{cv.name}</strong><br/><span style={{fontSize:11}}>{(cv.size/1024).toFixed(0)} KB</span></>:<><strong>Upload CV / Resume</strong><br/>PDF, DOC, DOCX — max 10 MB</>}</div>
              </label>
            </div>
            <div className="card mb16" style={{padding:24}}>
              <div className="row jb mb12"><span className="slbl s-cyan">⚡ Skills & Certificates</span><span className="badge b-cyan">Gemini Verified</span></div>
              {skills.map((sk,i)=>(
                <div key={i} className="sk-block">
                  <div className="row jb mb8">
                    <span style={{fontSize:11.5,fontWeight:700,letterSpacing:'.05em'}} className="tc">SKILL #{i+1}</span>
                    {skills.length>1&&<button className="btn btn-danger" onClick={()=>setSkills(p=>p.filter((_,j)=>j!==i))}>Remove ✕</button>}
                  </div>
                  <div className="g2">
                    <div className="field" style={{marginBottom:0}}><label>Skill Name *</label><input className="inp" placeholder="Python, Machine Learning, SQL…" value={sk.name} onChange={e=>setSkills(p=>p.map((s,j)=>j===i?{...s,name:e.target.value}:s))}/></div>
                    <div className="field" style={{marginBottom:0}}>
                      <label>Certificate <span style={{fontWeight:400,textTransform:'none',fontSize:10}}>optional</span></label>
                      <label className={`uzone ${sk.certData?'filled':''}`} style={{padding:'8px 12px',minHeight:44,cursor:'pointer'}}>
                        <input type="file" accept=".pdf,.jpg,.jpeg,.png" onChange={e=>{const f=e.target.files[0];if(f&&f.size>4*1024*1024){showToast('Max 4 MB','error');return;}b64(f).then(d=>setSkills(p=>p.map((s,j)=>j===i?{...s,certData:d,certName:f.name}:s)));}}/>
                        <div className="uzone-text" style={{fontSize:12}}>{sk.certData?<strong style={{color:'var(--green)'}}>✓ {sk.certName||'Attached'}</strong>:<strong>📎 PDF/Image</strong>}</div>
                      </label>
                    </div>
                  </div>
                </div>
              ))}
              <button className="btn btn-glass btn-sm mt8" onClick={()=>setSkills(p=>[...p,{name:'',certData:'',certName:''}])}>+ Add Skill</button>
            </div>
            <div className="card mb16" style={{padding:24}}>
              <div className="row jb mb12"><span className="slbl s-amber">💼 Work Experience</span><span className="badge b-red">Company names private</span></div>
              {exp.map((ex,i)=>(
                <div key={i} className="exp-block">
                  <div className="row jb mb8"><span style={{fontSize:11.5,fontWeight:700,letterSpacing:'.05em'}} className="ta">EXPERIENCE #{i+1}</span>{exp.length>1&&<button className="btn btn-danger" onClick={()=>setExp(p=>p.filter((_,j)=>j!==i))}>Remove ✕</button>}</div>
                  <div className="g2">
                    <div className="field" style={{marginBottom:0}}><label>Role / Position</label><input className="inp" placeholder="Software Engineer Intern" value={ex.role} onChange={e=>setExp(p=>p.map((x,j)=>j===i?{...x,role:e.target.value}:x))}/></div>
                    <div className="field" style={{marginBottom:0}}><label>Duration (months)</label><input className="inp" type="number" min="1" placeholder="6" value={ex.durationMonths} onChange={e=>setExp(p=>p.map((x,j)=>j===i?{...x,durationMonths:e.target.value}:x))}/></div>
                    <div className="field" style={{marginBottom:0}}><label>Company <span className="tr" style={{fontSize:9,marginLeft:4}}>🔒 Private</span></label><input className="inp" placeholder="Google (hidden from HR)" value={ex.company} onChange={e=>setExp(p=>p.map((x,j)=>j===i?{...x,company:e.target.value}:x))}/></div>
                    <div className="field" style={{marginBottom:0}}><label>Description</label><input className="inp" placeholder="Built APIs, improved perf 40%…" value={ex.description} onChange={e=>setExp(p=>p.map((x,j)=>j===i?{...x,description:e.target.value}:x))}/></div>
                  </div>
                </div>
              ))}
              <button className="btn btn-glass btn-sm mt8" onClick={()=>setExp(p=>[...p,{role:'',company:'',durationMonths:'',description:''}])}>+ Add Experience</button>
            </div>
            <div className="row jb wrap g12">
              <button className="btn btn-glass btn-sm" onClick={()=>setStep(2)}>← Back</button>
              <button className="btn btn-indigo" onClick={s3} disabled={loading} style={{minWidth:210,fontSize:14}}>{loading?<><span className="sp"/>Running AI Verification…</>:'🤖 Verify & Complete →'}</button>
            </div>
          </div>
        )}

        {/* ── STEP 4: Done ── */}
        {step===4&&(
          <div className="card stin" style={{padding:44,textAlign:'center'}}>
            <div className="cring">🎉</div>
            <h2 className="ub" style={{fontSize:22,fontWeight:900,marginBottom:8}}>Profile Complete!</h2>
            <p className="tm" style={{marginBottom:6}}>Candidate ID: <strong className="tc ub" style={{fontSize:15}}>{cid||localStorage.getItem('fh_cid')}</strong></p>
            <p className="tm" style={{fontSize:13,marginBottom:24}}>AI verification done. Redirecting to your dashboard…</p>
            <button className="btn btn-cyan btn-lg" onClick={()=>setPage('candidate-dashboard')}>Go to Dashboard →</button>
          </div>
        )}
      </div>
    </div>
  );
}

/* ── Candidate Login ── */
function CandidateLogin({setPage,showToast,setAuth}){
  const [email,setEmail]=useState('');
  const [pw,setPw]=useState('');
  const [loading,setLoading]=useState(false);
  async function login(){
    if(!email||!pw){showToast('Please enter email and password','error');return;}
    setLoading(true);
    try{
      const r=await api('/candidate/login',{method:'POST',body:JSON.stringify({email,password:pw})});
      localStorage.setItem('fh_token',r.token);localStorage.setItem('fh_type','candidate');localStorage.setItem('fh_cid',r.candidateId);
      setAuth(r.token,'candidate');
      setPage(r.step>=4?'candidate-dashboard':'candidate-register');
      showToast('Welcome back!','success');
    }catch(e){showToast(e.message,'error');}
    setLoading(false);
  }
  return(
    <div className="page" style={{display:'flex',alignItems:'center',justifyContent:'center'}}>
      <div style={{width:'100%',maxWidth:430}}>
        <div className="card card-cyan stin" style={{padding:36}}>
          <div style={{textAlign:'center',marginBottom:24}}><div style={{fontSize:46,marginBottom:10}}>🔐</div><h1 className="ub" style={{fontSize:20,fontWeight:900,marginBottom:5}}>Candidate Login</h1><p className="tm" style={{fontSize:13.5}}>Continue your application</p></div>
          <div className="hdiv"/>
          <div style={{marginTop:20}}>
            <div className="field"><label>Email</label><div className="inp-wrap"><span className="ic">✉️</span><input className="inp" type="email" placeholder="you@example.com" value={email} onChange={e=>setEmail(e.target.value)} onKeyDown={e=>e.key==='Enter'&&login()}/></div></div>
            <PasswordInput label="Password" value={pw} onChange={e=>setPw(e.target.value)}/>
          </div>
          <button className="btn btn-cyan" style={{width:'100%',padding:12,fontSize:14}} onClick={login} disabled={loading}>{loading?<span className="sp"/>:null} Login</button>
          <p style={{marginTop:14,textAlign:'center',fontSize:12.5,color:'var(--muted)'}}>No account? <span className="tc fw6" style={{cursor:'pointer'}} onClick={()=>setPage('candidate-register')}>Register free →</span></p>
        </div>
      </div>
    </div>
  );
}

/* ── Gauge ── */
function Gauge({label,value,color,size=70}){
  const R=size*.38,cx=size/2,cy=size/2,circ=2*Math.PI*R,pct=Math.max(0,Math.min(100,value||0));
  return(
    <div className="gauge-wrap">
      <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
        <circle cx={cx} cy={cy} r={R} fill="none" stroke="rgba(255,255,255,.06)" strokeWidth={size*.1}/>
        <circle cx={cx} cy={cy} r={R} fill="none" stroke={color} strokeWidth={size*.1} strokeDasharray={circ} strokeDashoffset={circ-(pct/100)*circ} strokeLinecap="round" transform={`rotate(-90 ${cx} ${cy})`} style={{transition:'stroke-dashoffset .8s cubic-bezier(.4,0,.2,1)'}}/>
        <text x={cx} y={cy+5} textAnchor="middle" fill="white" fontSize={size*.19} fontWeight="700" fontFamily="Unbounded,sans-serif">{pct.toFixed(0)}</text>
      </svg>
      <div className="gauge-lbl">{label}</div>
    </div>
  );
}

/* ── Candidate Dashboard ── */
function CandidateDashboard({showToast}){
  const [p,setP]=useState(null);
  const [loading,setLoading]=useState(true);
  useEffect(()=>{api('/candidate/profile').then(setP).catch(e=>showToast(e.message,'error')).finally(()=>setLoading(false));},[]);
  if(loading)return<div className="page" style={{display:'flex',alignItems:'center',justifyContent:'center',minHeight:'60vh'}}><span className="sp" style={{width:32,height:32,borderWidth:3}}/></div>;
  if(!p)return<div className="page nrw" style={{textAlign:'center',paddingTop:80}}><p>Could not load profile.</p></div>;
  const sc=p.score;
  const cc=sc?.confidence_level==='High'?'var(--green)':sc?.confidence_level==='Medium'?'var(--amber)':'var(--red)';
  const cb=sc?.confidence_level==='High'?'b-green':sc?.confidence_level==='Medium'?'b-amber':'b-red';
  return(
    <div className="page">
      <div className="ctr">
        <div className="row jb wrap g12 mb24 fu">
          <div>
            <h1 className="ub" style={{fontSize:22,fontWeight:900}}>My Dashboard</h1>
            <div className="row g8 mt8 wrap">
              <span className="badge b-cyan">ID: {p.candidateId}</span>
              {p.isShortlisted&&<span className="badge b-green">⭐ Shortlisted by HR</span>}
              {sc&&<span className={`badge ${cb}`}>{sc.confidence_level} Confidence</span>}
            </div>
          </div>
          {sc&&<div style={{textAlign:'right'}}><div className="ub" style={{fontSize:40,fontWeight:900,color:cc,lineHeight:1}}>{sc.final_score?.toFixed(1)}<span style={{fontSize:16,color:'var(--muted)'}}>/100</span></div><div style={{fontSize:11,color:'var(--muted)',marginTop:2}}>Final Score</div></div>}
        </div>
        {p.isShortlisted&&(
          <div className="notice n-green mb16 fu">
            ⭐ <strong>Congratulations!</strong> You have been shortlisted by HR. The admin team will contact you soon at <strong>{p.email}</strong>.
            {p.shortlistNote&&<div style={{marginTop:4}}>Note: {p.shortlistNote}</div>}
          </div>
        )}
        <div style={{display:'grid',gridTemplateColumns:'1fr 300px',gap:18,alignItems:'start'}}>
          <div>
            {/* Identity */}
            <div className="card fu d1" style={{padding:24,marginBottom:14,borderLeft:'3px solid var(--red)'}}>
              <div className="row jb mb12"><span className="slbl s-cyan" style={{fontSize:11}}>🔐 Your Identity — Private</span><span className="badge b-red">🔒 Hidden from HR</span></div>
              <div className="g2" style={{gap:10}}>
                {[['👤 Name',p.fullName],['✉️ Email',p.email],['📱 Phone',p.phone||'—'],['🏠 Address',p.address||'—']].map(([k,v])=>(
                  <div key={k} style={{padding:'9px 12px',background:'rgba(255,255,255,.04)',borderRadius:9,border:'1px solid var(--border)'}}>
                    <div style={{fontSize:10,color:'var(--muted)',textTransform:'uppercase',letterSpacing:'.05em',marginBottom:3}}>{k}</div>
                    <div style={{fontSize:13.5,fontWeight:500}}>{v}</div>
                  </div>
                ))}
              </div>
              {(p.photoData||p.signatureData)&&(
                <div className="g2 mt12" style={{gap:10}}>
                  {p.photoData&&<div><div style={{fontSize:10,color:'var(--muted)',textTransform:'uppercase',letterSpacing:'.05em',marginBottom:4}}>Photo</div><img src={p.photoData} alt="Photo" style={{width:'100%',maxHeight:90,objectFit:'cover',borderRadius:8,border:'1px solid var(--border)'}}/></div>}
                  {p.signatureData&&<div><div style={{fontSize:10,color:'var(--muted)',textTransform:'uppercase',letterSpacing:'.05em',marginBottom:4}}>Signature</div><img src={p.signatureData} alt="Signature" style={{width:'100%',maxHeight:60,objectFit:'contain',borderRadius:8,border:'1px solid var(--border)',background:'rgba(255,255,255,.05)',padding:4}}/></div>}
                </div>
              )}
            </div>
            {/* Qualifications */}
            {p.qualifications&&(
              <div className="card fu d2" style={{padding:24,marginBottom:14}}>
                <div className="row jb mb12"><span className="slbl s-violet" style={{fontSize:11}}>🎓 Qualifications</span><span className="badge b-amber">Scores visible · Names hidden</span></div>
                <div className="g3" style={{gap:8}}>
                  {[['10th %',p.qualifications.tenth_percentage+'%',true],['12th %',p.qualifications.twelfth_percentage+'%',true],['CGPA',p.qualifications.cgpa,true],['Degree',p.qualifications.degree||'—',true],['Branch',p.qualifications.branch||'—',true],['College',p.qualifications.college_name||'—',false],].map(([k,v,vis])=>(
                    <div key={k} style={{padding:'10px 12px',background:'rgba(255,255,255,.04)',borderRadius:9,border:`1px solid ${vis?'var(--border)':'rgba(244,63,94,.14)'}`}}>
                      <div style={{fontSize:9.5,color:'var(--muted)',textTransform:'uppercase',letterSpacing:'.06em',marginBottom:3}}>{k}</div>
                      <div className="ub" style={{fontSize:14,fontWeight:700}}>{v}</div>
                      <div style={{marginTop:4,fontSize:9.5,color:vis?'var(--green)':'var(--red)',fontWeight:600}}>{vis?'✓ HR sees':'🔒 Hidden'}</div>
                    </div>
                  ))}
                </div>
              </div>
            )}
            {/* Skills */}
            {p.skills.length>0&&(
              <div className="card fu d3" style={{padding:24,marginBottom:14}}>
                <div className="row jb mb12"><span className="slbl s-cyan" style={{fontSize:11}}>⚡ Skills</span><span className="badge b-indigo">AI Verified</span></div>
                <div style={{display:'flex',flexWrap:'wrap',gap:8}}>{p.skills.map(s=><span key={s.skill_name} className={`sk-chip ${s.is_verified?'sk-v':'sk-u'}`}>{s.skill_name} {s.is_verified?'✅':'⚠️'} <span style={{fontSize:10.5,opacity:.7}}>{s.confidence?.toFixed(0)}%</span></span>)}</div>
              </div>
            )}
            {/* Documents */}
            {p.documents?.length>0&&(
              <div className="card fu d4" style={{padding:24,marginBottom:14}}>
                <div className="row jb mb12"><span className="slbl s-orange" style={{fontSize:11}}>📂 Career Documents</span><span className="badge b-orange">Admin Access Only</span></div>
                {p.documents.map((d,i)=>(
                  <div key={i} className="doc-item"><span style={{fontSize:18}}>📄</span><div><div style={{fontSize:13,fontWeight:600}}>{d.doc_name}</div><div style={{fontSize:11,color:'var(--muted)'}}>PDF · Uploaded {d.uploaded_at?.slice(0,10)||'—'}</div></div><span className="badge b-orange" style={{marginLeft:'auto'}}>Secure</span></div>
                ))}
              </div>
            )}
            {/* Experience */}
            {p.experience.length>0&&(
              <div className="card fu d5" style={{padding:24}}>
                <div className="row jb mb12"><span className="slbl s-amber" style={{fontSize:11}}>💼 Experience</span><span className="badge b-red">Company private</span></div>
                {p.experience.map((e,i)=>(
                  <div key={i} className="ecrd"><div className="row jb"><strong style={{fontSize:13.5}}>{e.role||'—'}</strong><span className="ta ub fw7" style={{fontSize:12}}>{Math.floor((e.duration_months||0)/12)}y {(e.duration_months||0)%12}m</span></div>{e.description&&<p style={{fontSize:12.5,color:'var(--muted)',marginTop:4}}>{e.description}</p>}</div>
                ))}
              </div>
            )}
          </div>
          {/* Score sidebar */}
          {sc&&(
            <div className="card spanel fu d2">
              <h3 className="ub" style={{fontSize:13,fontWeight:700,marginBottom:16}}>📊 Score Breakdown</h3>
              <div className="fdisp"><div className="ub fnum" style={{color:cc}}>{sc.final_score?.toFixed(1)}</div><div style={{fontSize:11.5,color:'var(--muted)',marginTop:3}}>Final Score / 100</div><div style={{marginTop:8}}><span className={`badge ${cb}`}>{sc.confidence_level} Confidence</span></div><div style={{marginTop:10}}><div className="pbar"><div className="pfill" style={{width:sc.final_score+'%',background:cc}}/></div></div></div>
              <div style={{display:'flex',justifyContent:'space-around',flexWrap:'wrap',gap:10,marginBottom:16}}>
                <Gauge label="Academic"   value={sc.academic_score}     color="var(--cyan)"/>
                <Gauge label="Skills"     value={sc.skill_score}        color="var(--violet)"/>
                <Gauge label="Verified"   value={sc.verification_score} color="var(--green)"/>
                <Gauge label="Experience" value={sc.experience_score}   color="var(--amber)"/>
              </div>
              <div className="hdiv"/>
              <div style={{display:'flex',flexDirection:'column',gap:8}}>
                {[['Academic',sc.academic_score,'var(--cyan)'],['Skills',sc.skill_score,'var(--violet)'],['Verification',sc.verification_score,'var(--green)'],['Experience',sc.experience_score,'var(--amber)']].map(([l,v,c])=>(
                  <div key={l}><div className="row jb" style={{marginBottom:3}}><span style={{fontSize:11.5,color:'var(--muted)'}}>{l}</span><strong style={{fontSize:12.5,color:c,fontFamily:'Unbounded,sans-serif'}}>{v?.toFixed(1)}</strong></div><div className="pbar"><div className="pfill" style={{width:v+'%',background:c}}/></div></div>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

/* ── HR Login ── */
function HRLogin({setPage,showToast,setAuth}){
  const [u,setU]=useState('hr@fairhire.com');
  const [pw,setPw]=useState('hr123');
  const [loading,setLoading]=useState(false);
  async function login(){
    setLoading(true);
    try{const r=await api('/hr/login',{method:'POST',body:JSON.stringify({username:u,password:pw})});localStorage.setItem('fh_token',r.token);localStorage.setItem('fh_type','hr');setAuth(r.token,'hr');setPage('hr-dashboard');showToast('HR dashboard access granted','success');}
    catch(e){showToast(e.message,'error');}
    setLoading(false);
  }
  return(
    <div className="page" style={{display:'flex',alignItems:'center',justifyContent:'center'}}>
      <div style={{width:'100%',maxWidth:420}}>
        <div className="card stin" style={{padding:36}}>
          <div style={{textAlign:'center',marginBottom:24}}><div style={{width:56,height:56,borderRadius:14,background:'linear-gradient(135deg,var(--indigo),var(--violet))',display:'flex',alignItems:'center',justifyContent:'center',fontSize:24,margin:'0 auto 12px'}}>🏢</div><h1 className="ub" style={{fontSize:20,fontWeight:900,marginBottom:4}}>HR Portal</h1><p className="tm" style={{fontSize:13}}>Anonymized candidate evaluation</p></div>
          <div className="hdiv"/>
          <div style={{marginTop:18}}>
            <div className="field"><label>Email</label><div className="inp-wrap"><span className="ic">🏢</span><input className="inp" type="email" value={u} onChange={e=>setU(e.target.value)}/></div></div>
            <PasswordInput label="Password" value={pw} onChange={e=>setPw(e.target.value)}/>
          </div>
          <div style={{background:'rgba(99,102,241,.07)',border:'1px solid rgba(99,102,241,.18)',borderRadius:9,padding:'9px 13px',fontSize:12,color:'#a5b4fc',marginBottom:14}}>
            <strong>Demo:</strong> hr@fairhire.com / hr123
          </div>
          <button className="btn btn-indigo" style={{width:'100%',padding:12,fontSize:14}} onClick={login} disabled={loading}>{loading?<span className="sp"/>:null} Access HR Dashboard</button>
        </div>
      </div>
    </div>
  );
}

/* ── HR Dashboard ── */
function HRDashboard({showToast}){
  const [cands,setCands]=useState([]);
  const [sel,setSel]=useState(null);
  const [det,setDet]=useState(null);
  const [loading,setLoading]=useState(true);
  const [dlLoad,setDlLoad]=useState(false);
  const [slLoading,setSlLoading]=useState(false);
  const [sort,setSort]=useState('finalScore');
  const [cf,setCf]=useState('All');
  const [search,setSearch]=useState('');
  const [tab,setTab]=useState('all');
  const [slNote,setSlNote]=useState('');

  useEffect(()=>{api('/hr/candidates').then(setCands).catch(e=>showToast(e.message,'error')).finally(()=>setLoading(false));},[]);

  async function selectC(cid){setSel(cid);setDet(null);try{setDet(await api('/hr/candidate/'+cid));}catch(e){showToast(e.message,'error');}}

  async function toggleShortlist(cid,isShortlisted){
    setSlLoading(true);
    try{
      if(isShortlisted){
        await api('/hr/shortlist/'+cid,{method:'DELETE'});
        showToast('Removed from shortlist','success');
      } else {
        await api('/hr/shortlist/'+cid,{method:'POST',body:JSON.stringify({note:slNote})});
        showToast('✅ Candidate shortlisted! Admin will contact them.','success');
        setSlNote('');
      }
      const updated=await api('/hr/candidates');
      setCands(updated);
      if(det)setDet(await api('/hr/candidate/'+cid));
    }catch(e){showToast(e.message,'error');}
    setSlLoading(false);
  }

  async function dlReport(cid){
    setDlLoad(true);
    try{
      const tk=localStorage.getItem('fh_token');
      const res=await fetch(BASE+'/hr/report/'+cid,{headers:{Authorization:'Bearer '+tk}});
      if(!res.ok)throw new Error('Report failed');
      const blob=await res.blob();
      const url=URL.createObjectURL(blob);
      const a=document.createElement('a');a.href=url;a.download=`FairHire_${cid}.pdf`;a.click();URL.revokeObjectURL(url);
      showToast('PDF downloaded!','success');
    }catch(e){showToast(e.message,'error');}
    setDlLoad(false);
  }

  const allFiltered=[...cands].filter(c=>cf==='All'||c.confidenceLevel===cf).filter(c=>!search||c.candidateId.toLowerCase().includes(search.toLowerCase())).sort((a,b)=>(b[sort]||0)-(a[sort]||0));
  const showList=tab==='shortlisted'?allFiltered.filter(c=>c.isShortlisted):allFiltered;
  const st={total:cands.length,high:cands.filter(c=>c.confidenceLevel==='High').length,sl:cands.filter(c=>c.isShortlisted).length,avg:cands.length?+(cands.reduce((a,c)=>a+(c.finalScore||0),0)/cands.length).toFixed(1):0};

  return(
    <div className="page">
      <div className="ctr">
        <div className="row jb wrap g12 mb20 fu">
          <div><h1 className="ub" style={{fontSize:22,fontWeight:900}}>HR Evaluation Dashboard</h1><p className="tm mt4" style={{fontSize:13}}>All identities anonymized. Shortlist candidates for Admin to contact.</p></div>
          <div className="row g8 wrap">
            <input className="inp" placeholder="Search ID…" style={{width:130,padding:'8px 12px',fontSize:12.5}} value={search} onChange={e=>setSearch(e.target.value)}/>
            <select className="inp" style={{width:120,fontSize:12.5,padding:'8px 12px'}} value={cf} onChange={e=>setCf(e.target.value)}><option>All</option><option>High</option><option>Medium</option><option>Low</option></select>
            <select className="inp" style={{width:160,fontSize:12.5,padding:'8px 12px'}} value={sort} onChange={e=>setSort(e.target.value)}>
              <option value="finalScore">↓ Final Score</option><option value="academicScore">↓ Academic</option><option value="skillScore">↓ Skills</option>
            </select>
          </div>
        </div>
        <div className="g4 mb16 fu d1">
          {[{l:'Total',v:st.total,c:'var(--cyan)',li:'linear-gradient(90deg,var(--cyan),var(--indigo))'},{l:'High Confidence',v:st.high,c:'var(--green)',li:'var(--green)'},{l:'Shortlisted',v:st.sl,c:'var(--amber)',li:'var(--amber)'},{l:'Avg Score',v:st.avg,c:'#c4b5fd',li:'linear-gradient(90deg,var(--violet),var(--pink))'},].map(s=>(
            <div key={s.l} className="card sc" style={{position:'relative',overflow:'hidden'}}><div className="grid-bg"/><div className="sc-n" style={{color:s.c,fontSize:24}}>{s.v}</div><div className="sc-l">{s.l}</div><div className="sc-line" style={{background:s.li}}/></div>
          ))}
        </div>

        {/* TABS */}
        <div className="tabs fu d2">
          <button className={`tab ${tab==='all'?'active':''}`} onClick={()=>setTab('all')}>All Candidates ({cands.length})</button>
          <button className={`tab ${tab==='shortlisted'?'active':''}`} onClick={()=>setTab('shortlisted')}>⭐ Shortlisted ({st.sl})</button>
        </div>

        {tab==='shortlisted'&&st.sl===0&&(
          <div className="notice n-cyan mb16">No candidates shortlisted yet. Shortlist candidates from the "All Candidates" tab.</div>
        )}

        <div style={{display:'grid',gridTemplateColumns:sel?'1fr 360px':'1fr',gap:14,alignItems:'start'}}>
          <div className="card fu d2" style={{overflow:'hidden'}}>
            {loading?<div style={{padding:50,textAlign:'center'}}><span className="sp" style={{width:28,height:28,borderWidth:3,margin:'auto'}}/></div>
              :showList.length===0?<div style={{padding:50,textAlign:'center',color:'var(--muted)'}}>No candidates found.</div>
              :<table className="tbl">
                <thead><tr><th></th><th>ID</th><th>10th</th><th>12th</th><th>CGPA</th><th>Skills</th><th>Exp</th><th>Score</th><th>Conf</th><th>Actions</th></tr></thead>
                <tbody>
                  {showList.map(c=>(
                    <tr key={c.candidateId} onClick={()=>selectC(c.candidateId)} className={`${sel===c.candidateId?'sel':''} ${c.isShortlisted?'shortlisted-row':''}`}>
                      <td>{c.isShortlisted&&<span className="shortlist-dot"/>}</td>
                      <td><strong className="ub tc" style={{fontSize:12}}>{c.candidateId}</strong></td>
                      <td>{c.tenthPercentage??'—'}%</td>
                      <td>{c.twelfthPercentage??'—'}%</td>
                      <td><strong>{c.cgpa??'—'}</strong></td>
                      <td><div style={{display:'flex',flexWrap:'wrap',gap:3}}>{(c.skills||[]).slice(0,2).map(s=><span key={s.name} style={{fontSize:10,padding:'1px 7px',borderRadius:5,fontWeight:600,background:s.verified?'rgba(16,185,129,.1)':'rgba(245,158,11,.1)',color:s.verified?'var(--green)':'var(--amber)',border:`1px solid ${s.verified?'rgba(16,185,129,.2)':'rgba(245,158,11,.2)'}`}}>{s.name} {s.verified?'✓':'⚠'}</span>)}{(c.skills?.length||0)>2&&<span style={{fontSize:10,color:'var(--muted)'}}>+{c.skills.length-2}</span>}</div></td>
                      <td>{c.experienceYears??0}yr</td>
                      <td><strong className="ub" style={{fontSize:13,color:(c.finalScore||0)>=75?'var(--green)':(c.finalScore||0)>=50?'var(--amber)':'var(--red)'}}>{c.finalScore?.toFixed(1)??'—'}</strong></td>
                      <td><span className={`badge ${c.confidenceLevel==='High'?'b-green':c.confidenceLevel==='Medium'?'b-amber':'b-red'}`} style={{fontSize:9.5}}>{c.confidenceLevel||'—'}</span></td>
                      <td onClick={e=>e.stopPropagation()}>
                        <div className="row g6">
                          <button className={`btn btn-xs ${c.isShortlisted?'btn-danger':'btn-green'}`} onClick={()=>toggleShortlist(c.candidateId,c.isShortlisted)} disabled={slLoading} title={c.isShortlisted?'Remove shortlist':'Shortlist'}>
                            {c.isShortlisted?'✕ Remove':'⭐ Select'}
                          </button>
                          <button className="btn btn-glass btn-xs" onClick={()=>dlReport(c.candidateId)} disabled={dlLoad}>⬇</button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            }
          </div>
          {sel&&(
            <div className="card slr" style={{padding:22,position:'sticky',top:80}}>
              <div className="row jb mb12">
                <div><div style={{fontSize:10.5,color:'var(--muted)',letterSpacing:'.06em',textTransform:'uppercase',marginBottom:2}}>Candidate</div><strong className="ub tc" style={{fontSize:14}}>{sel}</strong></div>
                <button className="btn btn-glass btn-xs" onClick={()=>{setSel(null);setDet(null);}}>✕</button>
              </div>
              <div className="hdiv" style={{margin:'10px 0'}}/>
              {!det?<div style={{textAlign:'center',padding:36}}><span className="sp" style={{width:26,height:26,margin:'auto'}}/></div>:(<>
                {det.score&&(<>
                  <div className="fdisp mb14">
                    <div className="ub fnum" style={{fontSize:38,color:det.score.confidence_level==='High'?'var(--green)':det.score.confidence_level==='Medium'?'var(--amber)':'var(--red)'}}>{det.score.final_score?.toFixed(1)}</div>
                    <div style={{fontSize:11,color:'var(--muted)',marginTop:2}}>Final Score / 100</div>
                    <span className={`badge ${det.score.confidence_level==='High'?'b-green':det.score.confidence_level==='Medium'?'b-amber':'b-red'}`} style={{marginTop:7,display:'inline-flex'}}>{det.score.confidence_level} Confidence</span>
                  </div>
                  <div style={{display:'flex',justifyContent:'space-around',gap:6,flexWrap:'wrap',marginBottom:12}}>
                    <Gauge label="Academic" value={det.score.academic_score} color="var(--cyan)" size={58}/>
                    <Gauge label="Skills" value={det.score.skill_score} color="var(--violet)" size={58}/>
                    <Gauge label="Exp" value={det.score.experience_score} color="var(--amber)" size={58}/>
                  </div>
                </>)}
                {det.qualifications&&(<>
                  <div className="slbl s-cyan" style={{fontSize:10,marginBottom:7}}>Academic</div>
                  <div className="g2" style={{gap:6,marginBottom:12}}>
                    {[['10th',det.qualifications.tenth_percentage+'%'],['12th',det.qualifications.twelfth_percentage+'%'],['CGPA',det.qualifications.cgpa],['Degree',det.qualifications.degree]].map(([k,v])=>(
                      <div key={k} style={{padding:'6px 10px',background:'rgba(255,255,255,.04)',borderRadius:7}}><div style={{fontSize:9,color:'var(--muted)',marginBottom:1,textTransform:'uppercase',letterSpacing:'.05em'}}>{k}</div><div style={{fontSize:12.5,fontWeight:600}}>{v||'—'}</div></div>
                    ))}
                  </div>
                </>)}
                {det.skills?.length>0&&(<>
                  <div className="slbl s-cyan" style={{fontSize:10,marginBottom:7}}>Skills</div>
                  {det.skills.map(s=><div key={s.skill_name} className="row jb" style={{padding:'6px 10px',background:'rgba(255,255,255,.04)',borderRadius:7,marginBottom:5}}><span style={{fontSize:12.5,fontWeight:500}}>{s.skill_name}</span><div className="row g8"><span style={{fontSize:10.5,color:'var(--muted)'}}>{s.confidence?.toFixed(0)}%</span><span>{s.is_verified?'✅':'⚠️'}</span></div></div>)}
                </>)}
                {det.experience?.length>0&&(<><div className="slbl s-amber" style={{fontSize:10,marginBottom:7,marginTop:10}}>Experience</div>{det.experience.map((e,i)=><div key={i} className="ecrd" style={{marginBottom:5}}><div className="row jb"><span style={{fontSize:12.5,fontWeight:600}}>{e.role||'—'}</span><span className="ta ub fw7" style={{fontSize:11}}>{e.duration_months}m</span></div></div>)}</>)}
                <div className="hdiv"/>
                {/* Shortlist section */}
                {!det.isShortlisted&&(
                  <div style={{marginBottom:10}}>
                    <label style={{fontSize:11,color:'var(--muted)',fontWeight:600,textTransform:'uppercase',letterSpacing:'.06em',display:'block',marginBottom:5}}>Note for Admin (optional)</label>
                    <input className="inp" placeholder="e.g. Strong Python skills, interview asap" value={slNote} onChange={e=>setSlNote(e.target.value)} style={{fontSize:12.5,padding:'8px 12px'}}/>
                  </div>
                )}
                <div className="g2" style={{gap:8}}>
                  <button className={`btn ${det.isShortlisted?'btn-danger':'btn-green'}`} style={{width:'100%',padding:'9px'}} onClick={()=>toggleShortlist(sel,det.isShortlisted)} disabled={slLoading}>
                    {slLoading?<span className="sp"/>:det.isShortlisted?'✕ Remove Shortlist':'⭐ Shortlist Candidate'}
                  </button>
                  <button className="btn btn-indigo" style={{width:'100%',padding:'9px'}} onClick={()=>dlReport(sel)} disabled={dlLoad}>{dlLoad?<span className="sp"/>:'⬇ PDF'}</button>
                </div>
                {det.isShortlisted&&<div className="notice n-green mt8" style={{fontSize:11.5}}>✅ Shortlisted. Admin can now see their contact details and reach out.</div>}
              </>)}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

/* ── Admin Login ── */
function AdminLogin({setPage,showToast,setAuth}){
  const [u,setU]=useState('admin@fairhire.com');
  const [pw,setPw]=useState('admin123');
  const [loading,setLoading]=useState(false);
  async function login(){
    setLoading(true);
    try{const r=await api('/admin/login',{method:'POST',body:JSON.stringify({username:u,password:pw})});localStorage.setItem('fh_token',r.token);localStorage.setItem('fh_type','admin');setAuth(r.token,'admin');setPage('admin-dashboard');showToast('Admin access granted ⚙️','success');}
    catch(e){showToast(e.message,'error');}
    setLoading(false);
  }
  return(
    <div className="page" style={{display:'flex',alignItems:'center',justifyContent:'center'}}>
      <div style={{width:'100%',maxWidth:420}}>
        <div className="card card-orange stin" style={{padding:36}}>
          <div style={{textAlign:'center',marginBottom:24}}><div style={{width:60,height:60,borderRadius:14,background:'linear-gradient(135deg,var(--orange),var(--amber))',display:'flex',alignItems:'center',justifyContent:'center',fontSize:26,margin:'0 auto 12px'}}>⚙️</div><h1 className="ub" style={{fontSize:20,fontWeight:900,marginBottom:4}}>Admin Portal</h1><p className="tm" style={{fontSize:13}}>Full access — all candidate data</p></div>
          <div className="hdiv"/>
          <div style={{marginTop:18}}>
            <div className="field"><label>Admin Email</label><div className="inp-wrap"><span className="ic">⚙️</span><input className="inp" type="email" value={u} onChange={e=>setU(e.target.value)}/></div></div>
            <PasswordInput label="Admin Password" value={pw} onChange={e=>setPw(e.target.value)}/>
          </div>
          <div style={{background:'rgba(249,115,22,.07)',border:'1px solid rgba(249,115,22,.18)',borderRadius:9,padding:'9px 13px',fontSize:12,color:'var(--orange)',marginBottom:14}}>
            <strong>Demo:</strong> admin@fairhire.com / admin123
          </div>
          <button className="btn btn-orange" style={{width:'100%',padding:12,fontSize:14}} onClick={login} disabled={loading}>{loading?<span className="sp"/>:null} Access Admin Dashboard</button>
        </div>
      </div>
    </div>
  );
}

/* ── Admin Dashboard ── */
function AdminDashboard({showToast}){
  const [cands,setCands]=useState([]);
  const [sel,setSel]=useState(null);
  const [det,setDet]=useState(null);
  const [stats,setStats]=useState(null);
  const [loading,setLoading]=useState(true);
  const [tab,setTab]=useState('all');
  const [search,setSearch]=useState('');

  useEffect(()=>{
    Promise.all([api('/admin/candidates'),api('/admin/stats')])
      .then(([c,s])=>{setCands(c);setStats(s);})
      .catch(e=>showToast(e.message,'error'))
      .finally(()=>setLoading(false));
  },[]);

  async function selectC(cid){
    setSel(cid);setDet(null);
    try{setDet(await api('/admin/candidate/'+cid));}catch(e){showToast(e.message,'error');}
  }

  const filtered=cands
    .filter(c=>tab==='shortlisted'?c.isShortlisted:true)
    .filter(c=>!search||c.candidateId.toLowerCase().includes(search.toLowerCase())||c.fullName.toLowerCase().includes(search.toLowerCase())||c.email.toLowerCase().includes(search.toLowerCase()));

  return(
    <div className="page">
      <div className="ctr">
        <div className="row jb wrap g12 mb20 fu">
          <div>
            <h1 className="ub" style={{fontSize:22,fontWeight:900}}>Admin Dashboard <span className="to">⚙️</span></h1>
            <p className="tm mt4" style={{fontSize:13}}>Full access to all candidate data. Contact shortlisted candidates.</p>
          </div>
          <input className="inp" placeholder="Search by ID, name, email…" style={{width:240,padding:'8px 12px',fontSize:12.5}} value={search} onChange={e=>setSearch(e.target.value)}/>
        </div>

        {/* Stats */}
        {stats&&(
          <div className="g4 mb16 fu d1">
            {[{l:'Total Candidates',v:stats.totalCandidates,c:'var(--cyan)',li:'linear-gradient(90deg,var(--cyan),var(--indigo))'},{l:'Verified',v:stats.verified,c:'var(--green)',li:'var(--green)'},{l:'Shortlisted by HR',v:stats.shortlisted,c:'var(--amber)',li:'var(--amber)'},{l:'Avg Score',v:stats.avgScore,c:'var(--orange)',li:'linear-gradient(90deg,var(--orange),var(--amber))'},].map(s=>(
              <div key={s.l} className="card sc"><div className="grid-bg"/><div className="sc-n" style={{color:s.c,fontSize:24}}>{s.v}</div><div className="sc-l">{s.l}</div><div className="sc-line" style={{background:s.li}}/></div>
            ))}
          </div>
        )}

        <div className="tabs fu d2">
          <button className={`tab ${tab==='all'?'active':''}`} onClick={()=>setTab('all')}>All Candidates ({cands.length})</button>
          <button className={`tab ${tab==='shortlisted'?'active':''}`} onClick={()=>setTab('shortlisted')}>⭐ Shortlisted ({cands.filter(c=>c.isShortlisted).length})</button>
        </div>

        {tab==='shortlisted'&&filtered.length===0&&(
          <div className="notice n-amber mb16">HR has not shortlisted any candidates yet.</div>
        )}

        <div style={{display:'grid',gridTemplateColumns:sel?'1fr 400px':'1fr',gap:14,alignItems:'start'}}>
          {/* Table */}
          <div className="card fu d2" style={{overflow:'hidden'}}>
            {loading?<div style={{padding:50,textAlign:'center'}}><span className="sp" style={{width:28,height:28,borderWidth:3,margin:'auto'}}/></div>
              :filtered.length===0?<div style={{padding:50,textAlign:'center',color:'var(--muted)'}}>No candidates found.</div>
              :<table className="tbl">
                <thead><tr><th></th><th>ID</th><th>Full Name</th><th>Email</th><th>Phone</th><th>DOB</th><th>Score</th><th>Status</th></tr></thead>
                <tbody>
                  {filtered.map(c=>(
                    <tr key={c.candidateId} onClick={()=>selectC(c.candidateId)} className={`${sel===c.candidateId?'sel':''} ${c.isShortlisted?'shortlisted-row':''}`}>
                      <td>{c.isShortlisted&&<span className="shortlist-dot"/>}</td>
                      <td><strong className="ub to" style={{fontSize:12}}>{c.candidateId}</strong></td>
                      <td style={{fontWeight:600}}>{c.fullName}</td>
                      <td style={{color:'var(--cyan)',fontSize:12.5}}>{c.email}</td>
                      <td style={{fontSize:12.5}}>{c.phone||'—'}</td>
                      <td style={{fontSize:12.5}}>{c.dob||'—'}</td>
                      <td><strong style={{color:(c.finalScore||0)>=75?'var(--green)':(c.finalScore||0)>=50?'var(--amber)':'var(--red)',fontFamily:'Unbounded,sans-serif',fontSize:13}}>{c.finalScore?.toFixed(1)??'—'}</strong></td>
                      <td>{c.isShortlisted?<span className="badge b-green">⭐ Shortlisted</span>:<span className="badge b-indigo">In Pool</span>}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            }
          </div>

          {/* Detail Drawer */}
          {sel&&(
            <div className="card slr" style={{padding:22,position:'sticky',top:80,maxHeight:'calc(100vh - 100px)',overflowY:'auto'}}>
              <div className="row jb mb10">
                <div>
                  <div style={{fontSize:10,color:'var(--muted)',letterSpacing:'.06em',textTransform:'uppercase',marginBottom:2}}>Full Admin View</div>
                  <strong className="ub to" style={{fontSize:14}}>{sel}</strong>
                </div>
                <button className="btn btn-glass btn-xs" onClick={()=>{setSel(null);setDet(null);}}>✕</button>
              </div>
              <div className="hdiv" style={{margin:'8px 0'}}/>

              {!det?<div style={{textAlign:'center',padding:36}}><span className="sp" style={{width:26,height:26,margin:'auto'}}/></div>:(<>
                {/* CONTACT CARD */}
                {det.isShortlisted&&(
                  <div className="contact-card">
                    <div style={{fontSize:11,fontWeight:800,color:'var(--green)',letterSpacing:'.07em',textTransform:'uppercase',marginBottom:10}}>⭐ SHORTLISTED — CONTACT INFO</div>
                    {[['📧','Email',det.email],['📱','Phone',det.phone||'—'],['🏠','Address',det.address||'—'],['🎂','Date of Birth',det.dob||'—']].map(([ic,l,v])=>(
                      <div key={l} className="contact-row"><span className="contact-icon">{ic}</span><div><div className="contact-label">{l}</div><div className="contact-value">{v}</div></div></div>
                    ))}
                    {det.shortlistNote&&<div style={{marginTop:8,padding:'7px 10px',background:'rgba(16,185,129,.08)',borderRadius:7,fontSize:12,color:'var(--green)'}}><strong>HR Note:</strong> {det.shortlistNote}</div>}
                  </div>
                )}

                {/* FULL IDENTITY */}
                <div className="slbl s-orange" style={{fontSize:10.5,marginBottom:8,marginTop:8}}>Full Identity (Admin Only)</div>
                <div className="g2" style={{gap:6,marginBottom:12}}>
                  {[['Name',det.fullName],['Email',det.email],['Phone',det.phone||'—'],['DOB',det.dob||'—'],['Address',det.address||'—'],['Gov ID',det.govIdType+': '+det.govIdNumber]].map(([k,v])=>(
                    <div key={k} style={{padding:'7px 10px',background:'rgba(255,255,255,.04)',borderRadius:7}}><div style={{fontSize:9,color:'var(--muted)',marginBottom:1,textTransform:'uppercase',letterSpacing:'.05em'}}>{k}</div><div style={{fontSize:12.5,fontWeight:600,wordBreak:'break-all'}}>{v}</div></div>
                  ))}
                </div>

                {/* PASSWORD */}
                <div style={{padding:'10px 12px',background:'rgba(244,63,94,.07)',border:'1px solid rgba(244,63,94,.18)',borderRadius:9,marginBottom:12}}>
                  <div style={{fontSize:9.5,color:'var(--red)',textTransform:'uppercase',letterSpacing:'.06em',fontWeight:700,marginBottom:4}}>🔑 Password (Admin Only)</div>
                  <div style={{fontFamily:'JetBrains Mono,monospace',fontSize:14,fontWeight:700,color:'var(--text)',letterSpacing:'.05em'}}>{det.passwordPlain||'—'}</div>
                </div>

                {/* PHOTO & SIGNATURE */}
                {(det.photoData||det.signatureData)&&(
                  <>
                    <div className="slbl s-cyan" style={{fontSize:10.5,marginBottom:8}}>Photo & Signature</div>
                    <div className="g2" style={{gap:8,marginBottom:12}}>
                      {det.photoData&&(
                        <div>
                          <div style={{fontSize:9.5,color:'var(--muted)',textTransform:'uppercase',letterSpacing:'.05em',marginBottom:4}}>Photo</div>
                          <div className="img-preview-wrap"><img src={det.photoData} alt="Candidate Photo" className="img-preview"/></div>
                        </div>
                      )}
                      {det.signatureData&&(
                        <div>
                          <div style={{fontSize:9.5,color:'var(--muted)',textTransform:'uppercase',letterSpacing:'.05em',marginBottom:4}}>Signature</div>
                          <div className="img-preview-wrap" style={{background:'rgba(255,255,255,.07)'}}><img src={det.signatureData} alt="Signature" className="img-preview" style={{maxHeight:80}}/></div>
                        </div>
                      )}
                    </div>
                  </>
                )}

                {/* QUALIFICATIONS */}
                {det.qualifications&&(<>
                  <div className="slbl s-violet" style={{fontSize:10.5,marginBottom:8}}>Qualifications (Full)</div>
                  <div className="g2" style={{gap:6,marginBottom:12}}>
                    {[['10th %',det.qualifications.tenth_percentage+'%'],['10th Board',det.qualifications.tenth_board],['12th %',det.qualifications.twelfth_percentage+'%'],['12th Board',det.qualifications.twelfth_board],['Degree',det.qualifications.degree],['Branch',det.qualifications.branch],['CGPA',det.qualifications.cgpa],['College',det.qualifications.college_name||'—'],['School',det.qualifications.school_name||'—']].map(([k,v])=>(
                      <div key={k} style={{padding:'6px 10px',background:'rgba(255,255,255,.04)',borderRadius:7}}><div style={{fontSize:9,color:'var(--muted)',marginBottom:1,textTransform:'uppercase',letterSpacing:'.05em'}}>{k}</div><div style={{fontSize:12.5,fontWeight:600}}>{v||'—'}</div></div>
                    ))}
                  </div>
                </>)}

                {/* CAREER DOCUMENTS */}
                {det.documents?.length>0&&(<>
                  <div className="slbl s-orange" style={{fontSize:10.5,marginBottom:8}}>Career Documents ({det.documents.length})</div>
                  {det.documents.map((d,i)=>(
                    <div key={i} className="doc-item">
                      <span style={{fontSize:20}}>📄</span>
                      <div style={{flex:1}}>
                        <div style={{fontSize:12.5,fontWeight:600}}>{d.name}</div>
                        <div style={{fontSize:10.5,color:'var(--muted)'}}>PDF · {d.uploadedAt?.slice(0,10)||'—'}</div>
                      </div>
                      {d.data&&(
                        <button className="btn btn-glass btn-xs" onClick={()=>{
                          const link=document.createElement('a');
                          link.href=d.data;link.download=d.name+'.pdf';link.click();
                        }}>⬇ Download</button>
                      )}
                    </div>
                  ))}
                </>)}

                {/* SKILLS */}
                {det.skills?.length>0&&(<>
                  <div className="slbl s-cyan" style={{fontSize:10.5,marginBottom:8,marginTop:8}}>Skills</div>
                  {det.skills.map(s=><div key={s.skill_name} className="row jb" style={{padding:'6px 10px',background:'rgba(255,255,255,.04)',borderRadius:7,marginBottom:5}}><span style={{fontSize:12.5,fontWeight:500}}>{s.skill_name}</span><div className="row g8"><span style={{fontSize:10.5,color:'var(--muted)'}}>{s.confidence?.toFixed(0)}%</span><span>{s.is_verified?'✅':'⚠️'}</span></div></div>)}
                </>)}

                {/* EXPERIENCE WITH COMPANY NAMES */}
                {det.experience?.length>0&&(<>
                  <div className="slbl s-amber" style={{fontSize:10.5,marginBottom:8,marginTop:10}}>Experience (with Company Names)</div>
                  {det.experience.map((e,i)=>(
                    <div key={i} className="ecrd">
                      <div className="row jb"><span style={{fontSize:12.5,fontWeight:600}}>{e.role||'—'}</span><span className="ta ub fw7" style={{fontSize:11}}>{e.duration_months}m</span></div>
                      {e.company_name&&<div style={{fontSize:11.5,color:'var(--amber)',marginTop:3}}>🏢 {e.company_name}</div>}
                      {e.description&&<div style={{fontSize:11.5,color:'var(--muted)',marginTop:2}}>{e.description}</div>}
                    </div>
                  ))}
                </>)}

                {/* SCORE */}
                {det.score&&(<>
                  <div className="slbl s-green" style={{fontSize:10.5,marginBottom:8,marginTop:10}}>Evaluation Score</div>
                  <div style={{padding:'12px 14px',background:'rgba(0,212,255,.05)',border:'1px solid rgba(0,212,255,.12)',borderRadius:10}}>
                    {[['Final Score',det.score.final_score?.toFixed(1)+' / 100'],['Confidence',det.score.confidence_level],['Academic',det.score.academic_score?.toFixed(1)],['Skills',det.score.skill_score?.toFixed(1)],['Verification',det.score.verification_score?.toFixed(1)],['Experience',det.score.experience_score?.toFixed(1)]].map(([k,v])=>(
                      <div key={k} className="row jb" style={{padding:'4px 0',borderBottom:'1px solid rgba(255,255,255,.04)'}}><span style={{fontSize:11.5,color:'var(--muted)'}}>{k}</span><strong style={{fontSize:12,fontFamily:'Unbounded,sans-serif',color:'var(--cyan)'}}>{v}</strong></div>
                    ))}
                  </div>
                </>)}
              </>)}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

/* ── App Root ── */
function App(){
  const [page,setPage]=useState('landing');
  const [token,setToken]=useState(localStorage.getItem('fh_token'));
  const [userType,setUType]=useState(localStorage.getItem('fh_type'));
  const [toast,setToast]=useState(null);
  function setAuth(t,type){setToken(t);setUType(type);}
  function logout(){['fh_token','fh_type','fh_cid'].forEach(k=>localStorage.removeItem(k));setToken(null);setUType(null);setPage('landing');}
  function showToast(msg,type='success'){setToast({msg,type,key:Date.now()});}
  const P={setPage,showToast,setAuth,token,userType};
  return(<>
    <Nav page={page} setPage={setPage} token={token} userType={userType} onLogout={logout}/>
    {page==='landing'            &&<Landing {...P}/>}
    {page==='candidate-register' &&<CandidateRegister {...P}/>}
    {page==='candidate-login'    &&<CandidateLogin {...P}/>}
    {page==='candidate-dashboard'&&<CandidateDashboard {...P}/>}
    {page==='hr-login'           &&<HRLogin {...P}/>}
    {page==='hr-dashboard'       &&<HRDashboard {...P}/>}
    {page==='admin-login'        &&<AdminLogin {...P}/>}
    {page==='admin-dashboard'    &&<AdminDashboard {...P}/>}
    {toast&&<Toast key={toast.key} msg={toast.msg} type={toast.type} onClose={()=>setToast(null)}/>}
  </>);
}
ReactDOM.createRoot(document.getElementById('root')).render(<App/>);
</script>
</body>
</html>
