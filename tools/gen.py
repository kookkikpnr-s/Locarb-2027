import re, json, os
ROOT='/mnt/user-data/outputs/artifacts/f4e40824-ae7d-4cfb-9d09-67115159c811/project/'
CSS='/_blob/e530b10be96a1b830084b553d65ae46d'
HERO_IMG='/_blob/76a10b9728d986483bbe8ab87e4dd874'
HAND_IMG='/_blob/070ecf4ba0bce5a6105896c061bf806d'
main=open(ROOT+'Main.dc.html').read()

LINKS={'#top':'Main.dc.html','#about':'About-Story.dc.html','#about-story':'About-Story.dc.html','#certificates':'About-Certificates.dc.html','#board':'About-Board.dc.html','#solutions':'Main.dc.html','#ifrs':'Solution-IFRS.dc.html','#carboncal':'Solution-CarbonCal.dc.html','#issb':'Solution-ISSB.dc.html','#scout':'Solution-CarbonScout.dc.html','#reporting':'Solution-Reporting.dc.html','#blog':'Blog.dc.html','#blog-hub':'Blog.dc.html','#portfolio':'Blog-Portfolio.dc.html','#knowledge':'Blog-Knowledge.dc.html','#others':'Blog-News.dc.html','#contact':'Contact.dc.html','#contact-form':'Contact.dc.html','#careers':'Contact.dc.html'}
def relink(h):
    return re.sub(r'href="(#[a-z\-]+)"',lambda m:'href="%s"'%LINKS.get(m.group(1),m.group(1)),h)

nav=main[main.index('<header class="nav">'):main.index('<!-- /search -->')+len('<!-- /search -->')]
nav=relink(nav)
foot=main[main.index('<footer class="foot dark'):main.index('</footer>')+9]
foot=relink(foot).replace('href="#top" class="totop"','href="#page-top" class="totop"').replace('href="Main.dc.html" class="totop"','href="#page-top" class="totop"')

def navfor(active):
    n=nav
    if active:
        key={'about':'About-Story.dc.html','solutions':'Main.dc.html','blog':'Blog.dc.html'}[active]
        n=n.replace('<div class="dd"><a href="%s"'%key,'<div class="dd cur"><a href="%s"'%key,1)
    return n

AR='<svg class="ar" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'
UP='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M7 17L17 7M9 7h8v8"></path></svg>'
CHK='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M5 12l5 5L20 7"></path></svg>'
ICONS={'story':'<path d="M5 19c0-8 5-13 14-14 0 9-5 14-13 14"></path><path d="M5 19l7-7"></path>',
'cert':'<circle cx="12" cy="9" r="6"></circle><path d="M8.5 14l-1.5 8 5-3 5 3-1.5-8"></path>',
'board':'<circle cx="9" cy="8" r="3"></circle><circle cx="17" cy="9" r="2.5"></circle><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M15 20c0-2.4 1.6-4.5 4-5"></path>',
'doc':'<path d="M7 3h7l5 5v13H7z"></path><path d="M14 3v5h5M10 13h6M10 17h4"></path>',
'chart':'<path d="M4 19V9M10 19V5M16 19v-7M22 19H2"></path>',
'cap':'<path d="M2 9l10-5 10 5-10 5z"></path><path d="M6 11v5c3 2.5 9 2.5 12 0v-5"></path>',
'scout':'<circle cx="12" cy="12" r="9"></circle><circle cx="12" cy="12" r="4"></circle><path d="M12 3v3M12 18v3M3 12h3M18 12h3"></path>',
'rep':'<path d="M4 4h16v16H4z"></path><path d="M8 15l3-3 2 2 3-4"></path>',
'bolt':'<path d="M13 2L4 14h7l-1 8 9-12h-7z"></path>',
'shield':'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"></path><path d="M9 12l2 2 4-4"></path>',
'users':'<circle cx="9" cy="8" r="3"></circle><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"></path><path d="M16 4a3 3 0 0 1 0 6M21 20c0-2.6-1.5-4.8-4-5.6"></path>',
'target':'<circle cx="12" cy="12" r="9"></circle><circle cx="12" cy="12" r="5"></circle><circle cx="12" cy="12" r="1.5"></circle>',
'layers':'<path d="M12 3l9 5-9 5-9-5z"></path><path d="M3 13l9 5 9-5"></path>',
'clock':'<circle cx="12" cy="12" r="9"></circle><path d="M12 7v5l3 2"></path>',
'lines':'<path d="M4 12h16M4 6h10M4 18h7"></path>',
'growth':'<path d="M4 19l6-6 4 4 6-8"></path><path d="M15 9h5v5"></path>',
'mail':'<rect x="3" y="5" width="18" height="14" rx="2"></rect><path d="M3 7l9 6 9-6"></path>',
'info':'<circle cx="12" cy="12" r="9"></circle><path d="M12 11v6M12 7.5v.5"></path>'}
def ic(k,size=22,w=1.8): return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>'%(size,size,w,ICONS[k])

def crumbs(items):
    out=['<nav class="crumbs" aria-label="Breadcrumb"><a href="Main.dc.html">Home</a>']
    for i,(t,h) in enumerate(items):
        out.append('<i></i>')
        out.append('<b>%s</b>'%t if h is None else '<a href="%s">%s</a>'%(h,t))
    out.append('</nav>'); return ''.join(out)

def label(t,dark=False):
    st=' style="color:#8FE3B0"' if dark else ''
    return '<p class="label"%s><span class="ln"></span>%s</p>'%(st,t)

def pcta(h2,p,b1,b1h,b2=None,b2h=None):
    btn2='<a href="%s" class="btn btn-o">%s</a>'%(b2h,b2) if b2 else ''
    return '''<section class="pcta dark">
<div class="ring" style="width:560px;height:560px;right:-180px;top:-240px" aria-hidden="true"></div>
<div class="ring" style="width:340px;height:340px;right:-70px;top:-130px" aria-hidden="true"></div>
<div class="wrap pctagrid">
<div class="rv">%s<h2 class="display h2" style="max-width:16ch">%s</h2></div>
<div class="rv2"><p class="lead" style="color:#DCE9DE;font-size:calc(17px*var(--s))">%s</p><div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:28px"><a href="%s" class="btn btn-l">%s %s</a>%s</div></div>
</div>
</section>'''%(label("Let's talk",True),h2,p,b1h,b1,AR,btn2)

def inline_form(sol):
    return '''<div class="formwrap">
<div class="rv">
<sc-if value="{{notSent}}" hint-placeholder-val="{{ true }}">
<div class="form">
<div class="fld full"><span class="flab">Solution</span><div class="presel">'''+CHK+''' '''+sol+''' <span style="margin-left:auto;font-size:13px;color:#4A4A42">Pre-selected</span></div></div>
<div class="fld"><label for="n1">Name <em>*</em></label><input id="n1" type="text" placeholder="Your full name"></div>
<div class="fld"><label for="e1">Email <em>*</em></label><input id="e1" type="email" placeholder="name@company.com"></div>
<div class="fld"><label for="c1">Company</label><input id="c1" type="text" placeholder="Company name"></div>
<div class="fld"><label for="p1">Position</label><input id="p1" type="text" placeholder="Your role"></div>
<div class="fld full"><label for="m1">Message</label><textarea id="m1" placeholder="Tell us where you are today and what you need."></textarea></div>
<div class="full"><button class="cbx {{agreeCls}}" onClick="{{toggleAgree}}" role="checkbox" aria-checked="{{agreeAria}}"><span class="bx">'''+CHK+'''</span><span>I agree to the <a href="#privacy">privacy policy</a> (PDPA). <em style="font-style:normal;color:#0EA552">*</em></span></button></div>
<sc-if value="{{err}}" hint-placeholder-val="{{ false }}"><p class="ferr full" style="margin:0">Please accept the privacy policy to send your message.</p></sc-if>
<div class="full"><button class="btn btn-p" onClick="{{submit}}">Send message '''+AR+'''</button></div>
</div>
</sc-if>
<sc-if value="{{sent}}" hint-placeholder-val="{{ false }}">
<div class="okmsg"><span class="oi">'''+CHK+'''</span><div><b>Thank you</b><p>Your message has been well received. Our '''+sol+''' team will get back to you.</p></div><button onClick="{{closeOk}}" aria-label="Close message">✕</button></div>
</sc-if>
</div>
<div class="cinfo rv2">
<div class="row2"><small>Goes to</small><b>contact@locarb.green</b><span>Tagged with '''+sol+''' and the page you came from.</span></div>
<div class="row2"><small>Prefer email?</small><b><a href="mailto:contact@locarb.green">contact@locarb.green</a></b><span>Business and partnership enquiries</span></div>
<div class="row2"><small>Careers</small><b><a href="mailto:hr@locarb.green">hr@locarb.green</a></b><span>Job seekers and interns</span></div>
</div>
</div>'''

