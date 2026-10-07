# Day 28: Build a Hospital Admission Readiness Simulator
# By Kanchan from Kanpur - Healthcare AI | ABTalks 60 Days Claude Challenge

import streamlit as st
import time
import random

st.set_page_config(page_title="Hospital Admission Readiness", page_icon="🏥", layout="centered")

st.title("🏥 Day 28: Hospital Admission Readiness Simulator")
st.subheader("ABTalks x Claude AI Challenge | By Kanchan")
st.markdown("---")

# Patient Form
st.markdown("### 👩‍⚕️ Patient Admission Check")
patient_name = st.text_input("Patient Name", placeholder="e.g. Kanchan")
age = st.number_input("Age", min_value=1, max_value=100, value=25)
department = st.selectbox("Department Required", ["Emergency", "ICU", "General Ward", "Maternity", "Pediatrics"])

col1, col2 = st.columns(2)
with col1:
    bp = st.slider("Blood Pressure (systolic)", 80, 200, 120)
    oxygen = st.slider("Oxygen Saturation %", 70, 100, 96)
with col2:
    heart_rate = st.slider("Heart Rate bpm", 50, 150, 80)
    temp = st.slider("Temperature °F", 95.0, 105.0, 98.6)

# Bed Status Mock
st.markdown("### 🛏️ Live Bed Availability")
bed_col1, bed_col2, bed_col3 = st.columns(3)
bed_col1.metric("ICU Beds", "2 / 10", "-8 occupied")
bed_col2.metric("General Beds", "12 / 30", "-18 occupied")
bed_col3.metric("Emergency Beds", "5 / 15", "-10 occupied")

if st.button("🚀 Check Admission Readiness", type="primary"):
    if not patient_name:
        st.warning("Please enter Patient Name!")
    else:
        with st.status("🔍 Analyzing patient vitals & hospital readiness...", expanded=True) as status:
            st.write(f"📋 Processing admission for {patient_name}, Age {age}...")
            time.sleep(1.2)
            st.write(f"🏨 Checking {department} availability...")
            time.sleep(1.2)
            st.write("🤖 Claude AI analyzing vitals for risk score...")
            time.sleep(1.2)
            
            # Readiness Logic
            risk_score = 0
            if oxygen < 92: risk_score += 40
            if bp > 160 or bp < 90: risk_score += 20
            if heart_rate > 110: risk_score += 20
            if temp > 101: risk_score += 10
            
            status.update(label="✅ Analysis Complete!", state="complete", expanded=False)
        
        st.markdown("---")
        st.markdown("### 📊 Admission Readiness Report")
        
        if risk_score >= 60:
            st.error(f"🚨 **HIGH PRIORITY ADMISSION** - Risk Score: {risk_score}/100")
            st.write(f"**Recommendation:** Immediate admission to {department} required.")
            st.write("**Assigned Bed:** ICU-03 | **Doctor:** Dr. Sharma on call")
        elif risk_score >= 30:
            st.warning(f"⚠️ **MODERATE PRIORITY** - Risk Score: {risk_score}/100")
            st.write(f"**Recommendation:** Admit to {department} within 2 hours observation.")
            st.write("**Assigned Bed:** General-12 | **Doctor:** Dr. Verma")
        else:
            st.success(f"✅ **STABLE - Low Risk** - Risk Score: {risk_score}/100")
            st.write("**Recommendation:** OPD consultation sufficient, admission not required now.")
            st.write("**Next Step:** Prescription + Home care advisory")
        
        st.balloons()
        st.info("💡 Built with Streamlit + Claude AI | Day 28 Completed - Healthcare for Bharat")

st.markdown("---")
st.caption("Day 28/60 | #ABTalks #ClaudeAI #BuildInPublic | github.com/km0438591-arch/60-days-claude-ai-challenge")
