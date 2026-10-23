# Day 41 - Interactive Learning Studio - By Kanchan Maurya
import streamlit as st
import time

st.set_page_config(page_title="Interactive Learning Studio - Day 41", page_icon="📚", layout="wide")
st.title("📚 Interactive Learning Studio")
st.subheader("Day 41 - Claude Challenge | By Kanchan Maurya")
st.markdown("### AI-Powered Interactive Courses - Koi bhi Topic Sikho!")

col1, col2 = st.columns(2)
with col1:
    topic = st.selectbox("Topic Chuno", ["Python", "SQL", "Data Analysis", "Power BI", "Machine Learning"])
    level = st.selectbox("Level", ["Beginner", "Intermediate", "Advanced"])
with col2:
    duration = st.selectbox("Course Kitne Din Ka?", ["3 Days Crash Course", "7 Days", "30 Days Full"])
    style = st.selectbox("Sikhne Ka Style", ["Video + Quiz", "Notes + Project", "Full Practical"])

if st.button("🚀 Course Banao"):
    with st.spinner("AI Course bana raha hai..."):
        time.sleep(2)
    st.success(f"✅ {topic} Course Ready Hai! - {level} | {duration}")

    st.markdown(f"## 📖 Course: {topic} Mastery - {level}")
    st.progress(20)
    st.markdown("### 📚 Chapters:")

    chapters = {
        "Python": ["1. Python Basics - Variables", "2. Loops & Functions", "3. Pandas - Data Handling", "4. EDA Project", "5. Final Project - Fraud Detection"],
        "SQL": ["1. SELECT Basics", "2. WHERE & JOIN", "3. GROUP BY", "4. Subqueries", "5. Final Project"],
        "Data Analysis": ["1. Excel Basics", "2. Python EDA", "3. Visualization", "4. Segmentation", "5. Final Dashboard"],
        "Power BI": ["1. Dashboard Basics", "2. DAX", "3. Charts", "4. Report Building", "5. Final Dashboard"],
        "Machine Learning": ["1. ML Basics", "2. Regression", "3. Classification", "4. Random Forest", "5. Final Model"]
    }
    for ch in chapters.get(topic, chapters["Python"]):
        st.write(f"✅ {ch}")
        st.write(f"   ⏱️ 30 min | 📝 Notes | 🎥 Video | ❓ Quiz")

    st.markdown("---")
    st.markdown("### ❓ Quick Quiz - Check Karo Kitna Aata Hai!")
    q1 = st.radio("1. Python me data handle karne ke liye kaunsi library hai?", ["Numpy", "Pandas", "Matplotlib"])
    if q1 == "Pandas":
        st.success("✅ Sahi Jawab! Tu to Pro hai!")
    q2 = st.radio("2. SQL me data lene ke liye kaunsa command?", ["GET", "SELECT", "TAKE"])
    if q2 == "SELECT":
        st.success("✅ Sahi Jawab! Mast!")
    q3 = st.radio("3. EDA ka full form?", ["Exploratory Data Analysis", "Extra Data App", "Easy Data"])
    if q3 == "Exploratory Data Analysis":
        st.success("✅ Sahi Jawab! 3/3 - Beast!")
        st.balloons()

    st.markdown("### 🏆 Certificate Preview:")
    st.code(f"Certificate of Completion\n\nThis is to certify that Kanchan Maurya\ncompleted {topic} - {level} Course\nwith {duration}\n\nScore: 100% | Date: 2026")
    st.markdown("### 📊 Your Progress:")
    colA, colB, colC = st.columns(3)
    with colA: st.metric("Chapters Done", "2/5")
    with colB: st.metric("Quiz Score", "90%")
    with colC: st.metric("Streak", "7 Days 🔥")

st.markdown("---")
st.markdown("**Made by Kanchan Maurya | Day 41 - Claude Challenge**")