FORM_JS='''const extra = {
      notSent: !st.sent, sent: !!st.sent, err: !!st.err,
      agreeCls: st.agree ? 'on' : '', agreeAria: st.agree ? 'true' : 'false',
      toggleAgree: () => this.setState({ agree: !st.agree, err: false }),
      submit: () => st.agree ? this.setState({ sent: true, err: false }) : this.setState({ err: true }),
      closeOk: () => this.setState({ sent: false, agree: false })
    };'''

def logic(init='{}',extra='const extra = {};'):
    return '''class Component extends DCLogic {
  constructor(props) { super(props); this.state = Object.assign({ scale: 1 }, '''+init+'''); }
  renderVals() {
    const s = this.state.scale; const st = this.state;
    const base = { scale: s, szS: s < 1 ? 'on' : '', szM: s === 1 ? 'on' : '', szL: s > 1 ? 'on' : '',
      setS: () => this.setState({ scale: 0.9 }), setM: () => this.setState({ scale: 1 }), setL: () => this.setState({ scale: 1.12 }) };
    '''+extra+'''
    return Object.assign(base, extra);
  }
}'''

def page(fname,title,active,body,js,h):
    html='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>'''+title+''' · LO-CARB</title>
<script src="./support.js"></script>
<link rel="stylesheet" href="'''+CSS+'''">
</head>
<body>
<x-dc>
<helmet>
<style>
body{margin:0;background:#F3F0DF}
a{color:#0B7A3E}a:hover{color:#0E0E0C}
</style>
</helmet>
<div class="lc" id="page-top" style="--s: {{scale}}">
'''+navfor(active)+'''

'''+body+'''

'''+foot+'''
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1440,"height":'''+str(h)+'''}}'>
'''+js+'''
</script>
</body>
</html>
'''
    open(ROOT+fname,'w').write(html)

def phero(cr,lab,h1,lead,right='',btns=''):
    return '''<section class="phero">
<div class="wrap">
'''+crumbs(cr)+'''
<div class="pgrid">
<div>'''+label(lab)+'''<h1 class="display ph1 rise">'''+h1+'''</h1></div>
<div class="rise d2"><p class="lead muted" style="font-size:calc(18px*var(--s))">'''+lead+'''</p>'''+btns+right+'''</div>
</div>
</div>
</section>'''

def btns(*bs):
    out='<div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:28px">'
    for i,(t,h) in enumerate(bs):
        out+= '<a href="%s" class="btn %s">%s%s</a>'%(h,'btn-p' if i==0 else 'btn-od',t,' '+AR if i==0 else '')
    return out+'</div>'

def items(lst,cols='cols3'):
    out='<div class="%s">'%cols
    for k,t,p in lst:
        out+='<div class="item rv"><span class="ii">%s</span><h3>%s</h3><p>%s</p></div>'%(ic(k),t,p)
    return out+'</div>'

def steps(lst):
    out='<div class="svc">'
    for i,(t,p) in enumerate(lst):
        out+='<div class="ss rv"><span class="sn">%02d</span><h3>%s</h3><p>%s</p></div>'%(i+1,t,p)
    return out+'</div>'

def banner(txt):
    return '''<section class="banner">
<div class="ring" style="width:520px;height:520px" aria-hidden="true"></div><div class="ring" style="width:880px;height:880px" aria-hidden="true"></div>
<div class="wrap rv">'''+label('IFRS Sustainability Alliance',True).replace('class="label"','class="label" style="justify-content:center;color:#8FE3B0"',1).replace(' style="color:#8FE3B0"','',1)+'''<h2 class="display">'''+txt+'''</h2></div>
</section>'''

def pteaser(cv,cat,title,num,numtxt,href='Blog-Story.dc.html'):
    return '''<a href="'''+href+'''" class="pteaser rv">
<span class="cv '''+cv+'''"><span class="cvl">Portfolio</span></span>
<div><span class="cat">'''+cat+'''</span><h3 class="ptitle2">'''+title+'''</h3>
<div class="resnum"><b>'''+num+'''</b><span>'''+numtxt+'''</span></div>
<span class="tlink" style="margin-top:20px">Read the story '''+AR+'''</span></div>
</a>'''

DATES=['14 Oct 2026','2 Oct 2026','19 Sep 2026','5 Sep 2026','22 Aug 2026','8 Aug 2026','25 Jul 2026','11 Jul 2026']
DI=[0]
def nd():
    DI[0]+=1; return DATES[DI[0]%len(DATES)]
def related(posts):
    out='<div class="postgrid">'
    for cv,cat,t,h in posts:
        out+='<a href="%s" class="pc rv"><span class="cv %s"></span><span class="cat">%s</span><span class="t">%s</span><span class="pmeta">%s</span></a>'%(h,cv,cat,t,nd())
    return out+'</div>'

def sec(cls,inner):
    return '<section class="psec %s"><div class="wrap">%s</div></section>'%(cls,inner)

def sechead(lab,h2,p='',link=None,dark=False):
    r=''
    if p: r='<p class="p %s" style="max-width:42ch;font-size:calc(17px*var(--s))%s">%s</p>'%('' if dark else 'muted',';color:#CFDCCF' if dark else '',p)
    if link: r='<a href="%s" class="tlink"%s>%s %s</a>'%(link[1],' style="color:#8FE3B0"' if dark else '',link[0],AR)
    return '<div class="sechead rv"><div>%s<h2 class="display h2" style="max-width:18ch">%s</h2></div>%s</div>'%(label(lab,dark),h2,r)

pages=[]

# ---------- ABOUT (v2: sub-nav, alternating bands, BD content) ----------
HAND_CUT='/_blob/422c6a2d434ec3a30444b8bfad18717f'
def asub(active):
    L=[('About-Story.dc.html',"LO-CARB's story"),('About-Certificates.dc.html','Certificates'),('About-Board.dc.html','Board of directors')]
    return '<nav class="asub" aria-label="About Us">'+''.join('<a href="%s"%s>%s</a>'%(h,' class="on" aria-current="page"' if h==active else '',n) for h,n in L)+'</nav>'
def ahero(cr,lab,h1,lead,active,vis=''):
    return '''<section class="ahero">
<div class="wrap">
'''+crumbs(cr)+'''
<div class="ahero-grid">
<div class="ahero-copy">'''+label(lab)+'''<h1 class="display ah1 rise">'''+h1+'''</h1><p class="ahero-lead rise d2">'''+lead+'''</p>'''+asub(active)+'''</div>
'''+vis+'''
</div>
</div>
<svg class="acurve" viewBox="0 0 1440 116" preserveAspectRatio="none" aria-hidden="true"><path d="M0 116H1440V44C1080 120 360 120 0 44Z" fill="CURVEFILL"></path></svg>
</section>'''
ACTA=lambda p: pcta('Read our blog or <span class="it" style="color:#8FE3B0">talk</span> to us',p,'Contact Us','Contact.dc.html','Read our blog','Blog.dc.html')

