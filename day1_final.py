# Day 1: Claude Setup & Your AI Personality Profile
# Created by Kanchan from Kanpur - ABTalks 60 Days Challenge

import streamlit as st

st.set_page_config(page_title="Day 1 - Claude Setup & Personality", page_icon="⚙️")

st.title("⚙️ Day 1: Claude Setup & Your AI Personality Profile")
st.caption("ABTalks 60 Days Claude AI Challenge | By Kanchan from Kanpur")
st.markdown("---")

st.markdown("### 👋 Welcome to Day 1!")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🔧 Claude Setup")
    st.code("""
    1. claude.ai pe account banaya ✅
    2. API Key generate ki ✅
    3. Streamlit install kiya ✅
    4. GitHub repo setup kiya ✅
    """, language="text")
    
    api_status = st.selectbox("Claude API Status", ["Connected ✅", "Not Connected ❌"])
    model = st.selectbox("Model Selected", ["Claude 3.5 Sonnet", "Claude 3 Opus", "Claude 3 Haiku"])

with col2:
    st.markdown("#### 👩‍💻 My AI Personality Profile")
    name = st.text_input("Your Name", "Kanchan")
    location = st.text_input("Location", "Itaunja, Kanpur, UP")
    goal = st.text_input("Your Goal", "Build AI for Bharat - Rural Healthcare")
    
    personality = st.multiselect("My AI Personality Traits",
        ["Friendly", "Helpful", "Innovative", "Hardworking", "Curious", "Bharat-Focused"],
        default=["Friendly", "Helpful", "Bharat-Focused"]
    )

st.markdown("---")
st.markdown("### 🧠 My AI Profile Card")

st.success(f"""
**Name:** {name}
**From:** {location}
**Mission:** {goal}
**AI Personality:** {', '.join(personality)}
**Day 1 Status:** Setup Complete! 🚀
**Challenge:** 60 Days Claude AI with ABTalks
""")

if st.button("✅ Generate My Day 1 Profile", type="primary"):
    st.balloons()
    st.markdown(f"""
    #### 🎉 Profile Created!
    
    > "Hi, I am **{name}** from **{location}**. 
    > I am starting my 60 Days AI journey with ABTalks.
    > My personality is **{', '.join(personality)}**.
    > I want to use Claude AI to build solutions for **{goal}**.
    > Day 1 - Setup Done!"
    """)
    st.metric("Setup Progress", "100%", "Day 1 Done")

st.caption("Day 1 Completed | #ABTalks #ClaudeSetup #AIPersonality")
