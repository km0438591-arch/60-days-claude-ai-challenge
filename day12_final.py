# Day 12: Build Your Complete Job Search & Personal Branding Toolkit with Claude
# By Kanchan from Kanpur

print("🚀 Day 12: Job Search & Personal Branding Toolkit")

# --- TOOLKIT 1: LinkedIn Headline Generator ---
def generate_linkedin_headline():
    headline = "AI Tools Developer | Claude AI | Prompt Engineering | Python | Building AI for Bharat's Small Businesses | Kanpur -> Remote | 60 Days Claude Challenge"
    about = """
    From Kanpur, building AI tools that actually help small businesses.

    🔧 I build: Kirana Dashboards, Nutrition Apps, Supply Chain Control Towers with Claude AI
    🎯 Learning: 60 Days Claude Challenge by ABTalks (Day 12/60)
    💡 Focus: Prompt Engineering, Claude Artifacts, Function Calling, Streamlit
    📍 Location: Kanpur, UP - Open to Remote AI Internships
    🔗 Projects: github.com/km0438591-arch/60-days-claude-ai-challenge

    Not looking for factory jobs, looking to build AI products.
    """
    print("\n[1] LINKEDIN HEADLINE:\n", headline)
    print("\n[2] LINKEDIN ABOUT:\n", about)
    return headline

# --- TOOLKIT 2: GitHub README Generator ---
def generate_github_readme():
    readme = """
    # Kanchan | AI Developer from Kanpur
    👩‍💻 Building AI Tools with Claude AI

    ## 🔥 60 Days Claude Challenge Progress
    Day 8: AI Dashboard | Day 9: Nutrition App | Day 10: Portfolio | Day 11: ATS Resume | Day 12: Branding Toolkit

    ## 🛠️ Tech Stack
    Claude AI, Prompt Engineering, Python, Streamlit, Pandas

    ## 🎯 Goal
    Remote AI Internship (Not 17k Factory)
    """
    print("\n[3] GITHUB README:\n", readme)

# --- TOOLKIT 3: Cover Letter Generator ---
def generate_cover_letter(company_name):
    letter = f"""
    Subject: AI Intern Application - Kanchan from Kanpur (Claude AI Projects)

    Hi {company_name} Team,

    I am Kanchan from Kanpur, currently completing 60 Days Claude Challenge.
    I built Kirana Dashboard, Nutrition Analytics App, and Supply Chain Tower using Claude Artifacts.

    My GitHub: https://github.com/km0438591-arch/60-days-claude-ai-challenge
    I am available for Remote Internship and can start immediately.

    Thanks,
    Kanchan
    """
    print(f"\n[4] COVER LETTER FOR {company_name}:\n", letter)

# --- TOOLKIT 4: Daily Job Search Tracker ---
def job_tracker():
    print("\n[5] DAILY JOB SEARCH TRACKER SHEET")
    print("Company | Role | Platform | ATS Score | Applied Date | Status")
    print("VVDN (Reject) | HR | Naukri | 40% | - | RED FLAG - 17k only")
    print("Startup X | AI Intern | Internshala | 95% | Today | APPLIED")
    print("Claude Tool Co | Prompt Engineer Intern | LinkedIn | 92% | Today | APPLIED")

# Run Toolkit
generate_linkedin_headline()
generate_github_readme()
generate_cover_letter("AI Startup Bangalore")
job_tracker()

print("\nDay 12 Complete - Personal Branding Toolkit Ready!")
print("Action: LinkedIn Headline update karo, GitHub README paste karo, 5 jobs pe apply karo")
