<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Day 38 - Typing Speed Studio</title>
<style>
:root{--bg:#09090b;--card:#18181b;--b:#27272a;--p:#22d3ee;--t:#fafafa;--m:#a1a1aa;--ok:#22c55e;--bad:#ef4444}
*{margin:0;padding:0;box-sizing:border-box;font-family:'JetBrains Mono',monospace}
body{background:var(--bg);color:var(--t);padding:18px}
.wrap{max-width:900px;margin:auto}
.hdr{text-align:center;padding:26px 0}
.hdr h1{font-size:2.5rem;background:linear-gradient(90deg,#22d3ee,#a78bfa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-family:Inter,sans-serif}
.card{background:var(--card);border:1px solid var(--b);border-radius:16px;padding:20px;margin:14px 0}
.top{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.kpi span{color:var(--m);font-size:.8rem;font-family:Inter,sans-serif}
.kpi h2{font-size:1.8rem}
.modes{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0}
.mode{padding:8px 14px;border-radius:20px;border:1px solid var(--b);background:transparent;color:var(--m);cursor:pointer;font-family:Inter,sans-serif}
.mode.active{background:var(--p);color:#000;border-color:var(--p);font-weight:700}
.text-box{background:#0f0f10;border:1px solid var(--b);border-radius:12px;padding:20px;font-size:1.2rem;line-height:2;min-height:160px;letter-spacing:.5px;position:relative}
.word{margin-right:8px;display:inline-block}
.word.correct{color:var(--ok)}
.word.wrong{color:var(--bad);text-decoration:underline}
.word.current{background:#22d3ee20;border-radius:4px;padding:0 4px;border-bottom:2px solid var(--p)}
.char.correct{color:var(--t)}
.char.wrong{color:var(--bad);background:#ef444420}
.input{width:100%;background:transparent;border:none;outline:none;color:transparent;position:absolute;top:0;left:0;height:100%;cursor:default}
.stats-bar{display:flex;justify-content:space-between;margin-top:14px}
.btn{background:var(--p);color:#000;font-weight:700;border:none;padding:10px 18px;border-radius:8px;cursor:pointer;font-family:Inter,sans-serif}
.btn2{background:transparent;border:1px solid var(--b);color:var(--t);padding:10px 18px;border-radius:8px;cursor:pointer;font-family:Inter,sans-serif}
.bar{height:6px;background:var(--b);border-radius:10px;overflow:hidden;margin:8px 0}
.fill{height:100%;background:var(--p);transition:width.2s}
.hidden{display:none}
</style>
</head>
<body>
<div class="wrap">
<div class="hdr">
<h1>Typing Speed Studio</h1>
<p style="color:var(--m);font-family:Inter,sans-serif">Train like a pro - WPM, Accuracy, Focus Mode - Day 38</p>
</div>

<div class="top">
<div class="card kpi"><span>WPM</span><h2 id="wpm">0</h2></div>
<div class="card kpi"><span>Accuracy</span><h2 id="acc">100%</h2></div>
<div class="card kpi"><span>Time</span><h2 id="time">60s</h2></div>
<div class="card kpi"><span>Streak</span><h2 id="streak">0</h2></div>
</div>

<div class="card">
<div class="modes">
<button class="mode active" onclick="setMode('code')">👨‍💻 Code Mode</button>
<button class="mode" onclick="setMode('quotes')">💬 Quotes</button>
<button class="mode" onclick="setMode('tech')">🚀 Tech Terms</button>
<button class="mode" onclick="setMode('claude')">🤖 Claude Prompts</button>
<select id="timeSel" class="mode" onchange="setTime(this.value)"><option value="30">30s</option><option value="60" selected>60s</option><option value="120">120s</option></select>
</div>

<div class="text-box" id="textBox" onclick="focusInput()">
<div id="words"></div>
<input id="hiddenInput" class="input" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false">
</div>

<div class="bar"><div id="progress" class="fill" style="width:0%"></div></div>

<div class="stats-bar">
<button class="btn" onclick="restart()">↻ Restart (Tab)</button>
<button class="btn2" onclick="showResult()">📊 Studio Report</button>
<span style="color:var(--m);font-size:.8rem;font-family:Inter,sans-serif">Click text and start typing. Esc to pause.</span>
</div>
</div>

<div id="result" class="card hidden">
<h2 style="font-family:Inter,sans-serif">🏆 Studio Report</h2>
<div id="resultContent" style="margin-top:10px;line-height:1.8"></div>
<div style="margin-top:12px;display:flex;gap:10px">
<button class="btn" onclick="restart()">Practice Again</button>
<button class="btn2" onclick="copyPrompt()">Copy AI Coach Prompt</button>
</div>
</div>
</div>

<script>
const data={
code:["function debounce(fn, delay){ let timer; return (...args)=>{ clearTimeout(timer); timer=setTimeout(()=>fn(...args), delay); }; }","const result = await Promise.all(tasks.map(async t=> await process(t)));","if (!user ||!user.emailVerified) throw new Error('Unauthorized');","git commit -m 'feat: add typing studio with WPM tracker'"],
quotes:["The best time to plant a tree was 20 years ago. The second best time is now.","Code is like humor. When you have to explain it, it's bad.","First, solve the problem. Then, write the code.","Simplicity is the soul of efficiency."],
tech:["Kubernetes orchestrates containerized microservices across distributed clusters with auto-scaling.","Prompt engineering requires context, role definition, task specificity, and output constraints.","Vector databases enable semantic search via embeddings and cosine similarity.","CI CD pipeline automates build test deploy with GitHub Actions."],
claude:["You are a senior tech writer. Context: audience is developers. Task: Explain event loop in 200 words. Format: bullet points with example.","Role: Code reviewer. Task: Find 3 security issues in this Node.js code. Constraint: Explain fix with OWASP reference.","Create a Claude prompt that generates unit tests with 90 percent coverage for React components."]
};

let mode='code',timeLimit=60,timeLeft=timeLimit,timer=null,started=false,currentWord=0,currentChar=0,correctChars=0,wrongChars=0,wordsList=[],typedHistory=[],bestWpm=0;

function setMode(m){mode=m;document.querySelectorAll('.mode').forEach(b=>b.classList.toggle('active',b.textContent.toLowerCase().includes(m)));restart()}
function setTime(v){timeLimit=parseInt(v);restart()}
function focusInput(){document.getElementById('hiddenInput').focus()}

function generateWords(){
let pool=data[mode];
let text=pool[Math.floor(Math.random()*pool.length)];
if(mode!=='code' && Math.random()>0.5) text+= " " + pool[Math.floor(Math.random()*pool.length)];
return text.split(/\s+/);
}

function renderWords(){
let container=document.getElementById('words');
container.innerHTML='';
wordsList.forEach((w,i)=>{
let span=document.createElement('span');span.className='word'+(i===currentWord?' current':'');span.id=`w-${i}`;
if(i<typedHistory.length){
let typed=typedHistory[i];
if(typed===w) span.classList.add('correct');else span.classList.add('wrong');
}
span.textContent=w+' ';
container.appendChild(span);
});
}

function restart(){
clearInterval(timer);started=false;timeLeft=timeLimit;currentWord=0;currentChar=0;correctChars=0;wrongChars=0;typedHistory=[];wordsList=generateWords();
document.getElementById('time').textContent=timeLeft+'s';
document.getElementById('wpm').textContent='0';
document.getElementById('acc').textContent='100%';
document.getElementById('streak').textContent='0';
document.getElementById('progress').style.width='0%';
document.getElementById('result').classList.add('hidden');
document.getElementById('hiddenInput').value='';
renderWords();focusInput();
}

document.getElementById('hiddenInput').addEventListener('keydown',e=>{
if(!started && e.key.length===1){started=true;startTimer()}
if(e.key===' '){
e.preventDefault();
let typed=document.getElementById('hiddenInput').value.trim();
if(!typed) return;
typedHistory[currentWord]=typed;
if(typed===wordsList[currentWord]){correctChars+=typed.length; document.getElementById('streak').textContent=parseInt(document.getElementById('streak').textContent)+1}
else{wrongChars+=1; document.getElementById('streak').textContent='0'}
currentWord++;
document.getElementById('hiddenInput').value='';
if(currentWord>=wordsList.length){wordsList=wordsList.concat(generateWords())}
renderWords();updateStats();
}else if(e.key==='Backspace'){
// allow
}
});

document.getElementById('hiddenInput').addEventListener('input',updateStats);

function startTimer(){
timer=setInterval(()=>{
timeLeft--;document.getElementById('time').textContent=timeLeft+'s';
document.getElementById('progress').style.width=`${(1-timeLeft/timeLimit)*100}%`;
if(timeLeft<=0){clearInterval(timer);showResult()}
},1000);
}

function updateStats(){
let total=correctChars+wrongChars;
let acc= total? Math.round(correctChars/total*100):100;
let minutes=(timeLimit-timeLeft)/60||0.1;
let wpm= minutes>0? Math.round((correctChars/5)/minutes):0;
if(wpm>bestWpm) bestWpm=wpm;
document.getElementById('wpm').textContent=wpm;
document.getElementById('acc').textContent=acc+'%';
}

function showResult(){
clearInterval(timer);
let wpm=parseInt(document.getElementById('wpm').textContent);
let acc=document.getElementById('acc').textContent;
let totalWords=typedHistory.length;
document.getElementById('result').classList.remove('hidden');
let level=wpm>80?'Elite - FAANG Ready':wpm>60?'Pro - Senior Dev':wpm>40?'Intermediate - Keep Grinding':'Beginner - Daily 15min';
document.getElementById('resultContent').innerHTML=`
<p><b>WPM:</b> ${wpm} | <b>Accuracy:</b> ${acc} | <b>Words:</b> ${totalWords}</p>
<p><b>Level:</b> ${level}</p>
<p><b>Best:</b> ${bestWpm} WPM</p>
<hr style="margin:10px 0;border-color:#27272a">
<b>Analysis:</b> ${acc.replace('%','')<90?'Focus on accuracy before speed - slow down 10%.':'Great accuracy! Now push speed with code mode.'} ${wpm<50?'Practice 2-finger to 10-finger transition.':''}
<br><br>
<b>Your Growth Plan:</b><br>
• Today: 3 rounds in ${mode} mode<br>
• Tomorrow: Switch to tech mode for vocab<br>
• Goal: ${wpm+10} WPM in 7 days
`;
window.scrollTo({top:document.body.scrollHeight,behavior:'smooth'});
}

function copyPrompt(){
let wpm=document.getElementById('wpm').textContent;
let prompt=`You are my typing coach. My stats: ${wpm} WPM, Mode: ${mode}, Accuracy: ${document.getElementById('acc').textContent}. Give me a 7-day plan to reach ${parseInt(wpm)+15} WPM with 15min daily drills.`;
navigator.clipboard.writeText(prompt);alert('Copied coach prompt!');
}

document.addEventListener('keydown',e=>{if(e.key==='Tab'){e.preventDefault();restart()} if(e.key==='Escape'){clearInterval(timer)}});

restart();
</script>
</body>
</html>
