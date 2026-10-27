<!DOCTYPE html>
<html>
<head>
<title>Defend Your Experience - Kanchan</title>
<style>
body{font-family:Arial;background:#f0f4ff;padding:20px}
h1{color:#6a00ff;text-align:center}
.card{background:white;padding:20px;border-radius:20px;box-shadow:0 2px 15px #ccc;max-width:600px;margin:auto}
button{background:#6a00ff;color:white;border:none;padding:10px 20px;border-radius:20px;cursor:pointer;margin:5px}
textarea{width:100%;height:80px;border-radius:10px;padding:10px}
#score{font-size:22px;font-weight:bold;color:green}
</style>
</head>
<body>
<h1>🎤 Defend Your Experience</h1>
<p style="text-align:center">AI-Powered Adaptive Interview Defense Simulator | Day 47/60 | Kanchan Maurya</p>

<div class="card">
<p><b>Level:</b> <span id="level">Easy 🟢</span> | <b>Score:</b> <span id="score">0</span>/100</p>
<h3 id="question">Q1. Tell me about yourself?</h3>
<textarea id="ans" placeholder="Apna jawab yaha likho... e.g. I am Kanchan from Kanpur, I did Sales Executive at Shapoorji..."></textarea>
<br><br>
<button onclick="checkAns()">Submit Answer ✅</button>
<button onclick="nextQ()">Next Question ➡️</button>
<p id="feedback" style="background:#fff3cd;padding:10px;border-radius:10px"></p>
</div>

<div class="card" style="margin-top:15px">
<h3>🔥 Practice Questions - Tere Liye</h3>
<p>1. Why should we hire you?</p>
<p>2. What did you do in Shapoorji Pallonji?</p>
<p>3. How did you handle a difficult customer?</p>
<p>4. Where do you see yourself in 2 years?</p>
</div>

<script>
let questions=[
"Tell me about yourself?",
"What did you do in Shapoorji Pallonji as Sales Executive?",
"Why should we hire you for Sales?",
"How did you handle a difficult customer in Gurgaon?",
"Your communication is weak, how will you improve?"
];
let i=0, score=0;
function nextQ(){i++; if(i>=questions.length) i=0; document.getElementById('question').innerText="Q"+(i+1)+". "+questions[i]; document.getElementById('feedback').innerText="";}
function checkAns(){
let a=document.getElementById('ans').value;
if(a.length<20){document.getElementById('feedback').innerText="⚠️ Thoda lamba jawab do baby - 2-3 line me bolo - Confidence se!"; return;}
score+=20; document.getElementById('score').innerText=score;
let lvl = score<40 ? "Easy 🟢" : score<80 ? "Medium 🟡" : "Hard 🔴 - Expert Level!";
document.getElementById('level').innerText=lvl;
document.getElementById('feedback').innerText="✅ Good Answer Kanchan! Score +20 | Tip: Add numbers - 'Maine 10 site visits karwaye' - aise bolo to 10/10 milega | Next level: "+lvl;
}
</script>
</body>
</html>
