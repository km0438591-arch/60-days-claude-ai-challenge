<!DOCTYPE html>
<html>
<head>
<title>Kanchan's Personal AI Playbook</title>
<style>
body{font-family:Arial;background:#fff5f8;padding:20px}
h1{color:#ff2e63;text-align:center}
.card{background:white;padding:15px;border-radius:15px;box-shadow:0 2px 10px #ccc;margin:15px 0}
button{background:#ff2e63;color:white;border:none;padding:8px 15px;border-radius:20px;cursor:pointer}
textarea{width:100%;height:60px;border-radius:10px;padding:10px}
</style>
</head>
<body>
<h1>📖 My Personal AI Playbook - Kanchan</h1>
<p style="text-align:center">Consistency Today, Expertise Tomorrow ✨ | Day 46/60</p>

<div class="card">
<h3>1. 💼 Job / Interview Playbook</h3>
<p>Prompt: "Write a professional mail to HR for accepting offer..."</p>
<button onclick="copyText(this)">Copy Prompt</button>
</div>

<div class="card">
<h3>2. 🏠 Sales Playbook - Shapoorji</h3>
<p>Prompt: "Write a WhatsApp message to customer for site visit in Sector-58 Gurgaon, polite and professional"</p>
<button onclick="copyText(this)">Copy Prompt</button>
</div>

<div class="card">
<h3>3. 📝 LinkedIn Caption Playbook</h3>
<p>Prompt: "Write LinkedIn caption for 60 Days Claude Challenge Day 46"</p>
<button onclick="copyText(this)">Copy Prompt</button>
</div>

<div class="card">
<h3>4. ✍️ Apna Prompt Add Karo</h3>
<textarea id="myPrompt" placeholder="Apna favourite prompt yaha likho..."></textarea>
<button onclick="savePrompt()">Save My Prompt</button>
<p id="saved"></p>
</div>

<script>
function copyText(btn){navigator.clipboard.writeText(btn.previousElementSibling.innerText); btn.innerText="Copied ✅"}
function savePrompt(){document.getElementById('saved').innerText="Saved ✅ : "+document.getElementById('myPrompt').value}
</script>
</body>
</html>
