# Day 15: Build Your Personal Astrology & Life Analysis Consultant with Claude
# By Kanchan from Kanpur - AI + Logic Based

print("🔮 Day 15: Astrology & Life Analysis Consultant - Kanpur Girl Edition")

def claude_life_consultant(name, birth_month, career_goal):
    print(f"\n--- Life Analysis for {name} | Goal: {career_goal} ---")
    
    # Claude Logic - Not superstitious, but analysis based on data
    # We combine Birth Month analysis + Career Trajectory
    
    life_map = {
        "career_phase": "Transition Phase - Factory Job (17k trap) to AI Engineer",
        "strength": "Hardworking, Self-Learner from Kanpur, 60 Days Challenge Completer",
        "challenge": "Location constraint (Kanpur) but Remote skill will solve it"
    }
    
    print(f"\n📊 Claude's Analysis:")
    print(f"1. Current Phase: {life_map['career_phase']}")
    print(f"2. Strength: {life_map['strength']}")
    print(f"3. Challenge: {life_map['challenge']}")

    # Astrology-style but AI advice
    if "AI" in career_goal or "Intern" in career_goal:
        print(f"\n🔮 Prediction (Data-Based):")
        print(f" - Next 3 Months: 5-7 Remote Internship calls if you apply daily on Internshala")
        print(f" - Lucky Skill: Claude Artifacts + Prompt Engineering")
        print(f" - Avoid: 17k Bond jobs, 12hr shifts")
        print(f" - Action Plan: GitHub daily push, LinkedIn post 2x week")
    
    # Daily Routine Advice
    print(f"\n🧘 Daily Life Planner for {name}:")
    print(f" - Morning (6-8am): 1 Claude Project")
    print(f" - Afternoon (2-4pm): Apply 5 Internships")
    print(f" - Evening (7-8pm): LinkedIn Networking")
    
    print(f"\n💡 Claude's Final Advice: Astrology ke bharose nahi, Actions pe focus karo. Kanpur se Remote tak ka rasta GitHub se hi hai.")

# Test for Kanchan
claude_life_consultant("Kanchan", "Your Birth Month", "Remote AI Internship")

# Test for other user
print("\n" + "="*60)
claude_life_consultant("Student from Itaunja", "March", "AI Developer")

print("\nDay 15 Complete - Life Consultant Ready!")
