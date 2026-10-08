# Claude Challenge - Day 32: Think Like a Marketing Strategist
# Task: Grow This Brand

brand = {
    "name": "BrewSoul - Organic Coffee",
    "product": "Premium Organic Coffee",
    "current_problem": "Low Instagram reach, no repeat customers",
    "goal": "10k followers + 3x sales in 30 days"
}

print(f"BRAND: {brand['name']} | GOAL: {brand['goal']}\n")

# 1. SWOT Analysis - Strategist jaisa sochna
print("=== 1. SWOT ANALYSIS ===")
print("""
Strength: Organic, Direct from farmers
Weakness: High price, Low awareness
Opportunity: Gen-Z loves sustainable brands
Threat: Big brands like Starbucks
""")

# 2. Target Persona
print("=== 2. TARGET PERSONA ===")
print("""
Name: Aman, 24, Working Professional
Pain: Needs energy but hates bitter, chemical coffee
Platform: Instagram Reels (8-10 PM), LinkedIn
Buying Trigger: Reels + Free sample + COD
""")

# 3. 3 Content Pillars
print("=== 3. CONTENT PILLARS (30 Days Plan) ===")
pillars = {
    "Pillar 1 - Educate (40%)": "Reel: 'Why your coffee is bitter? 3 mistakes'",
    "Pillar 2 - Social Proof (30%)": "UGC: Customer making coffee at office",
    "Pillar 3 - Brand Story (30%)": "Founder visiting farm in Chikmagalur"
}
for k,v in pillars.items():
    print(f"{k} -> {v}")

# 4. Growth Funnel - TOFU MOFU BOFU
print("\n=== 4. GROWTH FUNNEL ===")
print("""
TOFU (Awareness): 3 Reels/week + 5 Micro-influencers (10k followers) = Target 100k Reach
MOFU (Consideration): WhatsApp Community + Free Sample + 10% OFF Code
BOFU (Conversion): Retargeting Ad + Testimonial + Limited Offer (48hr)
Metric: Reach, Save Rate, CTR, Conversion%
""")

# 5. 30-Day Action Plan
print("=== 5. 30-DAY ACTION PLAN ===")
for day, task in [(1,"Launch 3 Reels"), (7,"Influencer collab"), (15,"Giveaway Contest"), (30,"Sales Report")]:
    print(f"Day {day}: {task}")

print("\nProof of Work Ready -> Screenshot lo aur upload kardo!")
