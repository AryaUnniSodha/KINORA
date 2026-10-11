"""Kinora site generator. Run: python build.py  (writes HTML/CSS/JS next to this file)."""
B = "Kinora"
TAG = "Make room for a better tomorrow."
NOTE = "Concept project. Images are AI-generated illustrations, not photographs of real people or programmes. Figures are demo data."
NAV = [("index.html", "Home"), ("index.html#mission", "Our Mission"), ("initiatives.html", "Our Initiatives"),
       ("impact.html", "Our Impact"), ("stories.html", "Stories"), ("about.html", "About Us")]

INIT = [
 ("learning", "Learning Without Limits", "children", "learn", "Reading corners, shared books and patient mentors, so a child's curiosity never waits for a classroom to be built.",
  "Children aged 5-14 and their families", "Learning gaps widen when books, quiet space and a mentor are out of reach.", "Weekly reading circles, a lending shelf, homework mentoring."),
 ("her-next-chapter", "Her Next Chapter", "women", "women", "Skills, savings circles and first-business coaching for women who are ready to earn on their own terms.",
  "Women 18+ starting or restarting work", "Capable women are held back by missing training, credit and networks.", "Digital skills labs, craft and food enterprise coaching, peer savings groups."),
 ("skills", "Skills for Tomorrow", "skills", "skills", "Practical workshops, from solar kits to certificates, that turn learning into something you can use on Monday.",
  "Teens and adults of any background", "Formal schooling rarely teaches the hands-on skills local work needs.", "Short workshops, certificates, career conversations with local professionals."),
 ("stronger-together", "Stronger Together", "community", "together", "Community meals, health information and volunteer-led projects that make a neighbourhood feel like one.",
  "Whole neighbourhoods", "Isolation and scattered services leave people unsure where to turn.", "Community harvests, multilingual information desks, volunteer days."),
]
STORIES = [
 ("A reading circle begins under the mango tree", "children", "learn", "Illustrative story: Meera, 9, wants to read the whole shelf before the monsoon.",
  "Meera is a made-up child used to show how a reading circle might feel. Each Saturday a mentor brings a crate of books. By the third week she is reading aloud to younger children. This is a demonstration, not a real testimonial."),
 ("Three women, one shared stall", "women", "women", "Illustrative story: a savings circle turns a recipe into a stall.",
  "Fictional example. Three neighbours pool small savings, learn to price and keep records, and open a weekend stall. It shows the path Her Next Chapter is designed around, not an achievement we are reporting."),
 ("Solar kits and a first certificate", "skills", "skills", "Illustrative story: a workshop where learning becomes something to hold.",
  "Fictional example. Students assemble a small solar model, explain it to visitors and receive a participation certificate. Concept content for demonstration."),
 ("The information desk that speaks your language", "community", "help", "Illustrative story: a volunteer-run desk answers questions in three languages.",
  "Fictional example. Volunteers staff a desk with health and schooling information in several languages so nobody has to guess where to go. Demonstration only."),
]
PATHS = [("Volunteer your time", "A few steady hours a week at reading circles, community days or events."),
 ("Share your skills", "Teach what you know: coding, accounts, sewing, farming, design."),
 ("Mentor a learner", "A regular, one-to-one conversation with a child or adult learner."),
 ("Support an initiative", "Fund a programme. Demo only: no payments are taken on this site."),
 ("Become a community partner", "Schools, clinics and businesses working alongside us.")]

def img(n, alt, cls="", w=1200, h=630, eager=False):
    return f'<img src="img/{n}.webp" alt="{alt}" width="{w}" height="{h}" class="{cls}" {"fetchpriority=high" if eager else "loading=lazy"}>'

def page(fn, title, desc, body):
    nav = "".join(f'<li><a href="{h}"{" aria-current=page" if h == fn else ""}>{t}</a></li>' for h, t in NAV)
    foot_i = "".join(f'<li><a href="initiatives.html#{i[0]}">{i[1]}</a></li>' for i in INIT)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | {B}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title} | {B}"><meta property="og:description" content="{desc}"><meta property="og:image" content="img/og.jpg">
