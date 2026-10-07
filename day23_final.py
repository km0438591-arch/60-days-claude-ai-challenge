# Day 23: Build Your Customer & MVP Blueprint with Claude
# By Kanchan from Kanpur - Kirana AI Blueprint

print("📘 Day 23: Customer & MVP Blueprint - Kanpur Kirana AI")

def customer_mvp_blueprint(startup_name):
    print(f"\n--- {startup_name} - Customer & MVP Blueprint ---\n")

    # --- 1. CUSTOMER PERSONA (Claude se banaya) ---
    print("👤 1. CUSTOMER PERSONA:")
    print("   Name: Ramesh Gupta")
    print("   Age: 42, Location: Itaunja, Lucknow (Near Kanpur)")
    print("   Shop: Gupta Kirana Store, Daily Sale: Rs 5000")
    print("   Pain: 'Raat ko hisab likhna padta hai, stock khatam ka pata nahi chalta'")
    print("   Tech: Sirf WhatsApp chalata hai, English nahi aati")
    print("   Goal: 'Dukaan me nuksan band ho, beta time se ghar aaye'")

    # --- 2. CUSTOMER JOURNEY MAP ---
    print("\n🗺️ 2. CUSTOMER JOURNEY (Before vs After):")
    print("   BEFORE: Customer aaya -> Maal nahi hai -> Naraz gaya -> Sale lost (Rs 200)")
    print("   AFTER (Your MVP): Claude AI alert subah 8 baje -> 'Aata 10Kg bacha hai, order karo' -> Sale saved!")

    # --- 3. MVP FEATURES - MoSCoW Method ---
    print("\n🔨 3. MVP BLUEPRINT (Must Have / Should Have / Wont Have):")
    
    mvp = {
        "MUST HAVE (Day 1-7 me banega)": [
            "1. Excel upload -> Low stock list (Day 18 wala code)",
            "2. Hindi Voice Alert - 'Aata khatam hone wala hai'",
            "3. WhatsApp daily report at 8 AM"
        ],
        "SHOULD HAVE (Day 14 me)": [
            "1. Auto supplier ko message",
            "2. Simple profit calculator"
        ],
        "WONT HAVE (Abhi nahi)": [
            "1. Payment gateway",
            "2. Big website - Sirf WhatsApp pe kaam"
        ]
    }

    for category, features in mvp.items():
        print(f"\n   {category}:")
        for f in features:
            print(f"    - {f}")

    # --- 4. CLAUDE PROMPT FOR MVP ---
    print("\n🤖 4. CLAUDE BUILD PROMPT:")
    print("   'Claude, build a Python script that takes Kirana stock Excel,")
    print("    finds items < 10 quantity, and sends Hindi WhatsApp alert")
    print("    using Streamlit dashboard. User is 40yr old, only Hindi.'")

    # --- 5. SUCCESS METRIC ---
    print("\n📊 5. MVP SUCCESS METRIC:")
    print("   If 3 Kirana shops in Itaunja use it for 7 days and save Rs 1000 loss,")
    print("   MVP is SUCCESS. Then charge Rs 199/month.")

    print("\n" + "="*70)
    print("✅ BLUEPRINT COMPLETE - Ready to Build MVP in Day 24!")
    print("📄 Blueprint saved: Kanpur_Kirana_MVP_Blueprint.md")

# Run for your startup
customer_mvp_blueprint("Kanpur Kirana AI - Low Stock Alert")

print("\n" + "="*70 + "\n")

# For Leather Idea also
customer_mvp_blueprint("Kanpur Leather Catalog AI")

print("\nDay 23 Complete!")
