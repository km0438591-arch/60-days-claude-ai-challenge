# Day 45 - AI Decision Strategist - By Kanchan Maurya
import streamlit as st
import time

st.set_page_config(page_title="AI Decision Strategist - Day 45", page_icon="🧠", layout="wide")
st.title("🧠 AI Decision Strategist Dashboard")
st.subheader("Day 45 - Claude Challenge | By Kanchan Maurya")
st.markdown("### Koi bhi Decision lo - AI batayega sahi hai ya galat!")

col1, col2 = st.columns(2)
with col1:
    decision = st.text_input("🤔 Apna Decision Likho", "Mujhe Data Analyst job leni chahiye?")
    category = st.selectbox("Category", ["Career", "Business", "Money", "Study", "Personal"])
    budget = st.number_input("💰 Budget / Salary (Rs)", 0, 1000000, 30000)
    time_needed = st.selectbox("Kitna Time Lagega?", ["1 Week", "1 Month", "3 Months", "6 Months", "1 Year"])

with col2:
    pros = st.text_area("✅ Pros - Fayde Likho", "High salary\nGrowth hai\nMujhe data pasand hai")
    cons = st.text_area("❌ Cons - Nuksaan Likho", "Thoda tough hai\nCompetition zyada hai")
    risk = st.selectbox("Risk Kitna Hai?", ["Low", "Medium", "High"])
    gut = st.slider("Dil Kya Keh Raha Hai? - 1 to 10", 1, 10, 8)

if st.button("🚀 AI Se Decision Lo"):
    with st.spinner("AI soch raha hai..."):
        time.sleep(2)
    
    pros_count = len([x for x in pros.split("\n") if x.strip()!=""])
    cons_count = len([x for x in cons.split("\n") if x.strip()!=""])
    
    score = 50 + (pros_count*10) - (cons_count*5) + (gut*2)
    if risk=="Low": score+=10
    if risk=="High": score-=15
    if score>95: score=92
    if score<30: score=32

    st.success(f"✅ Decision Analysis Complete - {category}")

    st.markdown(f"## 🎯 Decision Score: {score}/100")
    st.progress(score/100)

    if score >= 75:
        st.markdown("### 🟢 GO FOR IT! - Kar le - Sahi decision hai!")
        st.balloons()
    elif score >= 50:
        st.markdown("### 🟡 SOCH SAMAJH KE KAR - Thoda risk hai but kar sakti hai!")
    else:
        st.markdown("### 🔴 RUK JA! - Abhi mat kar - Aur soch!")

    colA, colB, colC = st.columns(3)
    with colA:
        st.metric("Pros", pros_count, "Fayde")
    with colB:
        st.metric("Cons", cons_count, "Nuksaan")
    with colC:
        st.metric("Risk", risk)

    st.markdown("---")
    st.markdown("### 🧠 AI Recommendation:")
    if score >= 75:
        st.info(f"Tera decision '{decision}' ek dum sahi hai! Pros {pros_count} hai aur Cons sirf {cons_count} hai. Tera gut feeling bhi {gut}/10 hai. Time {time_needed} me ho jayega. Budget {budget} me fit hai. GO FOR IT!")
    else:
        st.warning(f"'{decision}' me thoda risk hai. Pehle Cons ko solve kar - {cons}. Fir 1 week baad fir se check kar.")

    st.markdown("### 📊 Action Plan:")
    st.write("✅ Step 1 - Aaj hi 1 chota step le")
    st.write("✅ Step 2 - 3 din me progress check kar")
    st.write("✅ Step 3 - 1 week me final decision le")
    st.write("✅ Step 4 - Mentor se baat kar")

    st.markdown("### ⚠️ Risk Analysis:")
    st.write(f"Risk Level: {risk} | Time: {time_needed} | Budget: Rs {budget}")

st.markdown("---")
st.markdown("**Made by Kanchan Maurya | Day 45 - Claude Challenge**")
