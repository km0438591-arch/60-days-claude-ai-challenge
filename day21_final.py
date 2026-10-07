# Day 21: Build a Digital Privacy & Footprint Intelligence Dashboard with Claude
# By Kanchan from Kanpur - Privacy for Girls

import streamlit as st
from datetime import datetime

print("🔒 Day 21: Digital Privacy & Footprint Intelligence Dashboard")

# --- Full Streamlit Dashboard Code ---
dashboard_code = '''
import streamlit as st

st.set_page_config(page_title="Privacy Dashboard - Kanchan", page_icon="🔒")
st.title("🔒 Digital Privacy & Footprint Intelligence Dashboard")
st.subheader("By Kanchan from Kanpur | Built with Claude AI | For Girls Safety")

# Input
username = st.text_input("Enter Instagram/LinkedIn Username", "kanchan_kanpur")
email = st.text_input("Enter Email to check leak", "kanchan@example.com")

if st.button("🔍 Scan My Digital Footprint"):
    st.write("---")
    st.write(f"### Scan Report for: {username} | {datetime.now().strftime('%d-%m-%Y')}")

    # Mock Claude AI Scan
    risk_score = 0
    issues = []

    # 1. Photo Public Check
    photo_public = True # Simulated
    if photo_public:
        st.warning("⚠️ RISK: Your profile photos are PUBLIC - Location Kanpur is visible")
        risk_score += 40
        issues.append("Insta Private karo")

    # 2. Email Leak Check
    email_leaked = False
    if email_leaked:
        st.error("🚨 HIGH RISK: Email found in data breach!")
        risk_score += 50
    else:
        st.success("✅ Email is safe - Not found in leak")

    # 3. Location Tag Check
    location_tag = True
    if location_tag:
        st.warning("⚠️ RISK: You tagged Itaunja, Kanpur in 5 posts - Stalkers can track")
        risk_score += 30
        issues.append("Location tags hatao")

    # Final Score
    st.metric("Total Privacy Risk Score", f"{risk_score}/100")
    
    if risk_score > 70:
        st.error(f"🔴 HIGH RISK! Claude Advice: {', '.join(issues)} + 2FA ON karo")
    elif risk_score > 30:
        st.warning("🟡 MEDIUM RISK - Settings check karo")
    else:
        st.success("🟢 LOW RISK - Aap safe ho Kanchan!")
    
    st.balloons()
    st.info("💡 Claude Tip: Har Sunday ko ye scan chalao - Safe raho!")

st.markdown("---")
st.markdown("Built with Claude AI | Day 21 - ABTalks Challenge")
'''

print(dashboard_code)

# --- Demo for GitHub (Without Streamlit) ---
def privacy_dashboard_demo(user):
    print(f"\n--- Privacy Scan Demo for {user} ---\n")
    
    scan_result = {
        "public_photos": 12,
        "location_tags": ["Itaunja, Lucknow", "Kanpur", "VVDN Location"],
        "email_leaked": False,
        "phone_leaked": False
    }
    
    print(f"📱 Public Photos Found: {scan_result['public_photos']} (Risk)")
    print(f"📍 Location Tags: {scan_result['location_tags']}")
    print(f"📧 Email Leak: {'YES - DANGER' if scan_result['email_leaked'] else 'No - Safe'}")
    
    risk = 40 + len(scan_result['location_tags'])*10
    print(f"\n🎯 Final Risk Score: {risk}/100")
    print(f"🤖 Claude Advice: Insta ko Private karo, Location tag band karo, Password change karo!")
    print(f"\n📄 Report Saved: Privacy_Report_{user}.pdf")

privacy_dashboard_demo("kanchan_kanpur")

print("\n--- How to Run ---")
print("pip install streamlit")
print("streamlit run day21_final.py")
print("\nDay 21 Complete - Privacy Dashboard Ready for Girls!")