<link rel="icon" href="favicon.svg"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&family=Young+Serif&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css"></head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><a class="brand" href="index.html" aria-label="{B} home"><svg width="30" height="30" viewBox="0 0 30 30" aria-hidden="true"><path d="M3 27V15a12 12 0 0 1 24 0v12" fill="none" stroke="currentColor" stroke-width="2.5"/><path d="M10 27V16a5 5 0 0 1 10 0v11" fill="#C28A2C"/></svg>{B}</a>
<button class="sbtn" aria-haspopup="dialog">Search</button><button class="burger" aria-expanded="false" aria-controls="menu">Menu</button>
<nav id="menu" aria-label="Main"><ul>{nav}</ul><a class="btn solid" href="get-involved.html">Get Involved</a></nav></header>
<main id="main">{body}</main>
<footer><div class="fgrid"><div><a class="brand" href="index.html">{B}</a><p>We connect people, skills and opportunities so that learning, work and belonging are within reach of everyone.</p></div>
<div><h2>Explore</h2><ul>{nav}<li><a href="contact.html">Contact</a></li></ul></div><div><h2>Initiatives</h2><ul>{foot_i}</ul></div>
<div><h2>Legal</h2><ul><li><a href="privacy.html">Privacy Policy</a></li><li><a href="terms.html">Terms of Use</a></li></ul></div></div>
<p class="note">{NOTE} No contact details or social profiles are listed because none have been verified.</p><p class="note">&copy; 2026 {B} concept project.</p></footer>
<dialog id="sd" aria-label="Search Kinora"><form method="dialog"><label for="sq">Search pages, initiatives and stories</label><input id="sq" type="search" autocomplete="off"><ul id="sr"></ul><p class="demo" id="sh">Press / to search from any page.</p><button class="btn ghost">Close</button></form></dialog>
<script src="app.js"></script></body></html>'''

def banner(t, p, im):
    return f'<section class="pagehead wrap"><div><h1>{t}</h1><p class="lead">{p}</p></div>{img(im, "", "arch small")}</section>'

def form(kind):
    extra = ""
    if kind == "involve":
        extra = '''<label for="type">How would you like to take part?</label><select id="type" name="type" required><option value="">Choose one</option>''' + "".join(f"<option>{p[0]}</option>" for p in PATHS) + '''</select><p class="err" data-for="type"></p>
<label for="hours">Hours you can offer each week (optional)</label><input id="hours" name="hours" type="number" min="0" max="40" inputmode="numeric"><p class="err" data-for="hours"></p>'''
    else:
        extra = '''<label for="type">What is your enquiry about?</label><select id="type" name="type" required><option value="">Choose one</option><option>General question</option><option>Volunteering</option><option>Partnership</option><option>Media</option><option>Feedback</option></select><p class="err" data-for="type"></p>'''
    return f'''<form class="card form" novalidate data-demo><p class="demo">Demonstration form: nothing you type here is sent to anyone.</p>