# ---------- ABOUT: STORY ----------
vis='''<div class="ahero-vis rise d2" aria-hidden="true"><span class="ahero-glow"></span><img src="'''+HAND_CUT+'''" alt=""><span class="aseal"><small>Est.</small><b>2021</b><span>Bangkok</span></span></div>'''
body=ahero([('About Us','About-Story.dc.html'),("LO-CARB's story",None)],'About LO-CARB','Our <span class="it" style="color:var(--forest)">story</span>',
 'Founded in 2021, LO-CARB is a sustainability consultancy that sees sustainability as the heart of business, not a trend or CSR. We combine science, technology and business to help Thai organizations cut emissions, meet global standards and grow.','About-Story.dc.html',vis).replace('CURVEFILL','#000000')
# Mission — black band
body+='''<section class="amission"><div class="wrap amission-grid">
<div class="rv">'''+label('Mission',True)+'''<p class="amission-h">We put the world <span class="it">on a carbon diet.</span></p></div>
<p class="amission-p rv2">We map a clear path to lower emissions while driving business performance, for organizations from the public to the private sector, large and small.</p>
</div></section>'''
# Milestones — horizontal timeline
MS=[('2021','LO-CARB founded',False),('[Year]','Launched CarbonCal and Carbon Camp',True),('2026',"Became Thailand’s first IFRS Sustainability Alliance member",False),('[Year]','[Other milestone]',True)]
body+='''<section class="psec amile"><div class="wrap">'''+sechead('Milestones','How we got here')+'''<ol class="atl" role="list">'''+''.join('<li class="rv%s"><span class="atl-dot" aria-hidden="true"></span><b>%s</b><p>%s</p></li>'%(' tbc' if tbc else '',y,h) for y,h,tbc in MS)+'''</ol></div></section>'''
# We believe — sand
body+='''<section class="psec sand abelieve"><div class="wrap abelieve-grid">
<div class="rv">'''+label('We believe')+'''<p class="abelieve-h"><span class="aq" aria-hidden="true">“</span>Sustainability is the new <span class="it">growth core.</span></p></div>
<p class="abelieve-p rv2">We don’t see it as a trend or CSR, but as the heart of the business: it drives performance, reduces risk, meets customer demand and opens local and global opportunities.</p>
</div></section>'''
# 3 DNAs
DNA=[('growth','Sustainability-rooted','We understand each sector’s challenges and find the smoothest path to transformation.'),('bolt','Technology-driven','We use technology to solve problems more efficiently than traditional methods.'),('story','Creative thinkers','We make sustainability simple, relevant and practical.')]
body+='''<section class="psec adna"><div class="wrap">'''+sechead('Our DNA','Three things that make LO-CARB')+'''<ol class="adna-g" role="list">'''+''.join('<li class="rv"><div class="adna-top"><span class="adna-n">0%d</span><span class="adna-ic">%s</span></div><h3>%s</h3><p>%s</p></li>'%(i+1,ic(k,24),h,d) for i,(k,h,d) in enumerate(DNA))+'''</ol></div></section>'''
# Key numbers — green band
KN=['clients across 5 sectors','organizations using CarbonCal','tCO₂e measured','people trained through Carbon Camp','years in sustainability consulting']
body+='''<section class="anum"><div class="wrap">'''+label('Key numbers')+'''<h2 class="display h2 anum-h">LO-CARB in numbers</h2><ul class="anum-g" role="list">'''+''.join('<li class="rv"><b>[x]</b><span>%s</span></li>'%k for k in KN)+'''</ul><p class="anum-note">Figures to be confirmed by LO-CARB.</p></div></section>'''
body+=ACTA('See how we think about IFRS and carbon, or tell us what you need.')
page('About-Story.dc.html',"LO-CARB's story",'about',body,logic(),4300); pages.append(('About-Story.dc.html',"About · Story",4300,'about'))

# ---------- ABOUT: CERTIFICATES ----------
def certimg(txt): return '<span class="acert-img" aria-hidden="true"><span class="acert-paper"><i></i><i></i><i></i><em>%s</em></span></span>'%txt
body=ahero([('About Us','About-Story.dc.html'),('Certificates',None)],'Credentials','Our <span class="it" style="color:var(--forest)">certificates</span>','The standards and memberships behind our work. Each certificate opens as a PDF.','About-Certificates.dc.html').replace('CURVEFILL','#F3F0DF')
body+='''<section class="psec acert"><div class="wrap">
<article class="acert-feat rv">
<div class="acert-feat-l"><span class="acert-logo">Official logo</span></div>
<div class="acert-feat-r">
<span class="acert-tag">Thailand’s 1st</span>
<h2 class="acert-feat-h">Thailand’s 1<em>st&#8203;</em> IFRS Sustainability Alliance &amp; ISSB Training Partner</h2>
<p class="acert-feat-p">Direct connection to the standard setter &amp; IFRS community</p>
<div class="acert-meta"><span><small>Issued by</small><b>IFRS Foundation</b></span><span><small>Year</small><b>[Year]</b></span></div>
<a href="#pdf" class="btn btn-l">View PDF '''+UP+'''</a>
</div>
</article>
<ul class="acert-g" role="list">'''
CERTS=[('ISO','ISO','[ISO standard to confirm]','[Issuer]'),('ISSB Training Partner','ISSB','Thailand’s first ISSB training partner','[Issuer]'),('CFO','CFO','Carbon Footprint for Organization','TGO'),('BSI (CBAM)','BSI','Carbon Border Adjustment Mechanism','BSI')]
body+=''.join('''<li class="acert-c rv">'''+certimg(img)+'''<div class="acert-b"><h3>%s</h3><p>%s</p><div class="acert-meta"><span><small>Issued by</small><b>%s</b></span><span><small>Year</small><b>[Year]</b></span></div><a href="#pdf" class="acert-pdf">View PDF '''%(n,d,iss)+UP+'''</a></div></li>''' for n,img,d,iss in CERTS)
body+='''</ul><p class="anote2">Certificate images and PDFs to be added from LO-CARB’s shared drive.</p></div></section>'''
body+=ACTA('Want to know how these credentials apply to your project?')
page('About-Certificates.dc.html','Certificates','about',body,logic(),2900); pages.append(('About-Certificates.dc.html','About · Certificates',2900,'about'))

# ---------- ABOUT: BOARD ----------
LI='<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM9 9h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1V21h-4v-5.5c0-1.3-.02-3-1.83-3-1.83 0-2.11 1.43-2.11 2.9V21H9z"></path></svg>'
def bcard(ini,name,role,bio):
    return '''<li class="abm rv"><span class="abm-ph"><svg class="sil" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="36" r="19" fill="currentColor"></circle><path d="M12 100c0-23 17-38 38-38s38 15 38 38z" fill="currentColor"></path></svg><span class="abm-ini">%s</span></span><div class="abm-b"><h3>%s</h3><small>%s</small><p>%s</p><a href="#linkedin" class="abm-li" aria-label="%s on LinkedIn">'''%(ini,name,role,bio,name)+LI+'''</a></div></li>'''
body=ahero([('About Us','About-Story.dc.html'),('Board of directors',None)],'Leadership','Board of <span class="it" style="color:var(--forest)">directors</span>','The people who set LO-CARB’s direction and stand behind our work.','About-Board.dc.html').replace('CURVEFILL','#F3F0DF')
body+='''<section class="psec aboard"><div class="wrap"><ul class="abm-g" role="list">'''+bcard('AC','Arthit Chaem-Choi','Co-Founder','[One-line bio]')+bcard('—','[Name]','[Title]','[One-line bio]')+bcard('—','[Name]','[Title]','[One-line bio]')+bcard('—','[Name]','[Title]','[One-line bio]')+'''</ul>
<div class="note">'''+ic('info',20)+'''<span>Names and photos are published with each director’s consent under the Personal Data Protection Act (PDPA).</span></div></div></section>'''
body+=ACTA('Partners and advisers are welcome to reach the team directly.')
page('About-Board.dc.html','Board of directors','about',body,logic(),2600); pages.append(('About-Board.dc.html','About · Board',2600,'about'))

