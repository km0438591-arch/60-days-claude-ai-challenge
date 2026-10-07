# Day 6: AI Resume Optimizer
# By Kanchan from Kanpur - 60 Days Claude Challenge
# Goal: Optimize resume for AI Internship, not 17k factory job

my_old_resume = """
Name: Kanchan
Location: Kanpur
Skills: Basic Python, MS Word
Looking for: Any job in Noida
"""

# Claude Prompt for Resume Optimization
claude_prompt = """
You are an Expert AI Resume Writer. Optimize this resume:

CONTEXT:
- Candidate: Kanchan from Kanpur, Learning 60 Days Claude AI Challenge
- Target Role: Remote AI Intern / AI Tools Developer for Small Businesses
- Skills to highlight: Claude AI, Prompt Engineering, Context Engineering, Python, GitHub
- Projects: 60-days-claude-ai-challenge (github.com/km0438591-arch/60-days-claude-ai-challenge) - Built 6 AI tools for Kanpur businesses
- Avoid: Factory job keywords

TASK: Rewrite resume in modern format with:
1. Professional Summary (2 lines)
2. Skills (AI Tools, Python, Prompt Engineering)
3. Projects (with GitHub link)
4. Goal

Give output ready to paste.
"""

# Optimized Resume (Output you will get from Claude)
my_new_resume = """
KANCHAN | AI Tools Developer (Kanpur)
GitHub: github.com/km0438591-arch/60-days-claude-ai-challenge | Location: Kanpur (Remote Ready)

PROFESSIONAL SUMMARY:
Aspiring AI Engineer from Kanpur, completed 6/60 Days Claude AI Challenge. Building AI tools for local Kirana, Coaching businesses using Claude, Prompt Engineering.

SKILLS:
- AI: Claude AI, Prompt Engineering, Context Engineering, Role-Based Prompting
- Tech: Python, GitHub, AI Content Generation
- Strength: Consistent builder, Kanpur local business understanding

PROJECTS:
1. Kanpur Business Chatbot (Day 3) - Role-based bot for Kirana queries
2. Zero-Budget Marketing Ideas Generator (Day 5) - Context Engineering use case
3. 60 Days Claude Challenge Portfolio - 6 projects live on GitHub

GOAL: Seeking Remote AI Internship to build AI solutions for Bharat's small businesses.

"""

print("OLD RESUME (Before Claude):")
print(my_old_resume)
print("\nCLAUDE PROMPT USED:")
print(claude_prompt)
print("\nNEW RESUME (After Claude Optimization):")
print(my_new_resume)
print("\nDay 6 Complete - Resume Ready for Internship!")