<label for="name">Full name</label><input id="name" name="name" autocomplete="name" required><p class="err" data-for="name"></p>
<label for="email">Email address</label><input id="email" name="email" type="email" autocomplete="email" required><p class="err" data-for="email"></p>{extra}
<label for="msg">Your message</label><textarea id="msg" name="msg" rows="5" minlength="10" required></textarea><p class="err" data-for="msg"></p>
<button class="btn solid" type="submit">Preview my message</button><div class="ok" role="status" hidden></div></form>'''

P = {}
# ---------- HOME
cards = ""
for i, (slug, t, c, im, d, *_r) in enumerate(INIT):
    cards += f'<a class="ini i{i}" href="initiatives.html#{slug}">{img(im, t + ": illustrative scene", "", 900, 600)}<div><h3>{t}</h3><p>{d}</p><span>Explore {t}</span></div></a>'
paths = "".join(f'<li><a href="get-involved.html#{j}"><strong>{a}</strong><span>{b}</span></a></li>' for j, (a, b) in enumerate(PATHS))
steps = "".join(f"<li><h3>{a}</h3><p>{b}</p></li>" for a, b in [("Discover a need", "Listen first. Neighbours tell us what is missing."),
 ("Connect with people", "Match that need with volunteers, mentors and partners."),
 ("Take action", "Start small and local, with clear roles and a schedule."),
 ("Build lasting opportunity", "Hand over skills and tools so the work keeps going.")])
sto = "".join(f'<a class="story" href="stories.html#s{i}">{img(s[2], s[0], "", 700, 460)}<h3>{s[0]}</h3><p>{s[3]}</p></a>' for i, s in enumerate(STORIES[:3]))
P["index.html"] = ("Make room for a better tomorrow", "A concept social-impact organisation connecting people, skills and opportunity through education, women's enterprise and community.", f'''
<section class="hero wrap"><div class="htxt"><h1>Make room for a better tomorrow.</h1>
<p class="lead">Where people, opportunities, and compassion come together to create meaningful change.</p>
<p class="cta"><a class="btn solid" href="#mission">Discover Our Mission</a><a class="btn ghost" href="#help">Find Your Way to Help</a></p></div>
<figure class="arch">{img("vision", "Concept illustration of a connected community campus with solar canopies, a library, clinic and gardens", "", 1400, 764, True)}<figcaption>Illustrative scene</figcaption></figure>
<a class="scroll" href="#mission" aria-label="Scroll to mission">Scroll</a></section>
<section id="mission" class="wrap split"><h2>Change begins when opportunity reaches someone.</h2>
<div><p class="lead">Lasting progress needs four things at once: access to education, practical skills, a supportive community and a real chance to take part.</p>
<p>{B} is a concept organisation built on that belief. We treat every person as capable and ambitious, and we measure ourselves by what people build, not by what they lack.</p></div></section>
<section class="wrap vision">{img("hero", "Women, children and neighbours gathered at sunrise in front of a community learning hub", "", 1200, 670)}<p class="cap">Concept illustration of the neighbours we work alongside. AI-generated, not real people.</p></section>
<section class="wrap"><h2>Four ways we work</h2><div class="inis">{cards}</div></section>
<section class="wrap band"><h2>How change happens</h2><ol class="steps">{steps}</ol></section>
<section id="help" class="wrap"><h2>Find your way to help</h2><p class="lead">Taking part can look many ways, and every contribution is voluntary.</p><ul class="paths">{paths}</ul></section>
<section class="wrap"><h2>Stories that matter</h2><p class="demo">Illustrative stories with fictional characters, not real testimonials.</p><div class="stories">{sto}</div><p><a class="btn ghost" href="stories.html">Read all stories</a></p></section>
<section class="wrap band"><h2>Trust and transparency</h2><div class="cols3"><div><h3>Our approach</h3><p>Listen, co-design with residents, start small, review in public.</p></div>
<div><h3>Responsible participation</h3><p>Clear roles, safeguarding for children, and no pressure to give.</p></div>
<div><h3>Reports</h3><p>Verified reports would be published on the <a href="impact.html">Impact page</a>. None exist yet because this is a concept project. We claim no registrations or partnerships.</p></div></div></section>
<section class="final"><div class="wrap"><h2>A better future is something we build together.</h2><p class="lead">Start with what you can offer. Discover where it can make a difference.</p><a class="btn amber" href="get-involved.html">Take Your First Step</a></div></section>''')

# ---------- ABOUT
P["about.html"] = ("About Us", "The purpose, values and approach behind Kinora, a concept social-impact organisation.", banner("A place to arrive, and a place to start from.", "Our name starts from kin, the people we belong to. In Kerala homes the verandah is where neighbours stop, talk and are made welcome, and we take that as our model.", "hub") + f'''
<section class="wrap split"><h2>Origin and purpose</h2><div><p>{B} is concept content created for a design project, so it has no real history. The idea is simple: build open, welcoming places where learning, skills and community meet.</p>
<p><strong>Mission:</strong> connect people, skills and resources so everyone can build a better future. <strong>Vision:</strong> a neighbourhood where nobody has to ask permission to learn.</p></div></section>
<section class="wrap band"><h2>Values</h2><div class="cols3"><div><h3>Dignity</h3><p>People are the experts on their own lives.</p></div><div><h3>Inclusion</h3><p>Every language, faith, ability and age is welcome.</p></div><div><h3>Responsibility</h3><p>Voluntary giving, honest reporting, safe participation.</p></div></div></section>
<section class="wrap split"><h2>How initiatives are designed and evaluated</h2><div><p>We start with residents' priorities, pilot for three months, then review outputs and outcomes with participants before scaling. Our hopes for the future: more local mentors, a shared learning library and open yearly reports.</p></div></section>
<section class="wrap">{img("garden", "Illustrative scene of a community hub with a health desk, a world-map table and a vegetable garden", "wide", 1408, 383)}</section>''')

# ---------- INITIATIVES
ib = ""
for slug, t, c, im, d, aud, chal, act in INIT:
    ib += f'''<article id="{slug}" class="ibox" data-cat="{c}">{img(im, t + ": illustrative scene", "", 900, 520)}<div><h2>{t}</h2><p class="lead">{d}</p>