# ---------- SERVICE PAGES ----------
def service(fname,title,crumb,lab,h1,lead,cta,whatlab,whath2,whatp,whatitems,showbanner,stephead,stepsl,pt,blogposts,formsol,h):
    body=phero([('Our Solutions','Main.dc.html'),(crumb,None)],lab,h1,lead,btns((cta,'#form'),('See how it works','#how')))
    body+=sec('', sechead(whatlab,whath2,whatp)+items(whatitems,'cols2' if len(whatitems)==2 else 'cols3'))
    if showbanner: body+=banner("Thailand’s 1<span class=\"it\" style=\"color:#8FE3B0\">st&#8203;</span> IFRS Sustainability Alliance &amp; ISSB Training Partner")
    body+='<section class="psec sand" id="how"><div class="wrap">'+sechead('How it works',stephead)+steps(stepsl)+'</div></section>'
    body+=sec('', sechead('Client story','Client results','',('All client stories','Blog-Portfolio.dc.html'))+pt)
    body+=sec('tight', sechead('From the blog','Read more on this topic','',('View all posts','Blog.dc.html'))+related(blogposts))
    body+='<section class="psec sand" id="form"><div class="wrap">'+sechead('Get in touch',cta,'Fill in the form and the right specialist will reply.')+inline_form(formsol)+'</div></section>'
    page(fname,title,'solutions',body,logic('{ agree: false, sent: false, err: false }',FORM_JS),h)
    pages.append((fname,'Solution · '+crumb,h,'sol'))

service('Solution-IFRS.dc.html','IFRS Standards','IFRS Standards','Solution · Service',
 'IFRS S1 &amp; S2, <span class="it" style="color:#0B7A3E">end to end</span>',
 'End-to-end IFRS S1/S2 support, from gap analysis and climate risk and financial impact assessment to your first disclosure.',
 'Talk to an IFRS specialist','What is IFRS S1 / S2','Two standards, in plain words','Thai listed companies are moving to ISSB-based disclosure in phases. We check the latest SEC Thailand timeline for your company in the first meeting.',
 [('doc','IFRS S1','General requirements for disclosing sustainability-related financial information: the risks and opportunities that could affect your company\'s prospects.'),('growth','IFRS S2','Climate-related disclosures: how climate risks and opportunities affect your strategy, finances and targets, including greenhouse gas emissions.')],
 True,'One-stop service in six steps',
 [('Gap analysis','Where you stand today against S1 and S2.'),('Gap closing','Fix governance, data and process gaps.'),('Climate risk &amp; opportunity','Scenario-based assessment of what climate means for you.'),('Financial impact','Translate climate risks into the numbers investors read.'),('Reporting','Your IFRS-aligned sustainability disclosure.'),('Capacity building','Train your team to run it next year.')],
 pteaser('cv1','Portfolio · IFRS','[Client name]: IFRS S1 &amp; S2 readiness in [X] weeks','[X]','weeks from gap analysis to a board-approved disclosure'),
 [('cv2','Knowledge base','What IFRS S2 means for SET-listed companies','Blog-Article.dc.html'),('cv4','Knowledge base','IFRS S1 vs S2: what each standard asks for','Blog-Article.dc.html'),('cv6','Knowledge base','Climate scenario analysis for first-time reporters','Blog-Article.dc.html')],
 'IFRS Standards',5600)

service('Solution-ISSB.dc.html','ISSB training','ISSB training','Solution · Service',
 'ISSB <span class="it" style="color:#0B7A3E">training</span>',
 'Hands-on ISSB reporting training from Thailand\'s first ISSB training partner.',
 'Plan a workshop','Who it is for','Training for every level',' ',
 [('board','Board &amp; executives','Briefings on what ISSB means for governance, risk and strategy.'),('users','Management','Sessions for finance, IR and sustainability leads who own the disclosure.'),('cap','Reporting team','Hands-on workshops on S1 and S2 data, calculations and drafting.')],
 True,'From brief to follow-up',
 [('Needs check','We learn where your team is today.'),('Tailored programme','Half-day or full-day, on-site or online, in Thai or English.'),('Delivery','On-site or online sessions led by LO-CARB specialists.'),('Follow-up','Q&amp;A and materials your team keeps.')],
 pteaser('cv5','Portfolio · ISSB training','[Client name]: ISSB training for the board and reporting team','[X]','directors and managers trained'),
 [('cv4','Knowledge base','What boards need to know about ISSB','Blog-Article.dc.html'),('cv2','Knowledge base','IFRS S1 vs S2: what each standard asks for','Blog-Article.dc.html'),('cv3','News &amp; events','ISSB for Boards workshop, Bangkok · 21 Nov 2026','Blog-Article.dc.html')],
 'ISSB training',5000)

service('Solution-Reporting.dc.html','Sustainability reporting & consulting','Reporting &amp; consulting','Solution · Service',
 'Reporting <span class="it" style="color:#0B7A3E">&amp;</span> consulting',
 'Sustainability and ESG reports and strategy that meet GRI, CDP and other standards, through to your Net Zero pathway, led by our specialist team.',
 'Talk to us','What we cover','From materiality assessment to a published report','',
 [('rep','Sustainability &amp; ESG reports','Reports that meet GRI, CDP and other standards.'),('target','ESG strategy','Strategy and materiality that set what to report and what to improve.'),('growth','Net Zero pathway','A target and roadmap to Net Zero, led by our specialist team.')],
 False,'How a reporting project runs',
 [('Materiality assessment','Agree the topics to report.'),('Data collection','Gather and check the numbers.'),('Drafting','Write the report with your team.'),('Review','Internal and external review before sign-off.'),('Disclosure','Publish and file with confidence.'),('Assurance support','Get ready for limited assurance by a third party.')],
 pteaser('cv7','Portfolio · Reporting','[Client name]: a first sustainability report in one cycle','[X]%','of material topics backed by verified data'),
 [('cv4','Knowledge base','Five common gaps in first sustainability reports','Blog-Article.dc.html'),('cv2','Knowledge base','What IFRS S2 means for SET-listed companies','Blog-Article.dc.html'),('cv8','Knowledge base','Double materiality, explained','Blog-Article.dc.html')],
 'Reporting &amp; consulting',5200)

