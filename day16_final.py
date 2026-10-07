# Day 16: Build a Custom Claude Skill for Stock Research
# By Kanchan from Kanpur - Custom Skill = .md file

print("📈 Day 16: Custom Claude Skill for Stock Research")

# --- This is how a Claude Skill is built ---
# Real me ye file .claude/skills/stock-research/SKILL.md me banti hai

skill_file_content = """
---
name: kanpur-stock-research-skill
description: Research Indian stocks for small investors from Kanpur with AI analysis
author: Kanchan from Kanpur
version: 1.0
---

# Stock Research Skill

## Purpose
Help Kanpur small investors analyze stocks like TCS, Infosys, ITC with Claude.

## Instructions
1. When user says "Analyze TCS", you should:
   - Check 1-year performance
   - Check P/E Ratio
   - Give Risk Level: Low/Medium/High
   - Give suggestion for small investor (5000rs budget)

2. Never give financial advice as guaranteed. Always say "AI analysis, consult advisor"

## Example
User: Analyze ITC
Claude: ITC is FMCG stock, good dividend, Low Risk for 5000 budget. 1 year return ~15%. Good for beginners from Kanpur.

## Tools Used
- Web Search (for live price)
- Python analysis
"""

print("--- SKILL.md File Content ---\n")
print(skill_file_content)

# --- Demo of how the skill works ---
def stock_research_skill(stock_name):
    print(f"\n--- Running Custom Skill: Analyzing {stock_name} ---\n")
    
    # Mock Data (Real me Claude API + Web Search)
    stocks_db = {
        "TCS": {"price": "3900", "pe": "28", "return_1y": "18%", "risk": "Low", "advice": "Best for IT students, stable, good for long term"},
        "ITC": {"price": "460", "pe": "25", "return_1y": "15%", "risk": "Low", "advice": "FMCG, dividend king, 5000 me 10 share aa jayega, beginners ke liye safe"},
        "VVDN": {"price": "Not Listed", "pe": "NA", "return_1y": "NA", "risk": "High", "advice": "Factory job mat lo, stock bhi mat lo - skill banao"},
    }
    
    if stock_name in stocks_db:
        data = stocks_db[stock_name]
        print(f"Stock: {stock_name}")
        print(f"Price: Rs {data['price']}")
        print(f"P/E Ratio: {data['pe']}")
        print(f"1 Year Return: {data['return_1y']}")
        print(f"Risk: {data['risk']}")
        print(f"Claude Advice: {data['advice']}")
        print(f"Disclaimer: AI analysis only, consult financial advisor.")
    else:
        print(f"Claude: {stock_name} ka data nahi mila, par main search karke bata sakta hu!")

# Test the Custom Skill
stock_research_skill("ITC")
stock_research_skill("TCS")
stock_research_skill("VVDN")

print("\n--- How to Install Skill in Claude ---")
print("1. Create folder: .claude/skills/stock-research/")
print("2. Save above content as SKILL.md")
print("3. Restart Claude -> Skill auto-load ho jayega")
print("\nDay 16 Complete - Custom Claude Skill Ready!")
