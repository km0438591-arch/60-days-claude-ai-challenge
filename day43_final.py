# Day 43 - AI Workflow Architect - By Kanchan Maurya
import streamlit as st
import time

st.set_page_config(page_title="AI Workflow Architect - Day 43", page_icon="⚡", layout="wide")

st.title("⚡ AI Workflow Architect")
st.subheader("Day 43 - Claude Challenge | By Kanchan Maurya")
st.markdown("### Design End-to-End AI Workflows in 1 Click!")

# Sidebar
st.sidebar.header("🎯 Choose Your Workflow")
workflow = st.sidebar.selectbox("Workflow Type", [
    "📱 Instagram Content Workflow",
    "💼 LinkedIn Post Workflow", 
    "🎥 YouTube Video Workflow",
    "🛍️ Business Automation Workflow",
    "📧 Email Marketing Workflow"
])

goal = st.text_input("✍️ Apna Goal Likho", "Mujhe viral Instagram post chahiye")
tone = st.selectbox("Tone", ["Professional", "Funny", "Motivational", "Educational"])
model = st.selectbox("AI Model", ["Claude 3.5 Sonnet", "GPT-4", "Gemini", "Llama"])

if st.button("🚀 Build My Workflow"):
    with st.spinner("AI Workflow bana raha hai..."):
        time.sleep(2)
    st.success("✅ Workflow Ready!")

    if workflow == "📱 Instagram Content Workflow":
        steps = [
            ("Step 1 - Idea Generation", "Claude se 5 viral ideas generate karo", "⏱️ 2 min", "Claude"),
            ("Step 2 - Content Writing", "Caption + Hook likho - 150 words", "⏱️ 5 min", "Claude"),
            ("Step 3 - Image Creation", "AI se image banao - Midjourney / DALL-E", "⏱️ 10 min", "Midjourney"),
            ("Step 4 - Hashtag Research", "30 trending hashtags nikalo", "⏱️ 3 min", "Claude"),
            ("Step 5 - Post & Analyze", "Post karo + Insights check karo", "⏱️ 5 min", "Instagram"),
        ]
    elif workflow == "💼 LinkedIn Post Workflow":
        steps = [
            ("Step 1 - Topic Research", "Trending topic find karo", "⏱️ 5 min", "Claude"),
            ("Step 2 - Story Draft", "Personal story + lesson likho", "⏱️ 10 min", "Claude"),
            ("Step 3 - Hook Design", "First 2 lines viral hook", "⏱️ 3 min", "Claude"),
            ("Step 4 - Formatting", "Emoji + Line breaks + CTA", "⏱️ 2 min", "Manual"),
            ("Step 5 - Publish", "Best time 9 AM pe post karo", "⏱️ 1 min", "LinkedIn"),
        ]
    elif workflow == "🎥 YouTube Video Workflow":
        steps = [
            ("Step 1 - Title Ideas", "10 clickbait titles banao", "⏱️ 5 min", "Claude"),
            ("Step 2 - Script Writing", "Full script - Intro, Body, CTA", "⏱️ 20 min", "Claude"),
            ("Step 3 - Thumbnail", "AI thumbnail banao", "⏱️ 10 min", "Canva AI"),
            ("Step 4 - Editing", "CapCut se edit karo", "⏱️ 30 min", "CapCut"),
            ("Step 5 - SEO + Upload", "Description, Tags, Upload", "⏱️ 10 min", "YouTube"),
        ]
    elif workflow == "🛍️ Business Automation Workflow":
        steps = [
            ("Step 1 - Lead Capture", "Website se lead lo", "⏱️ Auto", "Zapier"),
            ("Step 2 - AI Reply", "Claude se auto reply bhejo", "⏱️ Auto", "Claude"),
            ("Step 3 - Follow Up", "3 din me follow up mail", "⏱️ Auto", "Gmail"),
            ("Step 4 - Payment", "Payment link bhejo", "⏱️ Auto", "Razorpay"),
            ("Step 5 - Feedback", "Feedback + Review lo", "⏱️ Auto", "Google Form"),
        ]
    else:
        steps = [
            ("Step 1 - Audience", "Target audience define karo", "⏱️ 5 min", "Claude"),
            ("Step 2 - Subject Line", "5 subject lines banao", "⏱️ 3 min", "Claude"),
            ("Step 3 - Email Body", "Personalized email likho", "⏱️ 10 min", "Claude"),
            ("Step 4 - Send", "Best time pe send karo", "⏱️ 2 min", "Mailchimp"),
            ("Step 5 - Track", "Open rate check karo", "⏱️ 5 min", "Mailchimp"),
        ]

    st.markdown(f"### 🎯 Goal: {goal}")
    st.markdown(f"**Tone:** {tone} | **Model:** {model}")
    st.markdown("---")
    for title, desc, t, tool in steps:
        col1, col2, col3 = st.columns([3, 2, 1])
        with col1:
            st.markdown(f"**{title}**")
            st.write(desc)
        with col2:
            st.write(f"🛠️ Tool: {tool}")
        with col3:
            st.write(t)
        st.markdown("⬇️")
    st.balloons()
    st.success(f"🎉 Total Time: {len(steps)*5} min | Tools Used: {len(steps)} | Efficiency: 90% Saved!")

st.markdown("---")
st.markdown("**Made by Kanchan Maurya | OIBSIP + Claude Challenge Day 43**")