# ---------- PRODUCT PAGES ----------
UIM={'Solution-CarbonCal.dc.html':[
'<div class="ui"><div class="uh"><span><i></i>CarbonCal · Overview</span><span>FY2025</span></div><div class="ub"><div class="kpis"><div class="kpi"><small>Scope 1</small><b>4,210</b></div><div class="kpi"><small>Scope 2</small><b>6,870</b></div><div class="kpi"><small>Scope 3</small><b>7,340</b></div></div><div class="bars"><div style="height:46%"></div><div style="height:62%"></div><div style="height:54%"></div><div style="height:78%"></div><div class="hi" style="height:66%"></div><div class="hi" style="height:52%"></div><div class="hi" style="height:40%"></div></div></div></div>',
'<div class="ui"><div class="uh"><span><i></i>Progress vs target</span><span>2022–2030</span></div><div class="ub"><table><tr><td>Bangkok HQ</td><td style="width:45%"><div class="meter"><i style="width:72%"></i></div></td><td><span class="st ok">On track</span></td></tr><tr><td>Chonburi plant</td><td><div class="meter"><i style="width:48%"></i></div></td><td><span class="st pd">Watch</span></td></tr><tr><td>Rayong depot</td><td><div class="meter"><i style="width:81%"></i></div></td><td><span class="st ok">On track</span></td></tr><tr><td>Khon Kaen DC</td><td><div class="meter"><i style="width:30%"></i></div></td><td><span class="st lt">Behind</span></td></tr></table></div></div>',
'<div class="ui"><div class="uh"><span><i></i>Reports</span><span>3 ready</span></div><div class="ub"><table><tr><td><b>IFRS S2 metrics pack</b></td><td>PDF · XLSX</td><td><span class="st ok">Ready</span></td></tr><tr><td><b>56-1 One Report data</b></td><td>XLSX</td><td><span class="st ok">Ready</span></td></tr><tr><td><b>Buyer questionnaire</b></td><td>CSV</td><td><span class="st ok">Ready</span></td></tr><tr><td><b>Board summary Q3</b></td><td>PDF</td><td><span class="st pd">Draft</span></td></tr></table></div></div>',
'<div class="ui"><div class="uh"><span><i></i>Team</span><span>12 members</span></div><div class="ub"><table><tr><td><b>[Name]</b></td><td>Admin</td><td><span class="st ok">Active</span></td></tr><tr><td><b>[Name]</b></td><td>Approver</td><td><span class="st ok">Active</span></td></tr><tr><td><b>Chonburi plant</b></td><td>Data owner</td><td><span class="st pd">Invited</span></td></tr><tr><td><b>Rayong depot</b></td><td>Data owner</td><td><span class="st ok">Active</span></td></tr></table></div></div>'],
'Solution-CarbonScout.dc.html':[
'<div class="ui"><div class="uh"><span><i></i>Plots</span><span>Sample data</span></div><div class="ub"><table><tr><td><b>Plot A-01</b></td><td>Rubber</td><td>12.4 ha</td></tr><tr><td><b>Plot A-02</b></td><td>Oil palm</td><td>8.9 ha</td></tr><tr><td><b>Plot B-07</b></td><td>Durian</td><td>5.2 ha</td></tr><tr><td><b>Plot C-03</b></td><td>Rubber</td><td>15.0 ha</td></tr></table></div></div>',
'<div class="ui"><div class="uh"><span><i></i>Field measurements</span><span>Sample data</span></div><div class="ub"><table><tr><td>Plot A-01</td><td>Tree survey</td><td><span class="st ok">Done</span></td></tr><tr><td>Plot A-02</td><td>Soil sample</td><td><span class="st ok">Done</span></td></tr><tr><td>Plot B-07</td><td>Tree survey</td><td><span class="st pd">Scheduled</span></td></tr><tr><td>Plot C-03</td><td>Photo evidence</td><td><span class="st pd">Pending</span></td></tr></table></div></div>',
'<div class="ui"><div class="uh"><span><i></i>Carbon stock over time</span><span>tCO₂e · sample</span></div><div class="ub"><div class="bars"><div style="height:34%"></div><div style="height:42%"></div><div style="height:51%"></div><div style="height:60%"></div><div class="hi" style="height:70%"></div><div class="hi" style="height:79%"></div></div></div></div>',
'<div class="ui"><div class="uh"><span><i></i>Verification pack</span><span>Sample data</span></div><div class="ub"><table><tr><td><b>Plot boundaries</b></td><td>KML</td><td><span class="st ok">Ready</span></td></tr><tr><td><b>Measurement records</b></td><td>XLSX</td><td><span class="st ok">Ready</span></td></tr><tr><td><b>Photo evidence</b></td><td>ZIP</td><td><span class="st pd">In progress</span></td></tr></table></div></div>'
]}

FAQ_JS_TMPL='''const F = %s;
    %s
    const extra2 = { faqs: F.map((f, i) => ({ q: f.q, a: f.a, open: st.faq === i, cls: st.faq === i ? 'open' : '', exp: st.faq === i ? 'true' : 'false', toggle: () => this.setState({ faq: st.faq === i ? -1 : i }) })) };
    Object.assign(extra, extra2);'''
def product(fname,title,crumb,h1,lead,b1,b2,benefits,stats,features,testis,faqs,extra_section,formsol,h):
    body=phero([('Our Solutions','Main.dc.html'),(crumb,None)],'Solution · Platform',h1,lead,btns((b1,'#form'),(b2,'#form')))
    body+=sec('', sechead('Why teams choose it','Benefits')+items(benefits))
    body+='<section class="psec green tight"><div class="wrap"><div class="outnum">'+''.join('<div class="rv"><b>%s</b><span>%s</span></div>'%x for x in stats)+'</div></div></section>'
    fr=''.join('<div class="frow rv"><div><span class="fnum">%02d</span><h3>%s</h3><p>%s</p></div><div class="fvis">%s</div></div>'%(i+1,t,p,UIM[fname][i]) for i,(t,p) in enumerate(features))
    body+=sec('', sechead('Key features','What you can do')+'<div>'+fr+'</div>')
    body+=extra_section
    body+='<section class="psec ink"><div class="wrap">'+sechead('Testimonials','What clients say','',None,True)+'<div class="tgrid">'+''.join('<div class="tq rv"><p>“%s”</p><div class="qby"><span class="av2">%s</span><div><b style="color:#F3F0DF">%s</b><span style="color:#B9B6A3">%s</span></div></div></div>'%x for x in testis)+'</div></div></section>'
    body+=sec('', sechead('FAQ','Questions we hear often')+'''<div class="faq"><sc-for list="{{faqs}}" as="f" hint-placeholder-count="3"><div class="fq {{f.cls}}"><button onClick="{{f.toggle}}" aria-expanded="{{f.exp}}">{{f.q}}<span class="pl"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"></path></svg></span></button><sc-if value="{{f.open}}" hint-placeholder-val="{{ false }}"><p class="ans">{{f.a}}</p></sc-if></div></sc-for></div>''')
    body+='<section class="psec sand" id="form"><div class="wrap">'+sechead('Get started',b1,'Tell us a little about your company and we will set you up.')+inline_form(formsol)+'</div></section>'
    js=logic('{ agree: false, sent: false, err: false, faq: 0 }',FAQ_JS_TMPL%(json.dumps(faqs),FORM_JS))
    page(fname,title,'solutions',body,js,h)
    pages.append((fname,'Solution · '+crumb,h,'sol'))

camp=sec('sand', '<div class="pgrid mid"><div class="rv">'+label('Carbon Camp')+'<h2 class="display h2" style="max-width:14ch">Training so your team can <span class="it" style="color:#0B7A3E">run it</span></h2><p class="lead muted" style="margin-top:24px;font-size:calc(17px*var(--s))">Carbon Camp is hands-on training that comes with CarbonCal: your team learns carbon accounting by doing it on your own data.</p></div><div class="rv2">'+steps([('Kick-off','Set goals and scope.'),('Hands-on sessions','Work through your own data in CarbonCal.'),('Wrap-up','Certificate of completion and a 30-day follow-up check-in.')]).replace('class="svc"','class="svc" style="grid-template-columns:minmax(0,1fr);row-gap:32px"')+'</div></div>')
product('Solution-CarbonCal.dc.html','CarbonCal + Carbon Camp','CarbonCal + Carbon Camp',
 'Carbon<span class="it" style="color:#0B7A3E">Cal</span> + Carbon Camp','Measure Scope 1, 2 and 3 emissions on one easy, accurate platform, so your carbon footprint for organization (CFO) is ready for disclosure and TGO registration, with training that brings your team on board.','Request free trial','Book a demo',
 [('layers','Scope 1, 2 and 3 on one platform','Measure all three scopes on one easy, accurate platform.'),('cert','CFO ready for TGO registration','Your carbon footprint for organization (CFO) is ready for disclosure and TGO registration.'),('cap','Training with Carbon Camp','Hands-on training that brings your team on board.')],
 [('[X]','companies'),('[X]','users'),('[X]','tCO₂e measured')],
 [('Measure Scope 1–3','Enter or import fuel, electricity, travel and purchase data. CarbonCal applies the right factor and shows the result by scope.'),('Track progress over time','See monthly trends against your baseline and reduction targets, site by site.'),('Share reports','Export board-ready summaries and data tables for IFRS S2, 56-1 One Report and buyer questionnaires.'),('Invite your team','Give each site its own data owner and keep every change logged for auditors.')],
 [('[Client quote, pending approval]','SK','[Name]','Sustainability Manager, [Client name]'),('[Client quote, pending approval]','WT','[Name]','CFO, [Client name]'),('[Client quote, pending approval]','PJ','[Name]','Operations Director, [Client name]')],
 [{'q':'How much does CarbonCal cost?','a':'Pricing depends on the number of sites and users. [Pricing and free-trial terms to confirm with the product team.]'},{'q':'How is our data kept secure?','a':'Access is role-based for data owners, reviewers and approvers. [Encryption, hosting and data-retention details to confirm with the product team.]'},{'q':'What support do we get?','a':'Carbon Camp onboarding helps your team run CarbonCal on its own. [Support channels and hours to confirm.]'}],
 camp,'CarbonCal + Carbon Camp',6400)

