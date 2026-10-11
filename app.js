(function(){
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
var IDX=[{"t": "Make room for a better tomorrow", "u": "index.html", "d": "A concept social-impact organisation connecting people, skills and opportunity through education, women's enterprise and community."}, {"t": "About Us", "u": "about.html", "d": "The purpose, values and approach behind Kinora, a concept social-impact organisation."}, {"t": "Our Initiatives", "u": "initiatives.html", "d": "Four initiatives covering children's learning, women's enterprise, practical skills and community welfare."}, {"t": "Our Impact", "u": "impact.html", "d": "How Kinora would measure activities, outputs and long-term outcomes. All figures are demo data."}, {"t": "Stories", "u": "stories.html", "d": "Illustrative stories about learning, skills and community. All characters are fictional."}, {"t": "Get Involved", "u": "get-involved.html", "d": "Choose how to take part: volunteer, share skills, mentor, support or partner."}, {"t": "Contact", "u": "contact.html", "d": "Send a demonstration message to Kinora."}, {"t": "Privacy Policy", "u": "privacy.html", "d": "Privacy policy for the Kinora concept site."}, {"t": "Terms of Use", "u": "terms.html", "d": "Terms of use for the Kinora concept site."}, {"t": "Learning Without Limits", "u": "initiatives.html#learning", "d": "Reading corners, shared books and patient mentors, so a child's curiosity never waits for a classroom to be built."}, {"t": "Her Next Chapter", "u": "initiatives.html#her-next-chapter", "d": "Skills, savings circles and first-business coaching for women who are ready to earn on their own terms."}, {"t": "Skills for Tomorrow", "u": "initiatives.html#skills", "d": "Practical workshops, from solar kits to certificates, that turn learning into something you can use on Monday."}, {"t": "Stronger Together", "u": "initiatives.html#stronger-together", "d": "Community meals, health information and volunteer-led projects that make a neighbourhood feel like one."}, {"t": "A reading circle begins under the mango tree", "u": "stories.html#s0", "d": "Illustrative story: Meera, 9, wants to read the whole shelf before the monsoon."}, {"t": "Three women, one shared stall", "u": "stories.html#s1", "d": "Illustrative story: a savings circle turns a recipe into a stall."}, {"t": "Solar kits and a first certificate", "u": "stories.html#s2", "d": "Illustrative story: a workshop where learning becomes something to hold."}, {"t": "The information desk that speaks your language", "u": "stories.html#s3", "d": "Illustrative story: a volunteer-run desk answers questions in three languages."}],d=document.getElementById("sd"),sq=document.getElementById("sq"),sr=document.getElementById("sr");
function srch(){var v=sq.value.trim().toLowerCase();sr.innerHTML="";if(!v){return}
 var m=IDX.filter(function(x){return(x.t+" "+x.d).toLowerCase().indexOf(v)>-1});
 if(!m.length){sr.innerHTML="<li>No results. Try a word like reading, women or skills.</li>";return}
 m.slice(0,8).forEach(function(x){var li=document.createElement("li"),a=document.createElement("a");a.href=x.u;a.textContent=x.t;li.appendChild(a);sr.appendChild(li)})}
document.querySelector(".sbtn").addEventListener("click",function(){d.showModal();sq.focus()});
sq.addEventListener("input",srch);
document.addEventListener("keydown",function(e){if(e.key==="/"&&!/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)){e.preventDefault();d.showModal();sq.focus()}});
var ph=document.getElementById("ph");if(ph){function pu(){var h=+ph.value,y=h*44;document.getElementById("po").textContent=h;
 document.getElementById("pt").textContent="Over a 44-week year that is about "+y+" hours, or roughly "+Math.floor(y/2)+" two-hour reading or workshop sessions."}ph.addEventListener("input",pu);pu()}
})();