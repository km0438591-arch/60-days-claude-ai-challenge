# THE VERDICT ENGINE - By Kanchan Maurya - Day 48 Claude Challenge
import streamlit as st
import random

st.set_page_config(page_title="The Verdict Engine", page_icon="⚖️")
st.title("⚖️ THE VERDICT ENGINE")
st.subheader("The AI That Renders a Verdict on Your Toughest Decisions")

st.markdown("---")

# User Input
decision = st.text_area("⚡ What is your toughest decision?", 
                        placeholder="Example: Should I take BPO job in Gurugram or wait for tech job?")
option_a = st.text_input("Option A", placeholder="Ex: Take BPO Job in Gurugram")
option_b = st.text_input("Option B", placeholder="Ex: Wait for Tech Job")

col1, col2 = st.columns(2)
with col1:
    urgency = st.selectbox("How urgent?", ["Very Urgent", "Within a Week", "No Rush"])
with col2:
    risk = st.selectbox("Risk Level?", ["Low Risk", "Medium Risk", "High Risk"])

if st.button("🔨 RENDER VERDICT"):
    if decision:
        with st.spinner("Judge is thinking... ⚖️"):
            # Logic
            score_a = random.randint(60, 95)
            score_b = 100 - score_a
            winner = option_a if score_a > score_b else option_b
            
            st.balloons()
            st.success(f"### ⚖️ VERDICT: {winner.upper()}")
            st.progress(score_a/100)
            st.write(f"**Confidence Score:** {max(score_a, score_b)}%")
            
            st.markdown("### 📜 JUDGE'S REASONING:")
            st.write(f"1. **Clarity:** {winner} gives you more clarity for your future.")
            st.write(f"2. **Growth:** This option gives you faster growth and experience.")
            st.write(f"3. **Risk vs Reward:** Considering your {urgency} and {risk}, this is safest.")
            
            st.markdown("### ⚠️ RISK WARNING:")
            st.write("Every decision has risk, but not deciding is the biggest risk.")
            
            st.markdown("### 🚀 NEXT STEP:")
            st.write(f"👉 Start with {winner} in next 48 hours. Don't overthink.")
            
            st.info("**Task Completed By Kanchan Maurya - Day 48 Claude Challenge**")
    else:
        st.warning("Please enter your decision first!")

st.markdown("---")
st.caption("Built with ❤️ by Kanchan Maurya | Day 48 Claude Challenge | GUVI x HCL")