product('Solution-CarbonScout.dc.html','Carbon Scout','Carbon Scout',
 'Carbon <span class="it" style="color:#0B7A3E">Scout</span>','Track and verify carbon on farmland and plantations, ready for carbon credits.','Book a demo','Talk to us',
 [('growth','Carbon on every plot','Map farmland and plantation plots and follow their carbon over time.'),('shield','Verification-ready data','Keep measurements and evidence organised for third-party verification.'),('target','A path to carbon credits','Prepare project data for carbon credit programmes.')],
 [('[X]','hectares tracked'),('[X]','plots'),('[X]','tCO₂e estimated')],
 [('Plot mapping','Register each plot with its boundary, crop and area.'),('Field measurements','Plan and record field surveys, samples and photo evidence.'),('Carbon over time','See how carbon on each plot changes, season by season.'),('Verification pack','Export plot data and evidence for verifiers and carbon credit programmes.')],
 [('[Client quote, pending approval]','PJ','[Name]','Sustainability Manager, [Client name]'),('[Client quote, pending approval]','KR','[Name]','Plantation Manager, [Client name]'),('[Client quote, pending approval]','NW','[Name]','[Title], [Client name]')],
 [{'q':'Which crops and land types does Carbon Scout cover?','a':'Farmland and plantations. [Confirm the supported crop list with the product team.]'},{'q':'Does Carbon Scout issue carbon credits?','a':'No. Carbon Scout prepares tracked and verified data for carbon credit programmes; credits are issued by the programme operator.'},{'q':'How is plot data collected?','a':'[Data collection method to confirm with the product team.]'}],
 '','Carbon Scout',5600)

# ---------- BLOG HUB + CATEGORIES ----------
POSTS=[
 {'cv':'cv1','cat':'Portfolio','tag':'IFRS','t':'[Client name]: IFRS S1 & S2 readiness in [X] weeks','h':'Blog-Story.dc.html','d':'14 Oct 2026'},
 {'cv':'cv4','cat':'Knowledge base','tag':'IFRS','t':'What IFRS S2 means for SET-listed companies','h':'Blog-Article.dc.html','d':'2 Oct 2026'},
 {'cv':'cv2','cat':'Portfolio','tag':'CarbonCal','t':'[Client name]: measuring Scope 1–3 with CarbonCal','h':'Blog-Story.dc.html','d':'19 Sep 2026'},
 {'cv':'cv7','cat':'Knowledge base','tag':'IFRS','t':'IFRS S1 vs S2: what each standard asks for','h':'Blog-Article.dc.html','d':'12 Sep 2026'},
 {'cv':'cv3','cat':'News & events','tag':'ISSB','t':'ISSB for Boards workshop returns to Bangkok on 21 Nov','h':'Blog-Article.dc.html','d':'5 Sep 2026'},
 {'cv':'cv6','cat':'Portfolio','tag':'Carbon Scout','t':'[Client name]: tracking plantation carbon with Carbon Scout','h':'Blog-Story.dc.html','d':'28 Aug 2026'},
 {'cv':'cv5','cat':'Knowledge base','tag':'CarbonCal','t':'Scope 1, 2 and 3 emissions explained','h':'Blog-Article.dc.html','d':'22 Aug 2026'},
 {'cv':'cv8','cat':'Portfolio','tag':'Reporting','t':'[Client name]: a first sustainability report in one cycle','h':'Blog-Story.dc.html','d':'8 Aug 2026'},
 {'cv':'cv2','cat':'News & events','tag':'Carbon Scout','t':'LO-CARB and [Client name] team up on farmland carbon','h':'Blog-Article.dc.html','d':'1 Aug 2026'},
 {'cv':'cv1','cat':'Knowledge base','tag':'CarbonCal','t':'How to start collecting Scope 3 supplier data','h':'Blog-Article.dc.html','d':'25 Jul 2026'},
 {'cv':'cv4','cat':'Portfolio','tag':'ISSB','t':'[Client name]: ISSB training for the board','h':'Blog-Story.dc.html','d':'18 Jul 2026'},
 {'cv':'cv7','cat':'News & events','tag':'CarbonCal','t':'CarbonCal adds Scope 3 category templates','h':'Blog-Article.dc.html','d':'11 Jul 2026'}]
TAGS=['All','IFRS','CarbonCal','ISSB','Carbon Scout','Reporting']
def bloghub(fname,tab,cat,h1,lead,feat,h):
    tabs=[('All','Blog.dc.html'),('Portfolio','Blog-Portfolio.dc.html'),('Knowledge base','Blog-Knowledge.dc.html'),('News &amp; events','Blog-News.dc.html')]
    tb='<nav class="ftabs" aria-label="Blog categories">'+''.join('<a href="%s"%s>%s</a>'%(hh,' class="on" aria-current="page"' if t==tab else '',t) for t,hh in tabs)+'</nav>'
    cr=[('Blog','Blog.dc.html'),(tab,None)] if tab!='All' else [('Blog',None)]
    body=phero(cr,'Blog',h1,lead)
    inner='<div style="display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap;margin-bottom:64px">'+tb+'<div class="chips"><span class="lb">SOLUTION</span><sc-for list="{{chips}}" as="c" hint-placeholder-count="6"><button class="chip {{c.cls}}" onClick="{{c.pick}}">{{c.label}}</button></sc-for></div></div>'
    if feat:
        inner+='<a href="Blog-Story.dc.html" class="featpost rv"><span class="cv cv1"><span class="cvl">Featured</span></span><div><span class="cat">Portfolio · IFRS</span><h2 class="ptitle2">[Client name]: IFRS S1 &amp; S2 readiness in [X] weeks</h2><p class="p muted" style="margin-top:16px">[Two-line summary of a verified client story, approved by the client.]</p><span class="pmeta" style="display:block;margin-top:16px">14 Oct 2026</span><span class="tlink" style="margin-top:12px">Read the story '+AR+'</span></div></a>'
    inner+='<sc-if value="{{hasPosts}}" hint-placeholder-val="{{ true }}"><div class="postgrid"><sc-for list="{{posts}}" as="p" hint-placeholder-count="6"><a href="{{p.h}}" class="pc"><span class="cv {{p.cv}}"><span class="cvl">{{p.tag}}</span></span><span class="cat">{{p.cat}}</span><span class="t">{{p.t}}</span><span class="pmeta">{{p.d}}</span></a></sc-for></div></sc-if>'
    inner+='<sc-if value="{{noPosts}}" hint-placeholder-val="{{ false }}"><p class="empty">No posts for this solution yet. Try another filter.</p></sc-if>'
    inner+='<nav class="pager" aria-label="Pages"><a href="#" class="pg on">1</a><a href="#" class="pg">2</a><a href="#" class="pg">3</a><a href="#" class="pg">→</a></nav>'
    body+='<section class="psec" style="padding-top:24px"><div class="wrap">'+inner+'</div></section>'
    body+=pcta('Talk to us about a project <span class="it" style="color:#8FE3B0">like these</span>','Tell us your goal and we will point you to the right solution.','Contact Us','Contact.dc.html','Explore solutions','Main.dc.html')
    plist=[p for p in POSTS if cat is None or p['cat']==cat]
    js=logic("{ tag: 'All' }",'''const P = '''+json.dumps(plist)+''';
    const T = '''+json.dumps(TAGS)+''';
    const list = P.filter((p) => st.tag === 'All' || p.tag === st.tag);
    const extra = { chips: T.map((t) => ({ label: t, cls: st.tag === t ? 'on' : '', pick: () => this.setState({ tag: t }) })), posts: list, hasPosts: list.length > 0, noPosts: list.length === 0 };''')
    page(fname,'Blog' if tab=='All' else tab.replace('&amp;','&'),'blog',body,js,h)
    pages.append((fname,'Blog · '+tab.replace('&amp;','&'),h,'blog'))
