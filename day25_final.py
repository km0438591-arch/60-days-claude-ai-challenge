# Day 25: Build an AI Shark Tank Startup Simulator with Claude
# By Kanchan from Kanpur - Pitch to Sharks!

import random
import time

print("🦈 Day 25: AI Shark Tank Startup Simulator - Kanpur Edition")

def shark_tank_simulator():
    print("\n" + "="*70)
    print("🎬 WELCOME TO AI SHARK TANK - KANPUR SPECIAL")
    print("="*70)
    
    # Your Pitch
    startup_name = "Kanpur Kirana AI"
    ask = "Rs 2 Lakh for 10% Equity"
    
    print(f"\n👩‍💼 Founder: Kanchan from Kanpur")
    print(f"🚀 Startup: {startup_name}")
    print(f"💰 Ask: {ask}")
    print(f"💡 One Liner: 'Kanpur ke Kirana ka stock AI se track, Hindi me alert!'")
    
    print("\n--- Pitch Starts ---")
    print("'Namaste Sharks, Kanpur me 15,000 Kirana shops roz Rs 500 ka nuksan karte hai")
    print("kyuki stock khatam ka pata nahi chalta. Mera AI WhatsApp pe Hindi me bolta hai")
    print("- Aata khatam hone wala hai! Mere 5 customers ne 7 din me Rs 10,000 bachaya.'")
    
    time.sleep(1)
    print("\n🦈 SHARKS ARE LISTENING...\n")
    
    # Sharks AI - Claude Personas
    sharks = {
        "Aman Gupta (boAt)": {
            "personality": "D2C & Branding King",
            "question": "Branding kya hai? Kirana wala ye app kyu lega JioMart ke time pe?",
            "offer_logic": "If market large, he offers"
        },
        "Namita Thapar": {
            "personality": "Numbers Queen",
            "question": "Unit economics kya hai? Rs 199 me profit kitna? Burn kitna?",
            "offer_logic": "If profit clear, she offers"
        },
        "Peyush Bansal": {
            "personality": "Tech & Small Town Focus",
            "question": "Tech kya hai? Kanpur ke liye hi kyu? Scale kaise hoga?",
            "offer_logic": "Loves Kanpur small town idea"
        },
        "Anupam Mittal": {
            "personality": "Tough Question Guy",
            "question": "Competition se kaise bachoge? 5 shop is not traction!",
            "offer_logic": "Asks tough but offers if answer good"
        }
    }
    
    offers = []
    
    for shark_name, shark in sharks.items():
        print(f"🦈 {shark_name} ({shark['personality']}):")
        print(f"   ❓ Q: {shark['question']}")
        
        # Your Answer (Claude generated)
        if "Aman" in shark_name:
            ans = "Sir, branding hai 'Apni Bhasha Me AI'. JioMart unka competitor hai, hum unke dost hai - unka stock bachate hai"
            print(f"   👩‍💼 Kanchan: {ans}")
            print(f"   ✅ Aman: 'I love it! Hyperlocal ka zamana hai. I offer 2L for 12%'")
            offers.append("Aman: 2L for 12%")
            
        elif "Namita" in shark_name:
            ans = "Mam, Rs 199 me Rs 180 profit hai (WhatsApp API Rs 19). Burn zero, laptop se kaam. Month 3 me 19k profit"
            print(f"   👩‍💼 Kanchan: {ans}")
            print(f"   ✅ Namita: 'Numbers clear hai. I offer 2L for 10% as you asked'")
            offers.append("Namita: 2L for 10%")
            
        elif "Peyush" in shark_name:
            ans = "Sir, Tech hai Claude AI + Excel. Kanpur se start karungi, phir UP ke 2 Lakh Kirana. Hindi is my moat"
            print(f"   👩‍💼 Kanchan: {ans}")
            print(f"   ✅ Peyush: 'Bharat ke liye bana rahi ho! I offer 2L for 8% - best offer!'")
            offers.append("Peyush: 2L for 8% - BEST")
            
        else: # Anupam
            ans = "Sir, 5 se 100 tak jaungi Itaunja me hi. JioMart online hai, main unki dukaan me hu. Competition nahi, collaboration"
            print(f"   👩‍💼 Kanchan: {ans}")
            print(f"   ❌ Anupam: 'I am out - too early, but best wishes from Shaadi.com'")
        
        print()
        time.sleep(1)
    
    print("="*70)
    print("🏆 FINAL OFFERS SUMMARY:")
    for offer in offers:
        print(f"   - {offer}")
    
    print("\n🎯 CLAUDE SIMULATOR VERDICT:")
    print("   WINNER: Peyush Bansal - 2 Lakh for 8% (Lowest equity)")
    print("   Reason: He loves small-town Bharat startups + your Hindi AI edge")
    print("   Your Decision: Deal with Peyush!")
    print("\n💡 Learning: Pitch me numbers + emotion dono chahiye - Kanpur story is your power!")
    print("="*70)

# Run Simulator
shark_tank_simulator()

# --- Streamlit Version Code for ABTalks Deliverable ---
streamlit_code = '''
import streamlit as st

st.title("🦈 AI Shark Tank Simulator - Day 25")
st.write("By Kanchan from Kanpur")

idea = st.text_input("Your Startup Idea", "Kanpur Kirana AI")
ask = st.text_input("Your Ask", "2 Lakh for 10%")

if st.button("Pitch to Sharks"):
    st.write(f"Pitching: {idea} for {ask}")
    st.write("🦈 Aman: I love hyperlocal! Offer 2L for 12%")
    st.write("🦈 Namita: Numbers clear! Offer 2L for 10%")
    st.write("🦈 Peyush: Bharat ke liye! Offer 2L for 8% - BEST DEAL!")
    st.balloons()
    st.success("Deal Closed with Peyush! Kanpur Rocks!")
'''

print("\n--- Streamlit Code for ABTalks ---")
print(streamlit_code)
print("\nDay 25 Complete - Shark Tank Ready!")
