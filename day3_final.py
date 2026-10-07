# Day 3: Role-Based Prompting using Claude
# Created by Kanchan from Kanpur - ABTalks 60 Days Challenge

import streamlit as st

st.set_page_config(page_title="Day 3 - Role Based Prompting", page_icon="🎭")

st.title("🎭 Day 3: Role-Based Prompting")
st.caption("ABTalks 60 Days Claude AI Challenge | By Kanchan from Kanpur")

st.markdown("---")
st.write("### Learn how same question gives different answers with different Roles!")

question = st.text_area("Enter your question:", "Explain AI for a small shop owner in Kanpur")

role = st.selectbox("Choose AI Role:", 
    ["Doctor", "Teacher", "Shop Owner Friend", "Business Expert", "Kid"]
)

if st.button("Generate with Role"):
    st.success(f"**Role: {role}** -> Answering: {question}")
    st.write(f"As a {role}, I will explain this in my expert style...")
    st.write("This is how Role-Based Prompting works! One prompt, many expert personalities.")

st.markdown("---")
st.caption("Day 3 Completed | #ABTalks #RoleBasedPrompting")