bloghub('Blog.dc.html','All',None,'Insights &amp; <span class="it" style="color:#0B7A3E">client stories</span>','Client stories, explainers on IFRS, ISSB and carbon, and news from the LO-CARB team.',True,4300)
bloghub('Blog-Portfolio.dc.html','Portfolio','Portfolio','Client <span class="it" style="color:#0B7A3E">stories</span>','Named clients, the challenge they faced and the results they got. Grouped by solution so you can find peers.',False,3500)
bloghub('Blog-Knowledge.dc.html','Knowledge base','Knowledge base','Knowledge <span class="it" style="color:#0B7A3E">base</span>','Plain-language explainers on IFRS S1 &amp; S2, ISSB and carbon accounting.',False,3500)
bloghub('Blog-News.dc.html','News &amp; events','News & events','News &amp; <span class="it" style="color:#0B7A3E">events</span>','Updates, workshops and announcements from LO-CARB.',False,3200)

# ---------- PORTFOLIO STORY (template) ----------
body='''<section class="phero"><div class="wrap">'''+crumbs([('Blog','Blog.dc.html'),('Portfolio','Blog-Portfolio.dc.html'),('[Client name]',None)])+'''
<div class="pgrid">
<div><div style="display:flex;align-items:center;gap:16px;margin-bottom:28px"><span class="cl" style="width:72px;height:72px;border-radius:999px;background:#E9E5CF;color:#0B7A3E;display:flex;align-items:center;justify-content:center;font-family:Termina,sans-serif;font-weight:700;font-size:12px">[LOGO]</span><div><b style="font-family:Termina,sans-serif;font-size:15px;text-transform:uppercase">[Client name]</b><span style="display:block;color:#4A4A42;font-size:14px">[Industry] · [Segment]</span></div></div>
<h1 class="display ph1 rise" style="font-size:calc(clamp(36px,4.2vw,68px)*var(--s))">[Headline result, approved by the client]</h1></div>
<div class="rise d2"><div class="tagrow"><span class="tag g">IFRS Standards</span><span class="tag">Portfolio</span></div><p class="pmeta" style="margin-top:16px">14 Oct 2026</p></div>
</div></div></section>
<div class="wrap"><span class="cv cv4 rv" style="aspect-ratio:21/9;border-radius:28px"></span></div>
'''+sec('', '''<div class="art"><div class="prose">
<h2>The challenge</h2><p>[The challenge: what the client needed and why it was hard. Verified case content, approved by the client.]</p>
<h2>The solution</h2><p>We ran the six-step <a href="Solution-IFRS.dc.html">IFRS Standards</a> service: from gap analysis to disclosure. [Project details to confirm.]</p><p>[How the platform and training were used. Verified case content.]</p>
</div><aside class="aside"><div class="box"><small>Client</small><b style="font-family:Termina,sans-serif">[Client name]</b></div><div class="box"><small>Solutions used</small><div class="tagrow"><a href="Solution-IFRS.dc.html" class="tag g" style="text-decoration:none">IFRS Standards</a></div></div><div class="box"><small>Industry</small><span>[Industry]</span></div></aside></div>''')
body+='<section class="psec green"><div class="wrap">'+sechead('The outcome','Results approved by the client','',None,True)+'<div class="outnum"><div class="rv"><b>[X]</b><span>[Result one, approved by the client]</span></div><div class="rv"><b>[X]</b><span>[Result two, approved by the client]</span></div><div class="rv"><b>[X]</b><span>[Result three, approved by the client]</span></div></div></div></section>'
body+=sec('', '<div class="pgrid mid"><div class="rv">'+label('Client quote')+'<p class="bquote">“[Client quote, pending client approval]”</p><div class="qby"><span class="av2">CP</span><div><b>[Name]</b><span>Chief Financial Officer, [Client name]</span></div></div></div><div class="rv2"><a href="Solution-IFRS.dc.html" class="produse"><span class="ii">'+ic('doc')+'</span><div><small style="font-family:Termina,sans-serif;font-weight:700;font-size:10px;letter-spacing:.14em;color:#0EA552">SOLUTION USED</small><b>IFRS Standards</b><span>S1 &amp; S2 advisory, end to end</span></div><span class="arc">'+UP+'</span></a></div></div>')
body+=pcta('Talk to us about a project <span class="it" style="color:#8FE3B0">like this</span>','IFRS Standards will be pre-selected in the form.','Talk to us','Solution-IFRS.dc.html','More client stories','Blog-Portfolio.dc.html')
body+=sec('tight', sechead('Related stories','More from our clients','',('All client stories','Blog-Portfolio.dc.html'))+related([('cv2','Portfolio · CarbonCal','[Client name]: measuring Scope 1–3 with CarbonCal','Blog-Story.dc.html'),('cv6','Portfolio · Carbon Scout','[Client name]: [X]% supplier response rate','Blog-Story.dc.html'),('cv8','Portfolio · Reporting','[Client name]: a first sustainability report in one cycle','Blog-Story.dc.html')]))
page('Blog-Story.dc.html','Client story','blog',body,logic(),5000); pages.append(('Blog-Story.dc.html','Blog · Portfolio story',5000,'blog'))

# ---------- ARTICLE (template) ----------
body='''<section class="phero"><div class="wrap">'''+crumbs([('Blog','Blog.dc.html'),('Knowledge base','Blog-Knowledge.dc.html'),('Article',None)])+'''
<div style="max-width:960px">'''+label('Knowledge base · IFRS')+'''<h1 class="display ph1 rise" style="font-size:calc(clamp(36px,4.4vw,72px)*var(--s))">What IFRS S2 means for <span class="it" style="color:#0B7A3E">SET-listed</span> companies</h1>
<div style="display:flex;gap:20px;flex-wrap:wrap;align-items:center;margin-top:28px" class="pmeta"><span>2 Oct 2026</span><span>·</span><span>By [Author name]</span></div></div>
</div></section>
<div class="wrap"><span class="cv cv2 rv" style="aspect-ratio:21/9;border-radius:28px"></span></div>
'''+sec('', '''<div class="art"><div>
<div class="takeaway rv">'''+label('Key takeaways')+'''<ul><li>'''+CHK+'''<span>IFRS S2 covers four areas: governance, strategy, risk management, and metrics and targets.</span></li><li>'''+CHK+'''<span>You will need Scope 1, 2 and 3 emissions, plus a view of climate risks under different scenarios.</span></li><li>'''+CHK+'''<span>Start with a gap analysis: most companies already hold part of the data, just not in one place.</span></li></ul></div>
<div class="prose"><h2>What IFRS S2 asks for</h2><p>IFRS S2 is the ISSB's climate standard. It asks companies to explain how climate-related risks and opportunities could affect their cash flows, access to finance and cost of capital.</p><p>Disclosures are grouped into four areas that will look familiar to anyone who has used TCFD: governance, strategy, risk management, and metrics and targets.</p><h2>Why it matters for SET-listed companies</h2><p>Investors increasingly compare companies on the same climate metrics. A clear, consistent disclosure makes it easier for them to price your risk, and harder to overlook your progress.</p>
<div class="inlinecta"><div><b>Need help with IFRS S2?</b><span>Talk to Thailand's first IFRS Sustainability Alliance member.</span></div><a href="Solution-IFRS.dc.html" class="btn btn-l">IFRS Standards '''+AR+'''</a></div>
<h2>Three steps to get ready</h2><p>First, run a gap analysis against the standard. Second, bring emissions data into one inventory that covers all three scopes. Third, agree climate scenarios with the board early, because they shape the rest of the disclosure.</p></div>
<div class="author"><span class="av2">—</span><div><b>[Author name]</b><span>[Author title] at LO-CARB</span></div></div>
</div><aside class="aside"><div class="box"><small>Category</small><span>Knowledge base</span></div><div class="box"><small>Solution</small><div class="tagrow"><a href="Solution-IFRS.dc.html" class="tag g" style="text-decoration:none">IFRS</a></div></div><div class="box"><small>Share</small><div class="social" style="margin-top:0"><a href="#" class="soc" style="color:#0E0E0C;border-color:rgba(14,14,12,.2)">in</a><a href="#" class="soc" style="color:#0E0E0C;border-color:rgba(14,14,12,.2)">f</a></div></div></aside></div>''')
body+=sec('tight', sechead('Related posts','Keep reading','',('View all posts','Blog.dc.html'))+related([('cv4','Knowledge base','IFRS S1 vs S2: what each standard asks for','Blog-Article.dc.html'),('cv1','Portfolio · IFRS','[Client name]: IFRS S1 &amp; S2 readiness in [X] weeks','Blog-Story.dc.html'),('cv6','Knowledge base','Climate scenario analysis for first-time reporters','Blog-Article.dc.html')]))
body+=pcta('Questions about <span class="it" style="color:#8FE3B0">IFRS S2</span>?','Our specialists can tell you what it means for your company.','Talk to us','Contact.dc.html','Explore IFRS services','Solution-IFRS.dc.html')
page('Blog-Article.dc.html','Article','blog',body,logic(),5000); pages.append(('Blog-Article.dc.html','Blog · Article',5000,'blog'))

