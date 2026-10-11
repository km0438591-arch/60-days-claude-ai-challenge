<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Day 36 - Cognitive Pattern Explorer</title>
<style>
:root{--bg:#0a0a0f;--card:#15151c;--b:#252530;--p:#a78bfa;--t:#fff;--m:#9ca3af;--ok:#22c55e;--bad:#ef4444}
*{margin:0;padding:0;box-sizing:border-box;font-family:Inter,sans-serif}
body{background:var(--bg);color:var(--t);padding:20px}
.wrap{max-width:950px;margin:auto}
.hdr{text-align:center;padding:28px 0}
.hdr h1{font-size:2.6rem;background:linear-gradient(90deg,#a78bfa,#f472b6,#60a5fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.card{background:var(--card);border:1px solid var(--b);border-radius:16px;padding:22px;margin:14px 0}
.top{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.kpi span{color:var(--m);font-size:.85rem}
.bar{height:8px;background:var(--b);border-radius:10px;margin:12px 0;overflow:hidden}
.fill{height:100%;background:linear-gradient(90deg,#a78bfa,#ec4899);transition:.3s}
.qbox{background:#0f0f14;border-left:3px solid var(--p);padding:14px;border-radius:8px;margin:10px 0}
.zone{min-height:120px;border:2px dashed var(--b);border-radius:12px;padding:14px;display:flex;flex-wrap:wrap;gap:10px}
.chip{background:#222230;border:1px solid var(--b);padding:9px 14px;border-radius:22px;cursor:grab}
.btn{background:var(--p);color:#000;font-weight:700;border:none;padding:11px 20px;border-radius:10px;cursor:pointer}
.btn2{background:transparent;border:1px solid var(--b);color:var(--t);padding:11px 20px;border-radius:10px;cursor:pointer}
.opt{padding:14px;border:1px solid var(--b);border-radius:10px;margin:8px 0;cursor:pointer}
.opt:hover{border-color:var(--p)}
.opt.ok{border-color:var(--ok);background:#22c55e18}
.opt.no{border-color:var(--bad);background:#ef444418}
.hidden{display:none}
.tag{display:inline-block;padding:4px 10px;border-radius:20px;font-size:.75rem;margin:2px;background:#222230;border:1px solid var(--b)}
</style>
</head>
<body>
<div class="wrap">
<div class="hdr">
<h1>Cognitive Pattern Explorer</h1>
<p style="color:var(--m)">Explore your thinking patterns through science-based puzzles – Day 36</p>
</div>

<div class="top">
<div class="card kpi"><span>Patterns Found</span><h2 id="score">0</h2></div>
<div class="card kpi"><span>Level</span><h2 id="lvl">1/6</h2></div>
<div class="card kpi"><span>Bias Meter</span><h2 id="bias">Low</h2></div>
<div class="card kpi"><span>Insights</span><h2 id="ins">0</h2></div>
</div>

<div class="bar"><div id="prog" class="fill" style="width:16%"></div></div>

<div id="game" class="card">
<h2 id="title">Loading...</h2>
<p id="desc" style="color:var(--m);margin:8px 0"></p>
<div id="task" class="qbox"></div>
<div id="drop" class="zone" style="margin:12px 0"></div>
<div id="drag" class="zone"></div>
<div style="margin-top:14px;display:flex;gap:10px">
<button class="btn" onclick="check()">Analyze Pattern</button>
<button class="btn2" onclick="reset()">Reset</button>
<button class="btn2" onclick="hint()">💡 Hint</button>
</div>
<p id="fb" style="margin-top:14px"></p>
</div>

<div id="report" class="card hidden">
<h2>🧠 Your Cognitive Profile</h2>
<div id="rep"></div>
<button class="btn" style="margin-top:12px" onclick="location.reload()">Explore Again</button>
</div>
</div>

<script>
const levels=[
{
title:"1. Confirmation Bias Detector",
desc:"Drag statements into Thinking Traps",
task:"You only search articles that prove your startup idea will work. What bias is this? Separate biased vs balanced thinking.",
type:"sort",
buckets:["🔴 Biased Thinking","🟢 Balanced Thinking"],
items:[
{text:"Only reading positive reviews about your idea",bucket:0,bias:"Confirmation Bias"},
{text:"Ignoring negative feedback",bucket:0,bias:"Confirmation Bias"},
{text:"Actively searching for disconfirming evidence",bucket:1,bias:"Balanced"},
{text:"Asking 'What would prove me wrong?'",bucket:1,bias:"Balanced"},
],
hint:"Confirmation bias = favoring info that confirms your beliefs"
},
{
title:"2. Anchoring Effect",
desc:"Choose the rational decision",
task:"First house you saw was ₹2Cr. Second house ₹1.2Cr looks cheap but market value is ₹80L. What's happening?",
type:"mcq",
options:["A) Second house is a great deal","B) You are anchored to first price, second is still overpriced - need independent valuation","C) Buy quickly before price rises"],
correct:1,
hint:"Anchoring = first number sticks in mind"
},
{
title:"3. Availability Heuristic",
desc:"Drag into Fast vs Slow Thinking",
task:"After seeing 3 plane crash news, you think flying is dangerous, though stats say it's safest.",
type:"sort",
buckets:["⚡ Fast System 1 (Emotional)","🧠 Slow System 2 (Rational)"],
items:[
{text:"Plane crashes feel frequent because of news",bucket:0},
{text:"Check actual accident rate per million flights",bucket:1},
{text:"Avoid flying due to fear",bucket:0},
{text:"Calculate risk vs driving risk",bucket:1},
],
hint:"System 1 uses easy recall, System 2 uses data"
},
{
title:"4. Sunk Cost Fallacy Lab",
desc:"What should a rational founder do?",
task:"You spent 6 months building a feature no one uses. User says 'Continue, we already invested'.",
type:"mcq",
options:["A) Continue because 6 months invested","B) Stop and pivot - sunk cost should not affect future decision, evaluate future ROI only","C) Invest 6 more months to justify previous"],
correct:1,
hint:"Sunk cost = past cost should not drive future"
},
{
title:"5. Cognitive Distortion Puzzle",
desc:"Match distortion to thought",
task:"Drag thoughts to correct distortion type",
type:"match",
pairs:[
{thought:"I failed one interview, I will never get a job",type:"Catastrophizing"},
{thought:"My boss didn't reply = He hates me",type:"Mind Reading"},
{thought:"I must be perfect or I am a failure",type:"All-or-Nothing"},
{thought:"She got promoted because of luck, not skill",type:"Discounting Positive"},
],
hint:"Each is a common thinking trap"
},
{
title:"6. Metacognition - Your Pattern",
desc:"Self-reflection",
task:"When you face conflicting information, what is your FIRST reaction?",
type:"mcq",
options:["A) Defend my original view strongly","B) Pause, list evidence for and against, then update my belief","C) Avoid the information completely"],
correct:1,
hint:"Best metacognition = active open-mindedness"
}
];

let cur=0,score=0,insights=[],biasLevel=0,sec=0;
let dragState=[];

function load(){
let L=levels[cur];
document.getElementById('lvl').textContent=`${cur+1}/${levels.length}`;
document.getElementById('prog').style.width=`${(cur+1)/levels.length*100}%`;
document.getElementById('title').textContent=L.title;
document.getElementById('desc').textContent=L.desc;
document.getElementById('task').textContent=L.task;
document.getElementById('fb').textContent='';
document.getElementById('drag').innerHTML='';
document.getElementById('drop').innerHTML='';

if(L.type==='mcq'){
document.getElementById('drop').classList.add('hidden');
document.getElementById('drag').innerHTML=L.options.map((o,i)=>`<div class="opt" onclick="checkMcq(${i})">${o}</div>`).join('');
}else if(L.type==='sort'){
document.getElementById('drop').classList.remove('hidden');
document.getElementById('drop').innerHTML=L.buckets.map((b,i)=>`<div style="flex:1;min-width:200px"><strong>${b}</strong><div id="bucket-${i}" class="zone" style="min-height:100px;margin-top:6px" ondrop="drop(event,${i})" ondragover="allow(event)"></div></div>`).join('');
L.items.sort(()=>Math.random()-0.5).forEach(it=>{
let d=document.createElement('div');d.className='chip';d.draggable=true;d.textContent=it.text;
d.ondragstart=e=>e.dataTransfer.setData('t',it.text);
document.getElementById('drag').appendChild(d);
});
dragState=[];
}else if(L.type==='match'){
document.getElementById('drop').classList.remove('hidden');
let thoughts=L.pairs.map(p=>p.thought).sort(()=>Math.random()-0.5);
let types=[...new Set(L.pairs.map(p=>p.type))];
document.getElementById('drop').innerHTML=types.map(t=>`<div style="flex:1"><strong>${t}</strong><div id="bucket-${t}" class="zone" style="min-height:80px;margin-top:6px" ondrop="dropMatch(event,'${t}')" ondragover="allow(event)"></div></div>`).join('');
thoughts.forEach(th=>{
let d=document.createElement('div');d.className='chip';d.draggable=true;d.textContent=th;
d.ondragstart=e=>e.dataTransfer.setData('t',th);
document.getElementById('drag').appendChild(d);
});
dragState=[];
}
}
function allow(e){e.preventDefault()}
function drop(e,i){
e.preventDefault();let t=e.dataTransfer.getData('t');
let el=[...document.querySelectorAll('.chip')].find(x=>x.textContent===t);
if(el){document.getElementById(`bucket-${i}`).appendChild(el);dragState.push({text:t,bucket:i})}
}
function dropMatch(e,type){e.preventDefault();let t=e.dataTransfer.getData('t');let el=[...document.querySelectorAll('.chip')].find(x=>x.textContent===t);if(el){document.getElementById(`bucket-${type}`).appendChild(el);dragState.push({text:t,type:type})}}

function checkMcq(i){
let L=levels[cur];
let opts=document.querySelectorAll('.opt');
opts.forEach((o,idx)=>{if(idx===L.correct)o.classList.add('ok');else if(idx===i)o.classList.add('no')});
if(i===L.correct){score++;insights.push(L.title.split('.')[1]);document.getElementById('fb').innerHTML='<span style="color:#22c55e">✓ Pattern recognized! Metacognition improved.</span>';setTimeout(next,1200)}
else{biasLevel++;document.getElementById('fb').innerHTML='<span style="color:#ef4444">This is a thinking trap. Try again next level.</span>';setTimeout(next,1800)}
update();
}
function check(){
let L=levels[cur];
if(L.type==='sort'){
let correct=0;
dragState.forEach(d=>{let real=L.items.find(x=>x.text===d.text).bucket;if(real===d.bucket)correct++});
if(correct>=L.items.length-1){score++;insights.push(L.title);document.getElementById('fb').innerHTML=`<span style="color:#22c55e">✓ ${correct}/${L.items.length} correct - Pattern decoded!</span>`;setTimeout(next,1200)}
else{document.getElementById('fb').innerHTML=`<span style="color:#ef4444">Only ${correct}/${L.items.length}. Hint: ${L.hint}</span>`;biasLevel++}
}else if(L.type==='match'){
let correct=0;
dragState.forEach(d=>{let real=L.pairs.find(x=>x.thought===d.text).type;if(real===d.type)correct++});
if(correct>=L.pairs.length-1){score++;document.getElementById('fb').innerHTML='<span style="color:#22c55e">✓ Cognitive distortions mapped!</span>';setTimeout(next,1200)}else{document.getElementById('fb').innerHTML=`<span style="color:#ef4444">${correct}/${L.pairs.length} - Review hint</span>`}
}
update();
}
function next(){cur++;if(cur<levels.length)load();else finalReport()}
function update(){document.getElementById('score').textContent=score;document.getElementById('ins').textContent=insights.length;document.getElementById('bias').textContent=biasLevel>2?'High':biasLevel>0?'Medium':'Low';document.getElementById('bias').style.color=biasLevel>2?'#ef4444':biasLevel>0?'#f59e0b':'#22c55e'}
function reset(){load()}
function hint(){alert(levels[cur].hint)}
function finalReport(){
document.getElementById('game').classList.add('hidden');
document.getElementById('report').classList.remove('hidden');
let profile=score>=5?'Analytical Thinker':score>=3?'Reflective Explorer':'Bias-Prone - Keep Training';
document.getElementById('rep').innerHTML=`
<p><b>Score:</b> ${score}/${levels.length} | <b>Profile:</b> ${profile}</p>
<p><b>Bias Level:</b> ${biasLevel>2?'Needs work':'Good control'}</p>
<p><b>Patterns Mastered:</b> ${insights.join(', ')||'Learning in progress'}</p>
<hr style="margin:12px 0;border-color:#252530">
<h3>Your Thinking OS Upgrade</h3>
<ul style="margin:10px 0 0 18px;color:#9ca3af;line-height:1.7">
<li>Use <b>Pre-mortem</b>: Before deciding, imagine it failed and list reasons</li>
<li>Use <b>Second-order thinking</b>: Ask "And then what?" 3 times</li>
<li>Use <b>Disconfirming question</b>: "What evidence would prove me wrong?"</li>
</ul>
<pre style="background:#0f0f14;padding:12px;border-radius:8px;margin-top:12px;white-space:pre-wrap">Claude Prompt to explore yourself:
"You are a cognitive coach. Analyze my decision: [paste situation].
Identify 2 biases I might have and give me 3 reframing questions."</pre>
`;
}
load();
</script>
</body>
</html>
