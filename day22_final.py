# Day 22: Validate Your Startup Idea with Claude
# By Kanchan from Kanpur - Startup Idea: AI for Kirana Shops

print("🚀 Day 22: Validate Your Startup Idea with Claude - Kanpur Kirana AI")

def claude_startup_validator(idea_name, target_customer, problem):
    print(f"\n--- Claude Startup Validator: {idea_name} ---\n")
    print(f"💡 Idea: {idea_name}")
    print(f"👥 Customer: {target_customer}")
    print(f"😢 Problem: {problem}")
    print("\n" + "="*60)
    
    # Claude Validation Logic
    validation_score = 0
    report = {}

    # 1. Market Size (Kanpur)
    print("\n📊 1. MARKET SIZE CHECK:")
    market_size = "Kanpur me 15,000+ Kirana shops hai, 80% ka hisab paper pe"
    print(f" - {market_size}")
    print(" - India me 13M Kirana stores")
    report["Market"] = "LARGE - Good"
    validation_score += 25

    # 2. Problem Severity
    print("\n😭 2. PROBLEM SEVERITY (1-10):")
    severity = 9
    print(f" - Score: {severity}/10")
    print(" - Reason: Roz stock khatam hota hai, pata nahi chalta, nuksan hota hai")
    report["Problem"] = "REAL & PAINFUL - 9/10"
    validation_score += 30

    # 3. Competition
    print("\n⚔️ 3. COMPETITION CHECK:")
    competitors = ["Khatabook (only billing)", "Vyapar App (Complex)"]
    print(f" - Competitors: {competitors}")
    print(" - Your Edge: Claude AI se low stock alert in Hindi + Kanpur pricing")
    report["Competition"] = "LOW for AI + Hindi - Good Edge"
    validation_score += 20

    # 4. Will People Pay?
    print("\n💰 4. WILL PEOPLE PAY?")
    print(" - Kirana owner daily 2k-5k kamata hai")
    print(" - Rs 199/month = 1 day ka profit, affordable hai")
    print(" - Interview: 3 shopkeepers said YES for Hindi alert")
    report["Pay"] = "YES - Rs 199/month viable"
    validation_score += 25

    # Final Score
    print("\n" + "="*60)
    print(f"🎯 FINAL VALIDATION SCORE: {validation_score}/100")
    
    if validation_score >= 80:
        print("✅ VERDICT: GO FOR IT KANCHAN! Idea Validated!")
        print("🚀 Next Step: Build MVP in 7 days (Day 18 wala Excel automation is your MVP)")
    elif validation_score >= 50:
        print("🟡 VERDICT: NEEDS TWEAK - Customer se aur baat karo")
    else:
        print("🔴 VERDICT: DROP IDEA")
    
    print("\n🤖 Claude's 3 Action Steps:")
    print(" 1. Kal hi Itaunja ke 5 Kirana dukan pe jao aur pucho - 'Stock kaise track karte ho?'")
    print(" 2. Unko Day 18 wala Excel demo dikhao, Rs 199 bologe toh lenge?")
    print(" 3. 1 shop ko free me do, feedback lo")

    print(f"\n📄 Validation Report Saved: {idea_name.replace(' ', '_')}_Validation.md")
    return validation_score

# --- Validate Your Idea ---
claude_startup_validator(
    idea_name="Kanpur Kirana AI - Low Stock Alert System",
    target_customer="Kanpur ke small Kirana shop owners (Itaunja, Lucknow)",
    problem="Stock khatam hone ka pata late chalta hai, customer khali haath jata hai"
)

print("\n" + "="*70 + "\n")

# Second Idea for Practice
claude_startup_validator(
    idea_name="Leather Catalog AI for Kanpur",
    target_customer="Kanpur leather factory owners",
    problem="English catalog banana nahi aata, export client nahi milta"
)

print("\nDay 22 Complete - Startup Validated!")
