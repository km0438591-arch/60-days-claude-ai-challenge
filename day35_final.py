<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Prompt Puzzle - Day 35 | ABTalks Claude Challenge</title>
<style>
:root{--bg:#0f0f12;--card:#1a1a1f;--border:#2a2a32;--primary:#8b5cf6;--text:#fff;--muted:#9ca3af}
*{margin:0;padding:0;box-sizing:border-box;font-family:Inter,sans-serif}
body{background:var(--bg);color:var(--text);min-height:100vh;padding:20px}
.container{max-width:900px;margin:auto}
.header{text-align:center;padding:30px 0}
.header h1{font-size:2.5rem;background:linear-gradient(90deg,#8b5cf6,#ec4899);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.card{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:24px;margin:16px 0}
.btn{background:var(--primary);color:white;border:none;padding:12px 24px;border-radius:10px;cursor:pointer;font-weight:600}
.btn:hover{opacity:.9}
.puzzle-area{min-height:200px;border:2px dashed var(--border);border-radius:12px;padding:16px;display:flex;flex-wrap:wrap;gap:10px}
.chip{background:#2a2a32;padding:8px 14px;border-radius:20px;cursor:grab;border:1px solid var(--border);user-select:none}
.chip.dragging{opacity:.5}
.drop-slot{min-width:100px;min-height:40px;background:#111;padding:8px;border-radius:8px;border:1px dashed var(--primary)}
.stats{display:flex;gap:20px;justify-content:space-between}
.stat span{color:var(--muted);font-size:.9rem}
.progress{height:8px;background:var(--border);border-radius:10px;overflow:hidden;margin:10px 0}
.progress-bar{height:100%;background:var(--primary);transition:width.3s}
.option-card{padding:14px;border:1px solid var(--border);border-radius:10px;margin:8px 0;cursor:pointer}
.option-card:hover{border-color:var(--primary)}
.option-card.correct{border-color:#22c55e;background:#22c55e20}
.option-card.wrong{border-color:#ef4444;background:#ef444420}
.hidden{display:none}
</style>
</head>
<body>
<div class="container">
<div class="header">
<h1>Prompt Puzzle</h1>
<p style="color:var(--muted)">Master AI Prompting Through Play - Day 35</p>
</div>

<div class="stats card">
<div><span>Score</span><h3 id="score">0</h3></div>
<div><span>Level</span><h3 id="level">1/6</h3></div>
<div><span>Time</span><h3 id="timer">00:00</h3></div>
<div><button class="btn" onclick="showHint()">💡 Hint</button></div>
</div>

<div class="progress"><div id="progressBar" class="progress-bar" style="width:16%"></div></div>

<div id="gameArea" class="card">
<h2 id="qTitle">Build the Prompt</h2>
<p id="qDesc" style="color:var(--muted);margin:10px 0">Arrange the blocks to create the perfect prompt for the task below.</p>
<div id="taskBox" style="background:#111;padding:12px;border-radius:8px;margin:10px 0;border-left:3px solid var(--primary)"></div>

<div style="margin:15px 0">
<strong>Your Prompt:</strong>
<div id="dropZone" class="puzzle-area"></div>
</div>

<div>
<strong>Blocks:</strong>
<div id="dragZone" class="puzzle-area"></div>
</div>

<div style="margin-top:15px;display:flex;gap:10px">
<button class="btn" onclick="checkAnswer()">Check Prompt</button>
<button class="btn" style="background:transparent;border:1px solid var(--border)" onclick="resetPuzzle()">Reset</button>
</div>
<p id="feedback" style="margin-top:15px"></p>
</div>

<div id="reportArea" class="card hidden">
<h2>🏆 Prompt Performance Report</h2>
<div id="reportContent"></div>
<button class="btn" style="margin-top:15px" onclick="location.reload()">Replay with New Challenges</button>
</div>

</div>

<script>
const challenges=[
{type:"build",title:"Build the Prompt",task:"Write a blog post about Remote Work for developers",desc:"Arrange in correct order: Role + Context + Task + Format + Constraint",blocks:["You are a senior tech writer","Context: Audience is remote developers","Task: Write 500-word blog on remote work productivity","Format: Use bullet points and subheadings","Constraint: Avoid generic advice, give 3 actionable tools"],answer:["You are a senior tech writer","Context: Audience is remote developers","Task: Write 500-word blog on remote work productivity","Format: Use bullet points and subheadings","Constraint: Avoid generic advice, give 3 actionable tools"],hint:"Best order is Role -> Context -> Task -> Format -> Constraint"},
{type:"clean",title:"Clean the Prompt",task:"Fix this bad prompt: 'Write something about AI please do it nicely and fast maybe include some good stuff'",desc:"Remove vagueness, add structure",blocks:["Role: You are an AI researcher","Task: Explain 3 real-world uses of Generative AI in healthcare","Format: 300 words, simple language","Constraint: Include 1 example per use-case"],answer:["Role: You are an AI researcher","Task: Explain 3 real-world uses of Generative AI in healthcare","Format: 300 words, simple language","Constraint: Include 1 example per use-case"],hint:"A good prompt needs specific Role, Task, Format and Constraint"},
{type:"choose",title:"Choose the Best Prompt",task:"Goal: Get Claude to debug a Python error",desc:"Which prompt will give best output?",options:["A) Fix my code","B) You are a senior Python debugger. Here is my error log: [paste]. Explain root cause and give fixed code with 2 test cases.","C) Do my homework please"],correct:1,hint:"Option B has Role + Context + Specific Task"},
{type:"build",title:"Build the Prompt",task:"Create a product description for a smart water bottle",desc:"Build a high-converting prompt",blocks:["Role: E-commerce copywriter for fitness brand","Context: Target is gym-goers, USP is hydration tracking","Task: Write 150-word product description","Format: Persuasive tone + 3 benefits + CTA","Constraint: No jargon, include keywords: smart hydration"],answer:["Role: E-commerce copywriter for fitness brand","Context: Target is gym-goers, USP is hydration tracking","Task: Write 150-word product description","Format: Persuasive tone + 3 benefits + CTA","Constraint: No jargon, include keywords: smart hydration"],hint:"Follow R-C-T-F-C framework"},
{type:"clean",title:"Clean the Prompt",task:"Improve: 'Make a logo prompt for AI'",desc:"Make it usable for Midjourney / Claude",blocks:["Role: Brand designer","Task: Create minimal logo for AI startup named Promptly","Format: Describe style, colors, icon","Constraint: Flat design, vector, white background"],answer:["Role: Brand designer","Task: Create minimal logo for AI startup named Promptly","Format: Describe style, colors, icon","Constraint: Flat design, vector, white background"],hint:"Add specifics"},
{type:"choose",title:"Choose the Best Prompt",task:"Goal: Summarize a 20-page research paper",desc:"Best prompt?",options:["A) Summarize this","B) You are an academic researcher. Summarize this paper in 250 words covering Objective, Method, Findings, Limitations. Keep citations.","C) Make it short"],correct:1,hint:"B follows academic structure"}
];

let current=0,score=0,seconds=0,timerInt;
let userSequence=[];

function startTimer(){timerInt=setInterval(()=>{seconds++;document.getElementById('timer').textContent=`${String(Math.floor(seconds/60)).padStart(2,'0')}:${String(seconds%60).padStart(2,'0')}`},1000)}

function loadChallenge(){
const c=challenges[current];
document.getElementById('level').textContent=`${current+1}/${challenges.length}`;
document.getElementById('progressBar').style.width=`${((current+1)/challenges.length)*100}%`;
document.getElementById('qTitle').textContent=c.title;
document.getElementById('qDesc').textContent=c.desc;
document.getElementById('taskBox').textContent=c.task;
document.getElementById('feedback').textContent='';
userSequence=[];

if(c.type==='choose'){
document.getElementById('dropZone').classList.add('hidden');
document.getElementById('dragZone').innerHTML=c.options.map((o,i)=>`<div class="option-card" onclick="checkChoose(${i})">${o}</div>`).join('');
}else{
document.getElementById('dropZone').classList.remove('hidden');
document.getElementById('dropZone').innerHTML='';
document.getElementById('dragZone').innerHTML='';
document.getElementById('dragZone').classList.remove('hidden');
let blocks=[...c.blocks].sort(()=>Math.random()-0.5);
blocks.forEach(t=>{
let d=document.createElement('div');d.className='chip';d.draggable=true;d.textContent=t;
d.addEventListener('dragstart',e=>{d.classList.add('dragging');e.dataTransfer.setData('text',t)});
d.addEventListener('click',()=>{moveToDrop(t,d)});
document.getElementById('dragZone').appendChild(d);
});
const dz=document.getElementById('dropZone');
dz.ondragover=e=>e.preventDefault();
dz.ondrop=e=>{
e.preventDefault();
let txt=e.dataTransfer.getData('text');
let el=[...document.querySelectorAll('.chip')].find(x=>x.textContent===txt);
if(el) moveToDrop(txt,el);
};
}
}

function moveToDrop(text,el){
el.remove();
let chip=document.createElement('div');chip.className='chip';chip.textContent=text;
chip.onclick=()=>{chip.remove();let nd=document.createElement('div');nd.className='chip';nd.draggable=true;nd.textContent=text;nd.addEventListener('click',()=>moveToDrop(text,nd));document.getElementById('dragZone').appendChild(nd);userSequence=userSequence.filter(x=>x!==text)};
document.getElementById('dropZone').appendChild(chip);
userSequence.push(text);
}

function resetPuzzle(){loadChallenge()}
function showHint(){alert(challenges[current].hint)}

function checkAnswer(){
const c=challenges[current];
if(JSON.stringify(userSequence)===JSON.stringify(c.answer)){
score+=100;document.getElementById('score').textContent=score;
document.getElementById('feedback').innerHTML='<span style="color:#22c55e">✓ Perfect! +100 points. This follows R-C-T-F-C framework.</span>';
setTimeout(next,1200);
}else{
document.getElementById('feedback').innerHTML='<span style="color:#ef4444">✗ Not optimal. Hint: '+c.hint+'</span>';
}
}

function checkChoose(i){
const c=challenges[current];
const cards=document.querySelectorAll('.option-card');
cards.forEach((ca,idx)=>{if(idx===c.correct)ca.classList.add('correct');else if(idx===i)ca.classList.add('wrong')});
if(i===c.correct){score+=100;document.getElementById('score').textContent=score;document.getElementById('feedback').textContent='Correct! Specific prompts > Vague prompts';setTimeout(next,1200)}else{document.getElementById('feedback').textContent='Wrong. Best prompts have Role + Context + Format' ; setTimeout(next,2000)}
}

function next(){
current++;
if(current<challenges.length) loadChallenge();
else showReport();
}

function showReport(){
clearInterval(timerInt);
document.getElementById('gameArea').classList.add('hidden');
document.getElementById('reportArea').classList.remove('hidden');
let rank=score>=500?'Prompt Master':score>=300?'Prompt Crafter':'Prompt Beginner';
document.getElementById('reportContent').innerHTML=`
<p>Final Score: <b>${score}/600</b></p>
<p>Rank: <b>${rank}</b></p>
<p>Time: <b>${seconds}s</b></p>
<p>Accuracy: <b>${Math.round(score/6)}%</b></p>
<hr style="margin:12px 0;border-color:var(--border)">
<h3>Your Prompt DNA</h3>
<p style="color:var(--muted)">Structure: ${score>400?'Excellent':'Needs Improvement'} | Clarity: High | Optimization: ${score>400?'Pro Level':'Learning'}</p>
<h3 style="margin-top:10px">Optimized Master Prompt Template</h3>
<pre style="background:#111;padding:12px;border-radius:8px;white-space:pre-wrap;margin-top:8px">Role: [Define expert role]
Context: [Audience + Background]
Task: [Specific actionable task]
Format: [Word count, tone, structure]
Constraint: [What to avoid/include]
Example: [1 few-shot example]</pre>
`;
}

loadChallenge();startTimer();
</script>
</body>
</html>