<dl><dt>Who it is for</dt><dd>{aud}</dd><dt>The challenge</dt><dd>{chal}</dd><dt>What we do</dt><dd>{act}</dd></dl>
<p><a class="btn ghost" href="get-involved.html">Take part in {t}</a> <a href="stories.html?c={c}">Related stories</a></p></div></article>'''
flt = '<button data-f="all" aria-pressed="true">All</button>' + "".join(f'<button data-f="{i[2]}" aria-pressed="false">{i[2].title()}</button>' for i in INIT)
P["initiatives.html"] = ("Our Initiatives", "Four initiatives covering children's learning, women's enterprise, practical skills and community welfare.", banner("Four initiatives, one belief.", "Pick the one closest to your interest, or see how they connect.", "help") + f'<section class="wrap"><div class="filters" role="group" aria-label="Filter initiatives">{flt}</div><div id="list">{ib}</div><p class="empty" hidden>No initiatives match this filter.</p></section>')

# ---------- IMPACT
bars = "".join(f'<li><span>{a}</span><div class="bar"><i style="width:{v}%"></i></div><b>{v}%</b></li>' for a, v in
               [("Reading circles set up (demo goal)", 70), ("Women in skills labs (demo goal)", 55), ("Workshops delivered (demo goal)", 82), ("Volunteer days filled (demo goal)", 64)])
P["impact.html"] = ("Our Impact", "How Kinora would measure activities, outputs and long-term outcomes. All figures are demo data.", banner("Impact we would measure, and how we would show it.", "Every number on this page is demo data. Real reports would replace it.", "march") + f'''
<section class="wrap split"><h2>Activities, outputs, outcomes</h2><div><p><strong>Activities</strong> are what we do (a reading circle). <strong>Outputs</strong> are what that produces (sessions held, people attending). <strong>Outcomes</strong> are lasting changes (a child reads independently; a woman earns steadily). We report all three and never mix them up.</p></div></section>
<section class="wrap band"><h2>Programme progress <span class="tag">Demo data</span></h2><ul class="bars">{bars}</ul></section>
<section class="wrap"><h2>From need to opportunity <span class="tag">Concept visualisation</span></h2><p>Drag the handle to compare. This AI-generated illustration shows the kind of change we aim to support.</p>
<div class="cmp"><img src="img/skills.webp" alt="Illustration: a bright learning hall where children receive certificates" width="900" height="768"><div class="cl"><img src="img/before.webp" alt="Illustration: a crowded lane where families work with bundles of sticks" width="900" height="768"></div>
<input type="range" min="0" max="100" value="50" aria-label="Compare before and after" class="cr"></div></section>
<section class="wrap band"><h2>Sample impact report</h2><div class="card"><h3>Quarter 1 summary <span class="tag">Template</span></h3><p>Activities: [to be completed]. Outputs: [to be completed]. Outcomes: [to be completed]. Verified reports and updates would be published here.</p><button class="btn ghost" onclick="window.print()">Print this page</button></div></section>''')

# ---------- STORIES
sl = '<button data-f="all" aria-pressed="true">All</button>' + "".join(f'<button data-f="{i[2]}" aria-pressed="false">{i[2].title()}</button>' for i in INIT)
sb = "".join(f'<article id="s{i}" class="sbox" data-cat="{s[1]}">{img(s[2], s[0], "", 700, 460)}<div><h2>{s[0]}</h2><p class="demo">Illustrative story</p><p>{s[4]}</p><a href="initiatives.html#{INIT[["children","women","skills","community"].index(s[1])][0]}">Related initiative</a> <button class="share" data-t="{s[0]}">Copy link</button></div></article>' for i, s in enumerate(STORIES))
P["stories.html"] = ("Stories", "Illustrative stories about learning, skills and community. All characters are fictional.", banner("Stories of people building their own next chapter.", "Every story here is a fictional demonstration.", "women") + f'<section class="wrap"><div class="filters" role="group" aria-label="Filter stories">{sl}</div><div id="list">{sb}</div><p class="empty" hidden>No stories match this filter.</p></section>')

# ---------- GET INVOLVED / CONTACT / 404 / legal
pl = "".join(f'<li id="{j}"><strong>{a}</strong><span>{b}</span></li>' for j, (a, b) in enumerate(PATHS))
P["get-involved.html"] = ("Get Involved", "Choose how to take part: volunteer, share skills, mentor, support or partner.", banner("Start with what you can offer.", "Choose a pathway and tell us a little about you. This form is a demo.", "help") + f'''<section class="wrap band"><h2>Hours planner</h2><p>See what your time could add up to. Simple arithmetic on your own numbers, not a claim about results.</p>
<div class="card"><label for="ph">Hours per week: <output id="po">2</output></label><input id="ph" type="range" min="1" max="10" value="2">
<p id="pt" role="status"></p></div></section><section class="wrap split"><ul class="paths plain">{pl}</ul>{form("involve")}</section>''')
P["contact.html"] = ("Contact", "Send a demonstration message to Kinora.", banner("Say hello.", "No contact details are listed because none are verified. The form below is a local demo.", "hub") + f'<section class="wrap narrow">{form("contact")}</section>')
P["404.html"] = ("Page not found", "This page does not exist.", '<section class="wrap narrow"><h1>That page is not here.</h1><p class="lead">The link may be old or mistyped.</p><a class="btn solid" href="index.html">Go to the home page</a></section>')
P["privacy.html"] = ("Privacy Policy", "Privacy policy for the Kinora concept site.", '<section class="wrap narrow"><h1>Privacy Policy</h1><p>This concept site collects no personal data. Forms run in your browser and send nothing anywhere. It sets no tracking cookies. A real organisation would replace this text with a reviewed policy.</p></section>')
P["terms.html"] = ("Terms of Use", "Terms of use for the Kinora concept site.", '<section class="wrap narrow"><h1>Terms of Use</h1><p>This is a concept project for demonstration. It is not a registered organisation, takes no donations and makes no claims about real programmes.</p></section>')

for fn, (t, d, b) in P.items():
    open(fn, "w", encoding="utf-8").write(page(fn, t, d, b))

open("favicon.svg", "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 30 30"><rect width="30" height="30" rx="6" fill="#1F3A2D"/><path d="M5 26V15a10 10 0 0 1 20 0v11" fill="none" stroke="#F7F2E6" stroke-width="2.5"/><path d="M11 26V16a4 4 0 0 1 8 0v10" fill="#C28A2C"/></svg>')
open("sitemap.xml", "w").write('<?xml version="1.0"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{f}</loc></url>" for f in P if f != "404.html") + "</urlset>")

open("styles.css", "w").write(''':root{--iv:#F7F2E6;--cr:#EDE5D0;--fo:#1F3A2D;--sa:#D9E0CC;--sg:#8FA38A;--am:#C28A2C;--ch:#2B2A27;--r:14px}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--iv);color:var(--ch);font:17px/1.65 "Instrument Sans",system-ui,sans-serif}
h1,h2,h3{font-family:"Young Serif",Georgia,serif;font-weight:400;color:var(--fo);line-height:1.15;margin:0 0 .5em}
h1{font-size:clamp(2.4rem,6vw,4.6rem)}h2{font-size:clamp(1.7rem,3.4vw,2.7rem)}h3{font-size:1.3rem}
img{max-width:100%;height:auto;display:block}a{color:var(--fo)}:focus-visible{outline:3px solid var(--am);outline-offset:3px}
.skip{position:absolute;left:-999px}.skip:focus{left:8px;top:8px;background:#fff;padding:8px;z-index:99}
.wrap{max-width:1180px;margin:0 auto;padding:clamp(40px,7vw,96px) 20px}.narrow{max-width:720px}
.top{position:sticky;top:0;z-index:20;display:flex;align-items:center;justify-content:space-between;padding:12px 20px;background:rgba(247,242,230,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--cr)}
.brand{display:flex;gap:8px;align-items:center;font:1.5rem "Young Serif",serif;color:var(--fo);text-decoration:none}
nav{display:flex;gap:20px;align-items:center}nav ul{display:flex;gap:18px;list-style:none;margin:0;padding:0}nav a:not(.btn){text-decoration:none;font-size:.95rem}nav a[aria-current]{border-bottom:2px solid var(--am)}
.burger{display:none}.btn{display:inline-block;padding:.75em 1.4em;border-radius:99px;text-decoration:none;font-weight:600;border:2px solid var(--fo);cursor:pointer;font-size:1rem;font-family:inherit;transition:background .2s,color .2s}
.solid{background:var(--fo);color:var(--iv)}.solid:hover{background:#2c5440}.ghost{background:none;color:var(--fo)}.ghost:hover{background:var(--sa)}.amber{background:var(--am);border-color:var(--am);color:#1b1b1b}
.hero{display:grid;grid-template-columns:1.05fr 1fr;gap:48px;align-items:center;position:relative;padding-top:56px}.hero h1{max-width:12ch}.lead{font-size:1.2rem;max-width:34em}.cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}
.arch{margin:0;position:relative;justify-self:end;width:100%;max-width:520px;border-radius:999px 999px 8px 8px;overflow:hidden;animation:open 1.2s cubic-bezier(.2,.7,.2,1) both}.arch img{aspect-ratio:4/5;object-fit:cover;object-position:50% 55%;width:100%}
.arch figcaption{position:absolute;right:16px;bottom:12px;background:var(--iv);font-size:.75rem;padding:2px 8px;border-radius:9px}
@keyframes open{from{clip-path:inset(100% 0 0 0)}to{clip-path:inset(0)}}
.scroll{position:absolute;left:20px;bottom:20px;font-size:.8rem;text-decoration:none;color:var(--fo)}.scroll:after{content:"";display:block;width:1px;height:36px;background:var(--fo);margin:6px 0 0 14px}
.split{display:grid;grid-template-columns:1fr 1.2fr;gap:48px}.band{background:var(--sa);max-width:none}.band>*{max-width:1140px;margin-left:auto;margin-right:auto}
.vision img,.wide{width:100%;aspect-ratio:21/9;border-radius:var(--r);object-fit:cover}.cap{font-size:.85rem;opacity:.8}
.inis{display:grid;grid-template-columns:repeat(2,1fr);gap:48px 32px}.ini{text-decoration:none;color:inherit;display:grid;grid-template-rows:auto 1fr;gap:16px;align-content:start}.ini img{border-radius:var(--r);width:100%;aspect-ratio:3/2;object-fit:cover;object-position:center 40%}.ini h3{margin-bottom:.3em}.ini p{margin:0 0 .6em}

.ini span{color:var(--am);font-weight:600;text-decoration:underline}.ini:hover img{filter:brightness(1.05)}
.steps{counter-reset:s;list-style:none;padding:0;display:grid;grid-template-columns:repeat(4,1fr);gap:24px;position:relative}.steps li{counter-increment:s;border-top:3px solid var(--fo);padding-top:16px}.steps li:before{content:counter(s);font:1.6rem "Young Serif",serif;color:var(--am)}
.paths{list-style:none;padding:0;margin:24px 0 0;display:grid;gap:0}.paths li a,.paths.plain li{display:grid;grid-template-columns:1fr 1.4fr;gap:16px;padding:20px 0;border-top:1px solid var(--sg);text-decoration:none;color:inherit}.paths a:hover strong{color:var(--am)}.paths strong{font:1.3rem "Young Serif",serif;color:var(--fo)}
.stories{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin:20px 0}.story{text-decoration:none;color:inherit}.story img{border-radius:var(--r);aspect-ratio:3/2;object-fit:cover;width:100%}
.cols3{display:grid;grid-template-columns:repeat(3,1fr);gap:28px}.final{background:var(--fo);color:var(--iv);text-align:center}.final h2,.final .lead{color:var(--iv);margin-left:auto;margin-right:auto}.final .wrap{padding:96px 20px}
.demo,.tag{display:inline-block;background:var(--cr);border:1px dashed var(--am);padding:2px 10px;border-radius:99px;font:600 .8rem "Instrument Sans";color:var(--ch)}
.pagehead{display:grid;grid-template-columns:1.3fr 1fr;gap:40px;align-items:center;padding-bottom:20px}.arch.small{border-radius:999px 999px 8px 8px;aspect-ratio:4/5;object-fit:cover;object-position:center 35%;justify-self:end;width:100%;max-width:300px;max-height:none;animation:open 1s both}
.filters{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:28px}.filters button{padding:.5em 1.1em;border-radius:99px;border:2px solid var(--fo);background:none;font:inherit;cursor:pointer}.filters [aria-pressed=true]{background:var(--fo);color:var(--iv)}
.ibox,.sbox{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:start;padding:48px 0;border-top:1px solid var(--sg);scroll-margin-top:80px}.ibox:nth-child(even) img,.sbox:nth-child(even) img{order:2}.ibox img,.sbox img{border-radius:var(--r);width:100%;aspect-ratio:4/3;object-fit:cover;object-position:center 40%}.ibox h2,.sbox h2{margin-top:0}
dt{font-weight:600;color:var(--fo);margin-top:10px}dd{margin:0}[hidden]{display:none!important}
.bars{list-style:none;padding:0;display:grid;gap:16px}.bars li{display:grid;grid-template-columns:1fr 2fr 50px;gap:12px;align-items:center}.bar{background:var(--iv);border-radius:99px;height:14px;overflow:hidden}.bar i{display:block;height:100%;background:var(--fo)}
.cmp{position:relative;max-width:760px;overflow:hidden;border-radius:var(--r)}.cmp img{width:100%;object-fit:cover}.cl{position:absolute;inset:0;width:50%;overflow:hidden;border-right:3px solid var(--iv)}.cl img{width:auto;max-width:none;height:100%;aspect-ratio:900/768}
.cr{position:absolute;left:0;right:0;bottom:12px;width:100%;margin:0;accent-color:var(--am)}
.card{background:#fff8;border:1px solid var(--cr);border-radius:var(--r);padding:28px}.form{display:grid;gap:6px;background:var(--cr)}label{font-weight:600;margin-top:10px}input,select,textarea{font:inherit;padding:.7em;border:2px solid var(--sg);border-radius:10px;background:#fff;width:100%}input[aria-invalid=true],select[aria-invalid=true],textarea[aria-invalid=true]{border-color:#9b2c1d}
.err{color:#9b2c1d;font-size:.9rem;margin:0;min-height:0}.ok{background:var(--sa);padding:14px;border-radius:10px;margin-top:12px}.form button{margin-top:14px;justify-self:start}
footer{background:var(--cr);padding:56px 20px 24px}.fgrid{max-width:1140px;margin:0 auto;display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:32px}footer h2{font:600 1rem "Instrument Sans"}footer ul{list-style:none;padding:0;line-height:2}.note{max-width:1140px;margin:12px auto;font-size:.82rem}
@media(max-width:860px){.burger{display:block;padding:.5em 1em;border:2px solid var(--fo);border-radius:99px;background:none;font:inherit}nav{display:none;position:absolute;top:100%;left:0;right:0;background:var(--iv);flex-direction:column;align-items:flex-start;padding:20px;border-bottom:1px solid var(--cr)}nav.open{display:flex}nav ul{flex-direction:column}
.hero,.split,.pagehead,.ibox,.sbox,.cols3,.steps,.stories,.fgrid,.paths li a,.paths.plain li{grid-template-columns:1fr}.inis{grid-template-columns:1fr}.ibox:nth-child(even) img,.sbox:nth-child(even) img{order:0}.arch img{aspect-ratio:4/3}.scroll{display:none}.arch.small{justify-self:start;aspect-ratio:3/2;border-radius:var(--r);max-width:100%}.hero .arch{justify-self:stretch;max-width:none}.ibox,.sbox{gap:20px}.inis{gap:36px}.bars li{grid-template-columns:1fr 50px}.bar{grid-column:1/-1}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
dialog{border:0;border-radius:var(--r);padding:24px;width:min(560px,92vw);background:var(--iv)}dialog::backdrop{background:#1f3a2d99}#sr{list-style:none;padding:0}#sr li{padding:8px 0;border-bottom:1px solid var(--cr)}.sbtn{margin-left:auto;margin-right:10px;padding:.5em 1em;border:2px solid var(--fo);border-radius:99px;background:none;font:inherit;cursor:pointer}output{color:var(--am);font-weight:600}.share{margin-left:12px;padding:.3em .9em;border:2px solid var(--fo);border-radius:99px;background:none;font:inherit;font-size:.9rem;cursor:pointer}
@media print{.top,footer,.cta,.burger{display:none}}''')

open("app.js", "w").write(r'''(function(){
var b=document.querySelector(".burger"),n=document.getElementById("menu");
b.addEventListener("click",function(){var o=n.classList.toggle("open");b.setAttribute("aria-expanded",o)});
document.addEventListener("keydown",function(e){if(e.key==="Escape"&&n.classList.contains("open")){n.classList.remove("open");b.setAttribute("aria-expanded",false);b.focus()}});
var fb=document.querySelectorAll(".filters button");
function filt(f){var shown=0;document.querySelectorAll("#list [data-cat]").forEach(function(x){var s=f==="all"||x.dataset.cat===f;x.hidden=!s;if(s)shown++});
 fb.forEach(function(k){k.setAttribute("aria-pressed",k.dataset.f===f)});var e=document.querySelector(".empty");if(e)e.hidden=shown>0}
fb.forEach(function(k){k.addEventListener("click",function(){filt(k.dataset.f)})});
var q=new URLSearchParams(location.search).get("c");if(q&&fb.length)filt(q);
var r=document.querySelector(".cr");if(r)r.addEventListener("input",function(){document.querySelector(".cl").style.width=r.value+"%"});
document.querySelectorAll(".share").forEach(function(s){s.addEventListener("click",function(){
 var u=location.href.split("#")[0]+"#"+s.closest("article").id;
 (navigator.clipboard?navigator.clipboard.writeText(u):Promise.reject()).then(function(){s.textContent="Link copied"},function(){s.textContent="Copy failed: copy from the address bar"})})});
document.querySelectorAll("form[data-demo]").forEach(function(f){
 f.addEventListener("submit",function(e){e.preventDefault();var bad=null;
  f.querySelectorAll("input,select,textarea").forEach(function(i){var m="",v=i.value.trim(),p=f.querySelector('.err[data-for="'+i.id+'"]');
   if(i.required&&!v)m=i.tagName==="SELECT"?"Choose an option.":"Enter your "+(i.labels[0].textContent.toLowerCase());
   else if(i.type==="email"&&!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v))m="Enter an email like name@example.com.";
   else if(i.minLength>0&&v&&v.length<i.minLength)m="Write at least "+i.minLength+" characters.";
   else if(i.type==="number"&&v&&(v<0||v>40))m="Enter a number from 0 to 40.";
   if(p)p.textContent=m;i.setAttribute("aria-invalid",!!m);if(m&&!bad)bad=i});
  var ok=f.querySelector(".ok");
  if(bad){bad.focus();ok.hidden=true;return}
  ok.hidden=false;ok.textContent="Thanks, "+f.name.value.trim()+". This is a demonstration, so your message was NOT sent to anyone and nothing was stored.";f.reset()})});
})();''')
js=open("app.js").read()
import json
idx=[{"t":t,"u":h,"d":d} for h,(t,d,b) in P.items() if h not in("404.html",)]+[{"t":i[1],"u":"initiatives.html#"+i[0],"d":i[4]} for i in INIT]+[{"t":x[0],"u":"stories.html#s%d"%k,"d":x[3]} for k,x in enumerate(STORIES)]
js=js.rstrip()[:-6]+"""
var IDX=%s,d=document.getElementById("sd"),sq=document.getElementById("sq"),sr=document.getElementById("sr");
function srch(){var v=sq.value.trim().toLowerCase();sr.innerHTML="";if(!v){return}
 var m=IDX.filter(function(x){return(x.t+" "+x.d).toLowerCase().indexOf(v)>-1});
 if(!m.length){sr.innerHTML="<li>No results. Try a word like reading, women or skills.</li>";return}
 m.slice(0,8).forEach(function(x){var li=document.createElement("li"),a=document.createElement("a");a.href=x.u;a.textContent=x.t;li.appendChild(a);sr.appendChild(li)})}
document.querySelector(".sbtn").addEventListener("click",function(){d.showModal();sq.focus()});
sq.addEventListener("input",srch);
document.addEventListener("keydown",function(e){if(e.key==="/"&&!/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)){e.preventDefault();d.showModal();sq.focus()}});
var ph=document.getElementById("ph");if(ph){function pu(){var h=+ph.value,y=h*44;document.getElementById("po").textContent=h;
 document.getElementById("pt").textContent="Over a 44-week year that is about "+y+" hours, or roughly "+Math.floor(y/2)+" two-hour reading or workshop sessions."}ph.addEventListener("input",pu);pu()}
})();""" % json.dumps(idx)
open("app.js","w").write(js)
print("built", len(P), "pages")
