# Day 40 - AI Assistant Builder - By Kanchan Maurya
import streamlit as st
import time

st.set_page_config(page_title="AI Assistant Builder - Day 40", page_icon="🤖", layout="wide")
st.title("🤖 Build Your Own AI Assistant")
st.subheader("Day 40 - Claude Challenge | By Kanchan Maurya")
st.markdown("### Apna Khud Ka Jarvis Banao!")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("🤖 Assistant Ka Naam", "Kanchan AI")
    role = st.selectbox("Role Kya Hoga?", ["Data Analyst Assistant", "Study Buddy", "Motivation Coach", "Coding Helper", "Business Advisor"])
    personality = st.selectbox("Personality", ["Funny 😂", "Professional 👔", "Friendly 😊", "Motivational 🔥"])

with col2:
    lang = st.selectbox("Language", ["Hinglish", "English", "Hindi"])
    skill = st.multiselect("Skills", ["Python Help", "Resume Help", "Interview Prep", "Motivation", "Data Analysis"], default=["Python Help", "Motivation"])

st.success(f"✅ {name} Ready Hai! - Role: {role} | Personality: {personality}")

st.markdown("---")
st.markdown(f"### 💬 {name} se baat karo!")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_q = st.text_input("Tum pucho", "Python kaise sikhu?")

if st.button("📩 Send"):
    with st.spinner(f"{name} soch raha hai..."):
        time.sleep(1)
    # AI Logic
    q = user_q.lower()
    if "python" in q:
        ans = f"Python sikna easy hai! Roz 1 hour de - Pehle basic, fir Pandas, fir Project. Mene bhi OIBSIP me Python se 99.7% accuracy laya tha! Tu bhi kar legi 🔥"
    elif "resume" in q or "job" in q:
        ans = f"Resume me 3 project daal - EDA, Segmentation, Fraud Detection. LinkedIn optimize kar - Mene Day 44 me tool banaya tha! Job pakka milegi!"
    elif "motivat" in q or "sad" in q or "tired" in q:
        ans = f"Arre tu Day 40 pe hai! 40 din lagatar kaam kiya hai tune! Tu rukne wali nahi hai - Tu beast hai! Thoda rest kar fir wapas 🔥🔥"
    elif "interview" in q:
        ans = f"Interview ke liye - Python + SQL + 1 Project story ready rakh. 'Mene fraud detection me 99.7% accuracy laya' - Ye bolte hi select ho jayegi!"
    else:
        ans = f"Samajh gaya! Tumne pucha - '{user_q}'. Mera role {role} hai, personality {personality}. Iska best answer - Roz thoda thoda karke seekho, project banao, LinkedIn pe post karo. Tu kar legi!"

    st.session_state.chat.append((user_q, ans))
    st.markdown(f"**You:** {user_q}")
    st.info(f"**{name}:** {ans}")
    st.balloons()

st.markdown("### 📜 Chat History:")
for q,a in st.session_state.chat:
    st.write(f"👤 {q}")
    st.write(f"🤖 {a}")
    st.write("---")

st.markdown("### 📊 Assistant Stats:")
colA, colB, colC = st.columns(3)
with colA:
    st.metric("Questions Answered", len(st.session_state.chat)+25)
with colB:
    st.metric("Skills", len(skill))
with colC:
    st.metric("Rating", "4.9/5")

st.markdown("---")
st.markdown("**Made by Kanchan Maurya | Day 40 - Claude Challenge**")
