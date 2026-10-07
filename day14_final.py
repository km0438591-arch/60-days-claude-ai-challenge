# Day 14: Detect Job Red Flags - Protect Your Career from Toxic Jobs
# By Kanchan from Kanpur - Personal Experience Based

print("🚩 Day 14: Job Red Flags Detector - Kanpur Edition")

# Red Flag Database - Aapke VVDN interview se + common toxic patterns
red_flag_rules = {
    "LOW_SALARY_TRAP": {"keywords": ["17k", "12k", "15k for engineer", "stipend 5000"], "severity": "HIGH", "advice": "Kanpur me bhi fresher AI intern ko 20k+ milta hai. 17k factory me waste hai."},
    "FAKE_WFH": {"keywords": ["WFH but", "hybrid but 6 days office", "remote initially"], "severity": "MEDIUM", "advice": "Puch lo - permanent WFH hai ya 1 month ka jhooth?"},
    "LONG_HOURS": {"keywords": ["12hr shift", "6 days working", "9am to 9pm", "sunday working"], "severity": "HIGH", "advice": "Ye burnout factory hai. AI career me 6 days nahi hota."},
    "BOND_TRAP": {"keywords": ["2 year bond", "3 year agreement", "original documents submit", "1 lakh penalty"], "severity": "CRITICAL", "advice": "BOND = RED ALERT. Kabhi original documents mat do!"},
    "NO_GROWTH": {"keywords": ["production", "same work daily", "no learning", "call center"], "severity": "MEDIUM", "advice": "AI Engineer ko production line pe nahi lagna. Skill growth zero."},
    "LOCATION_TRAP": {"keywords": ["Manesar", "remote area", "no transport", "Gurgaon far"], "severity": "MEDIUM", "advice": "Kanpur se Manesar 500km, rent 8k, bachega kya? Remote lo."}
}

def detect_red_flags(job_desc):
    print(f"\n--- Scanning Job: {job_desc} ---\n")
    found_flags = []

    for flag_type, rule in red_flag_rules.items():
        for keyword in rule["keywords"]:
            if keyword.lower() in job_desc.lower():
                found_flags.append((flag_type, keyword, rule["severity"], rule["advice"]))

    if not found_flags:
        print("✅ GREEN FLAG: No Red Flags Found! Safe to apply.")
        return True
    else:
        print(f"🚨 {len(found_flags)} RED FLAGS DETECTED!")
        for flag_type, keyword, severity, advice in found_flags:
            print(f" [{severity}] {flag_type} -> Found '{keyword}'")
            print(f" 💡 Claude Advice: {advice}\n")

        # Final Verdict
        critical_count = sum(1 for f in found_flags if f[2] == "CRITICAL")
        high_count = sum(1 for f in found_flags if f[2] == "HIGH")

        if critical_count > 0 or high_count >= 2:
            print("⛔ FINAL VERDICT: DO NOT APPLY - TOXIC JOB - PROTECT YOUR CAREER")
        else:
            print("⚠️ FINAL VERDICT: APPLY WITH CAUTION - Ask HR these questions first")
        return False

# --- TEST CASES - Kanchan's Real Examples ---

# Test 1: Your VVDN Experience
detect_red_flags("VVDN Manesar Production Engineer, 17000 salary, 6 days working, 12hr shift, 2 year bond, original documents submit")

print("\n" + "="*70)

# Test 2: Good Remote AI Job
detect_red_flags("AI Intern Remote, 25000 stipend, Claude AI, Prompt Engineering, WFH, Mentorship, GitHub portfolio needed, No bond")

print("\n" + "="*70)

# Test 3: Another Trap
detect_red_flags("Kanpur Factory HR Executive 12k salary, 9am to 9pm, Sunday working, no growth")

print("\nDay 14 Complete - Red Flag Detector Ready!")
print("Mission: Help 1000 Kanpur students avoid 17k trap")
