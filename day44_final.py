# Day 44 - LinkedIn Profile Optimizer - By Kanchan Maurya
import streamlit as st
import time

st.set_page_config(page_title="LinkedIn Optimizer - Day 44", page_icon="💼", layout="wide")
st.title("💼 AI LinkedIn Profile Optimizer")
st.subheader("Day 44 - Claude Challenge | By Kanchan Maurya")
st.markdown("### Apna LinkedIn Profile 100/100 Banao!")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("👤 Your Name", "Kanchan Maurya")
    headline = st.text_input("📌 Current Headline", "Data Analyst | Python | Fresher")
    about = st.text_area("📝 About Section", "I am a data analyst fresher. I know python.")
    skills = st.text_input("🛠️ Skills", "Python, Pandas, Excel")

with col2:
    experience = st.selectbox("Experience", ["Fresher", "0-1 Year", "1-2 Year", "2+ Year"])
    target = st.selectbox("Target Job", ["Data Analyst", "Data Scientist", "Business Analyst", "ML Engineer"])
    photo = st.selectbox("Profile Photo Hai?", ["Yes - Professional", "No", "Yes - Casual"])
    banner = st.selectbox("Banner Hai?", ["Yes", "No"])

if st.button("🚀 Optimize My Profile"):
    with st.spinner("AI Profile check kar raha hai..."):
        time.sleep(2)
    
    # Score Logic
    score = 40
    if len(about) > 100: score += 20
    if len(headline) > 20: score += 10
    if "Yes" in photo: score += 15
    if "Yes" in banner: score += 10
    if len(skills.split(",")) >= 3: score += 5
    if score > 100: score = 95

    st.success(f"✅ Analysis Complete - {name}")
    
    # Score Display
    st.markdown(f"## 🏆 Profile Score: {score}/100")
    st.progress(score/100)
    if score >= 80:
        st.markdown("### 🟢 Excellent! Bas thoda sa polish chahiye!")
    elif score >= 60:
        st.markdown("### 🟡 Good! Thoda improvement chahiye!")
    else:
        st.markdown("### 🔴 Weak! Abhi optimize karna padega!")
    
    st.markdown("---")
    st.markdown("### 🔥 AI Suggested New Headline - COPY KAR LE!")
    st.code(f"{target} | Python | SQL | Power BI | {experience} | Helping Businesses with Data | Open to Work")
    
    st.markdown("### ✨ AI Suggested About Section:")
    st.info(f"Hi! I'm {name}, a passionate {target} with skills in {skills}. I completed OIBSIP Internship where I built EDA, Customer Segmentation & Fraud Detection projects with 99.7% accuracy. I love turning raw data into stories. Currently looking for {target} opportunities. Let's connect!")
    
    st.markdown("### 📌 Improvement Tips:")
    st.write("✅ Headline me 3 skills + Open to Work add kar")
    st.write("✅ About me 150 words ka likh - Story wala")
    st.write("✅ Skills me 10 skills add kar - Python, SQL, Power BI, Excel")
    st.write("✅ Har week 2 post daal - LinkedIn active rahega")
    st.write("✅ Banner me apna kaam likh - Data Analyst Portfolio")
    
    st.markdown("### 🎯 Missing Skills for " + target + ":")
    st.write("SQL, Power BI, Tableau, Excel Advanced, Statistics")
    
    st.balloons()

st.markdown("---")
st.markdown("**Made by Kanchan Maurya | Day 44 - Claude Challenge**")
