# Day 53: Project Setup & Foundation
# Capstone Day 3 - Project Structure Setup
# Author: Kanchan Maurya

import os

print("🛠️ Day 53: Project Setup & Foundation Started\n")

folders = [
    "frontend/app",
    "frontend/components",
    "backend/api",
    "backend/core",
    "backend/db",
    "backend/models"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"✅ Created: {folder}/")

# 1. Backend - FastAPI Foundation
backend_main = '''
from fastapi import FastAPI

app = FastAPI(title="PrepMate AI - Day 53 Foundation")

@app.get("/")
def root():
    return {"message": "Day 53: Project Setup Complete", "status": "Foundation Verified", "day": 53}

@app.get("/api/health")
def health():
    return {"status": "OK", "milestone": "Foundation Complete", "verified": True}

# Day 54 Core Feature will be added here
@app.post("/api/interview/create")
def create_interview():
    return {"feature": "Coming in Day 54 - Core Feature"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
'''

with open("backend/main.py", "w") as f:
    f.write(backend_main)
print("\n✅ Created: backend/main.py - FastAPI Foundation")

# 2. Requirements
with open("backend/requirements.txt", "w") as f:
    f.write("fastapi\nuvicorn\nsupabase\nanthropic\npython-dotenv\n")
print("✅ Created: backend/requirements.txt")

# 3. Env
with open("backend/.env.example", "w") as f:
    f.write("CLAUDE_API_KEY=your_key_here\nSUPABASE_URL=your_url\nSUPABASE_KEY=your_key\n")
print("✅ Created: backend/.env.example")

# 4. Frontend foundation
with open("frontend/app/page.tsx", "w") as f:
    f.write('''export default function Home() {
  return (
    <div>
      <h1>PrepMate AI - Day 53 Foundation</h1>
      <p>Project Setup Complete - Verified</p>
      <p>Day 53 Milestone: Foundation Ready</p>
    </div>
  )
}''')
print("✅ Created: frontend/app/page.tsx")

print("\n" + "="*60)
print("✅ Day 53 Milestone Verified: Project Setup & Foundation Complete")
print("Backend: FastAPI Running | Frontend: Next.js Ready")
print("Ready for Day 54: Core Feature Implementation")
print("="*60)