# ---------- CONTACT ----------
body=phero([('Contact Us',None)],'Contact Us','Let\'s <span class="it" style="color:#0B7A3E">talk</span>','Tell us what you need. Business enquiries go to our team; job applications go straight to HR.')
form='''<div class="formwrap">
<div class="rv">
<sc-if value="{{notSent}}" hint-placeholder-val="{{ true }}">
<div class="form">
<div class="fld full"><span class="flab">I'm contacting about <em>*</em></span><div class="chips"><sc-for list="{{topics}}" as="t" hint-placeholder-count="4"><button class="chip {{t.cls}}" onClick="{{t.pick}}" aria-pressed="{{t.pr}}">{{t.label}}</button></sc-for></div></div>
<sc-if value="{{isSol}}" hint-placeholder-val="{{ false }}"><div class="fld full"><span class="flab">Which solution?</span><div class="chips"><sc-for list="{{sols}}" as="t" hint-placeholder-count="5"><button class="chip {{t.cls}}" onClick="{{t.pick}}" aria-pressed="{{t.pr}}">{{t.label}}</button></sc-for></div></div></sc-if>
<div class="fld"><label for="cn">Name <em>*</em></label><input id="cn" type="text" placeholder="Your full name"></div>
<div class="fld"><label for="ce">Email <em>*</em></label><input id="ce" type="email" placeholder="name@company.com"></div>
<div class="fld"><label for="cc">Company</label><input id="cc" type="text" placeholder="Company name"></div>
<div class="fld"><label for="cp">Position</label><input id="cp" type="text" placeholder="Your role"></div>
<div class="fld full"><label for="ct">Phone</label><input id="ct" type="tel" placeholder="+66"></div>
<sc-if value="{{isCareer}}" hint-placeholder-val="{{ false }}"><div class="fld full"><label for="ci">Short introduction</label><textarea id="ci" placeholder="A few lines about you and the role you are interested in." style="min-height:110px"></textarea></div><div class="fld full"><label for="cl">LinkedIn URL</label><input id="cl" type="url" placeholder="https://linkedin.com/in/"></div></sc-if>
<div class="fld full"><label for="cm">Message</label><textarea id="cm" placeholder="How can we help?"></textarea></div>
<div class="full"><button class="cbx {{agreeCls}}" onClick="{{toggleAgree}}" role="checkbox" aria-checked="{{agreeAria}}"><span class="bx">'''+CHK+'''</span><span>I agree to the <a href="#privacy">privacy policy</a> (PDPA). <em style="font-style:normal;color:#0EA552">*</em></span></button></div>
<sc-if value="{{err}}" hint-placeholder-val="{{ false }}"><p class="ferr full" style="margin:0">{{errMsg}}</p></sc-if>
<div class="full"><button class="btn btn-p" onClick="{{submit}}">Send message '''+AR+'''</button></div>
</div>
</sc-if>
<sc-if value="{{sent}}" hint-placeholder-val="{{ false }}">
<div class="okmsg"><span class="oi">'''+CHK+'''</span><div><b>Thank you</b><p>Your message has been well received.</p></div><button onClick="{{closeOk}}" aria-label="Close message">✕</button></div>
</sc-if>
</div>
<div class="cinfo rv2">
<div class="row2"><small>Your message goes to</small><b>{{route}}</b><span>{{routeNote}}</span></div>
<div class="row2"><small>Business &amp; partnerships</small><b><a href="mailto:contact@locarb.green">contact@locarb.green</a></b><span>Solutions, partnership and other enquiries</span></div>
<div class="row2"><small>Careers</small><b><a href="mailto:hr@locarb.green">hr@locarb.green</a></b><span>Job seekers and interns</span></div>
<div class="row2"><small>Office</small><b>1/3-7, Rooftop, Soi Saladaeng 1 (Godche)</b><span>Silom Subdistrict, Bang Rak District, Bangkok 10500</span></div><div class="row2"><small>Phone</small><b><a href="tel:+66969966249">096 996 6249</a></b><span>contact@locarb.green</span></div>
<div class="row2"><small>Follow us</small><div class="social" style="margin-top:12px"><a href="#" class="soc" style="color:#0E0E0C;border-color:rgba(14,14,12,.2)">in</a><a href="#" class="soc" style="color:#0E0E0C;border-color:rgba(14,14,12,.2)">f</a></div></div>
</div>
</div>'''
body+='<section class="psec" style="padding-top:16px"><div class="wrap">'+form+'</div></section>'
js=logic("{ topic: '', sol: '', agree: false, sent: false, err: false }",'''const TOP = ['Solutions', 'Partnership', 'Careers', 'Other inquiries'];
    const SOL = ['IFRS', 'CarbonCal + Carbon Camp', 'ISSB training', 'Carbon Scout', 'Reporting & consulting'];
    const career = st.topic === 'Careers';
    const extra = {
      topics: TOP.map((t) => ({ label: t, cls: st.topic === t ? 'on' : '', pr: st.topic === t ? 'true' : 'false', pick: () => this.setState({ topic: t, err: false }) })),
      sols: SOL.map((t) => ({ label: t, cls: st.sol === t ? 'on' : '', pr: st.sol === t ? 'true' : 'false', pick: () => this.setState({ sol: t }) })),
      isSol: st.topic === 'Solutions', isCareer: career,
      route: career ? 'hr@locarb.green' : 'contact@locarb.green',
      routeNote: st.topic ? ('Subject: ' + st.topic + (st.topic === 'Solutions' && st.sol ? ' · ' + st.sol : '')) : 'Choose a topic to see where it goes.',
      notSent: !st.sent, sent: !!st.sent, err: !!st.err,
      errMsg: !st.topic ? 'Please choose what you are contacting us about.' : 'Please accept the privacy policy to send your message.',
      agreeCls: st.agree ? 'on' : '', agreeAria: st.agree ? 'true' : 'false',
      toggleAgree: () => this.setState({ agree: !st.agree, err: false }),
      submit: () => (st.topic && st.agree) ? this.setState({ sent: true, err: false }) : this.setState({ err: true }),
      closeOk: () => this.setState({ sent: false, agree: false, topic: '', sol: '' })
    };''')
page('Contact.dc.html','Contact Us',None,body,js,2700); pages.append(('Contact.dc.html','Contact Us',2700,'contact'))

json.dump(pages,open('/tmp/gen/pages.json','w'))
print(len(pages))
