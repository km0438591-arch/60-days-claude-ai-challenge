# Day 13: Connect Indeed with Claude & Build Your AI Job Search Assistant
# By Kanchan from Kanpur - Auto Job Filter

print("🤖 Day 13: AI Job Search Assistant - Indeed + Claude")

# Mock Indeed Jobs (Real me Claude API + Indeed scraper lagta hai)
indeed_jobs = [
    {"title": "Production Engineer", "company": "VVDN", "location": "Manesar, Gurgaon", "salary": "17000", "desc": "6 days working, 12hr shift, no WFH"},
    {"title": "AI Intern - Remote", "company": "GrowthX AI Startup", "location": "Remote", "salary": "15000 + Certificate", "desc": "Claude AI, Prompt Engineering, Python, Build AI dashboards, WFH"},
    {"title": "HR Executive", "company": "Local Factory Kanpur", "location": "Kanpur", "salary": "12000", "desc": "Hiring, no growth"},
    {"title": "Prompt Engineer Intern", "company": "ClaudeVerse", "location": "Remote", "salary": "25000", "desc": "Remote, Claude Artifacts, Streamlit, GitHub portfolio needed"},
    {"title": "Customer Support", "company": "Call Center", "location": "Noida", "salary": "18000", "desc": "Night shift"},
]

def claude_job_filter(job):
    """Claude's logic to filter jobs"""
    red_flags = ["6 days working", "12hr shift", "VVDN", "Night shift", "no growth"]
    green_flags = ["Remote", "WFH", "Claude", "Prompt Engineering", "Python", "GitHub", "Internship", "AI"]

    score = 0
    reason = []

    for flag in red_flags:
        if flag.lower() in job["desc"].lower() or flag.lower() in job["company"].lower():
            score -= 50
            reason.append(f"RED FLAG: {flag}")

    for flag in green_flags:
        if flag.lower() in job["desc"].lower():
            score += 20
            reason.append(f"GREEN FLAG: {flag}")

    return score, reason

def ai_job_assistant():
    print("Scanning 5 jobs from Indeed for Kanchan (Kanpur -> Remote AI)...\n")
    
    good_jobs = []
    for job in indeed_jobs:
        score, reasons = claude_job_filter(job)
        status = "✅ APPLY" if score > 30 else "❌ SKIP"
        
        print(f"--- {job['title']} @ {job['company']} ({job['location']}) ---")
        print(f"Salary: {job['salary']} | Score: {score} | {status}")
        print(f"Reason: {', '.join(reasons)}")
        print(f"Description: {job['desc']}\n")
        
        if score > 30:
            good_jobs.append(job)

    print("="*50)
    print(f"🤖 Claude's Final Suggestion for Kanchan:")
    print(f"Found {len(good_jobs)} good jobs out of {len(indeed_jobs)}")
    for j in good_jobs:
        print(f"-> APPLY NOW: {j['title']} at {j['company']} - {j['location']} - {j['salary']}")
        # Auto Generate Cover Letter
        print(f"   Claude Auto Cover Letter: 'Hi {j['company']}, I built 13 AI projects with Claude, my GitHub: km0438591-arch...'")
    
    print("\nAction: VVDN type jobs ko SKIP, Remote AI walo pe APPLY")

ai_job_assistant()
print("\nDay 13 Complete - AI Job Search Assistant Ready!")
