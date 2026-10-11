<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Day 37 - Task Compass | Tech Company Edition</title>
<style>
:root{--bg:#080a10;--card:#11131d;--b:#1e2235;--p:#6366f1;--t:#e5e7eb;--m:#8b90a0;--u1:#ef4444;--u2:#f59e0b;--u3:#10b981;--u4:#6b7280}
*{margin:0;padding:0;box-sizing:border-box;font-family:Inter,sans-serif}
body{background:var(--bg);color:var(--t);padding:18px}
.wrap{max-width:1100px;margin:auto}
.hdr{text-align:center;padding:26px 0}
.hdr h1{font-size:2.6rem;background:linear-gradient(90deg,#6366f1,#06b6d4,#a78bfa);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.grid{display:grid;grid-template-columns:1fr 320px;gap:14px}
.card{background:var(--card);border:1px solid var(--b);border-radius:16px;padding:18px}
.compass{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:12px;height:620px}
.quadrant{border-radius:14px;padding:12px;border:1px solid var(--b);position:relative;overflow:auto}
.q1{background:linear-gradient(135deg,#ef444420,#11131d);border-color:#ef444440}
.q2{background:linear-gradient(135deg,#6366f120,#11131d);border-color:#6366f140}
.q3{background:linear-gradient(135deg,#f59e0b20,#11131d);border-color:#f59e0b40}
.q4{background:linear-gradient(135deg,#1e2235,#11131d)}
.q-head{display:flex;justify-content:space-between;font-size:.8rem;font-weight:700;margin-bottom:10px}
.q-head span{padding:3px 8px;border-radius:20px;font-size:.7rem}
.task{background:#1a1d2e;border:1px solid var(--b);padding:10px 12px;border-radius:10px;margin:6px 0;cursor:grab;display:flex;justify-content:space-between;align-items:center}
.task.meta{font-size:.7rem;color:var(--m)}
.task button{background:transparent;border:none;color:var(--m);cursor:pointer;margin-left:6px}
.inbox{min-height:80px;border:2px dashed var(--b);border-radius:12px;padding:10px}
.input{width:100%;background:#0c0e18;border:1px solid var(--b);color:var(--t);padding:10px;border-radius:8px;margin:6px 0}
.btn{background:var(--p);color:white;border:none;padding:10px 16px;border-radius:8px;cursor:pointer;font-weight:600;width:100%}
.btn:hover{opacity:.9}
.kpi{display:flex;justify-content:space-between;margin:8px 0;font-size:.85rem}
.bar{height:6px;background:var(--b);border-radius:10px;overflow:hidden}
.fill{height:100%;background:var(--p);transition:.3s}
.hidden{display:none}
</style>
</head>
<body>
<div class="wrap">
<div class="hdr">
<h1>🧭 Task Compass</h1>
<p style="color:var(--m)">Tech Company Edition - Prioritize like a PM at FAANG - Day 37</p>
</div>

<div class="grid">
<div class="card">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
<strong>Priority Matrix</strong>
<span style="color:var(--m);font-size:.8rem">Drag tasks to compass →</span>
</div>
<div class="compass">
<div class="quadrant q1" id="q1" ondrop="drop(event,'q1')" ondragover="allow(event)">
<div class="q-head">🔥 Q1 Do First <span style="background:#ef4444;color:white">Urgent + Important</span></div>
<div id="list-q1"></div>
</div>
<div class="quadrant q2" id="q2" ondrop="drop(event,'q2')" ondragover="allow(event)">
<div class="q-head">🎯 Q2 Schedule <span style="background:#6366f1;color:white">Important, Not Urgent</span></div>
<div id="list-q2"></div>
</div>
<div class="quadrant q3" id="q3" ondrop="drop(event,'q3')" ondragover="allow(event)">
<div class="q-head">⚡ Q3 Delegate <span style="background:#f59e0b;color:white">Urgent, Not Important</span></div>
<div id="list-q3"></div>
</div>
<div class="quadrant q4" id="q4" ondrop="drop(event,'q4')" ondragover="allow(event)">
<div class="q-head">🗑️ Q4 Eliminate <span style="background:#374151;color:white">Low Value</span></div>
<div id="list-q4"></div>
</div>
</div>
</div>

<div>
<div class="card">
<h3>📥 Inbox - Tech Tasks</h3>
<p style="color:var(--m);font-size:.8rem;margin:6px 0">Add or drag default tasks to compass</p>
<div class="inbox" id="inbox" ondrop="drop(event,'inbox')" ondragover="allow(event)"></div>
<input id="newTaskTitle" class="input" placeholder="Task title: e.g., Fix production bug in payment API">
<select id="newTaskType" class="input">
<option value="Engineering">Engineering</option>
<option value="Product">Product</option>
<option value="Design">Design</option>
<option value="On-Call">On-Call</option>
<option value="Meeting">Meeting</option>
</select>
<button class="btn" onclick="addCustom()">+ Add Task</button>

<div style="margin-top:16px">
<div class="kpi"><span>Focus Score</span><span id="focus">0%</span></div>
<div class="bar"><div id="focusBar" class="fill" style="width:0%"></div></div>
<div class="kpi"><span>Q2 Time (Deep Work)</span><span id="q2count">0</span></div>
<div class="kpi"><span>Tech Debt in Q4</span><span id="q4count">0 eliminated</span></div>
</div>

<button class="btn" style="margin-top:14px;background:#10b981" onclick="generateReport()">Generate Sprint Report →</button>
</div>

<div id="report" class="card hidden">
<h3>📊 Sprint Compass Report</h3>
<div id="reportContent" style="font-size:.9rem;line-height:1.6;color:var(--m);margin-top:8px"></div>
</div>
</div>
</div>
</div>

<script>
const defaultTasks=[
{title:"Production incident: Checkout API down",type:"On-Call",impact:"High",suggest:"q1"},
{title:"Design system migration for dashboard",type:"Engineering",impact:"High",suggest:"q2"},
{title:"Q3 roadmap planning with leadership",type:"Product",impact:"High",suggest:"q2"},
{title:"Reply to 20 Slack threads about office party",type:"Meeting",impact:"Low",suggest:"q4"},
{title:"Fix typo in internal wiki",type:"Engineering",impact:"Low",suggest:"q3"},
{title:"Security audit for auth service - due tomorrow",type:"Engineering",impact:"Critical",suggest:"q1"},
{title:"Mentor junior engineers - 1:1s",type:"Product",impact:"Medium",suggest:"q2"},
{title:"Refactor legacy payment code (no deadline)",type:"Engineering",impact:"Medium",suggest:"q2"},
{title:"Approve expense reports",type:"Meeting",impact:"Low",suggest:"q3"},
{title:"Watch tech talk recording",type:"Product",impact:"Low",suggest:"q4"},
];

let state={inbox:[...defaultTasks],q1:[],q2:[],q3:[],q4:[]};

function render(){
['inbox','q1','q2','q3','q4'].forEach(k=>{
let el=document.getElementById(k==='inbox'?'inbox':`list-${k}`);
el.innerHTML='';
state[k].forEach((t,i)=>{
let d=document.createElement('div');d.className='task';d.draggable=true;
d.innerHTML=`<div><div>${t.title}</div><div class="meta">${t.type} • ${t.impact}</div></div><div><button onclick="remove('${k}',${i})">✕</button></div>`;
d.ondragstart=e=>e.dataTransfer.setData('id',`${k}-${i}`);
el.appendChild(d);
});
});
let total=state.q1.length+state.q2.length+state.q3.length+state.q4.length;
let focus = total? Math.round((state.q1.length*1 + state.q2.length*1.5)/total*50):0;
if(focus>100) focus=100;
document.getElementById('focus').textContent=focus+'%';
document.getElementById('focusBar').style.width=focus+'%';
document.getElementById('q2count').textContent=state.q2.length+' tasks';
document.getElementById('q4count').textContent=state.q4.length+' eliminated';
}

function allow(e){e.preventDefault()}
function drop(e,target){
e.preventDefault();
let id=e.dataTransfer.getData('id');
if(!id) return;
let [from,idx]=id.split('-'); idx=parseInt(idx);
let task=state[from][idx];
state[from].splice(idx,1);
if(target==='inbox') state.inbox.push(task);
else state[target].push(task);
render();
}

function remove(k,i){state[k].splice(i,1);render()}
function addCustom(){
let title=document.getElementById('newTaskTitle').value.trim();
let type=document.getElementById('newTaskType').value;
if(!title) return alert('Enter task');
state.inbox.push({title,type,impact:"Medium",suggest:"q2"});
document.getElementById('newTaskTitle').value='';
render();
}

function generateReport(){
let q1=state.q1,q2=state.q2,q3=state.q3,q4=state.q4;
let score= q2.length*30 + q1.length*20 - q3.length*5 + q4.length*10;
if(score<0) score=10;
let grade= score>150?'Staff Engineer Level Focus':score>90?'Senior PM Level':score>50?'Good balance':'Firefighting Mode';
document.getElementById('report').classList.remove('hidden');
document.getElementById('reportContent').innerHTML=`
<b>Focus Grade:</b> ${grade} (${score} pts)<br><br>
<b>Q1 Do First (${q1.length}):</b> ${q1.map(t=>t.title).join(', ')||'None - great!'}<br>
<b>Q2 Deep Work (${q2.length}):</b> ${q2.map(t=>t.title).join(', ')||'Need more Q2 time'}<br>
<b>Q3 Delegate (${q3.length}):</b> ${q3.length} tasks you should delegate/automate<br>
<b>Q4 Eliminated (${q4.length}):</b> ${q4.length*30} mins saved<br><br>
<hr style="margin:8px 0;border-color:#1e2235">
<b>AI Coach Prompt:</b><br>
<pre style="background:#0c0e18;padding:10px;border-radius:8px;white-space:pre-wrap;margin-top:6px">You are my tech lead coach. My tasks:
Q1: ${JSON.stringify(q1.map(t=>t.title))}
Q2: ${JSON.stringify(q2.map(t=>t.title))}
Give me a 3-step plan to protect 4h deep work tomorrow.</pre>
`;
window.scrollTo({top:document.body.scrollHeight,behavior:'smooth'});
}

render();
</script>
</body>
</html>
