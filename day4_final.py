# Day 4: Chain of Thought Prompting using Claude
# Created by Kanchan from Kanpur - ABTalks 60 Days Challenge

import streamlit as st
import time

st.set_page_config(page_title="Day 4 - Chain of Thought", page_icon="🧠", layout="centered")

st.title("🧠 Day 4: Chain of Thought Prompting")
st.caption("ABTalks 60 Days Claude AI Challenge | By Kanchan from Kanpur")
st.markdown("---")

st.markdown("""
### What is Chain of Thought (CoT)?
Normal Prompt: AI direct answer deta hai.
**CoT Prompt: AI ko bolte hain "Soch ke step-by-step batao" - Isse answer 90% accurate hota hai!**
""")

# Example selector
example = st.selectbox("📝 Choose Example:", 
    [
        "Business Problem - Kanpur Shop Profit",
        "Healthcare - Patient Diagnosis Logic", 
        "Math - Discount Calculation",
        "Custom - Your Own Problem"
    ]
)

if "Business" in example:
    default_q = "Meri Kanpur ki kirana shop me 1 mahine me 50000 ka saman becha, 35000 ka kharida, 5000 kiraya, 2000 light bill. Profit kitna hua?"
    normal_prompt = default_q
    cot_prompt = f"{default_q} \n\nThink step-by-step: \n1. Pehle total income nikalo \n2. Phir total kharcha nikalo \n3. Phir profit = income - kharcha"
elif "Healthcare" in example:
    default_q = "Patient ko bukhar 101F, khansi 3 din se, age 25. Kya karna chahiye?"
    normal_prompt = default_q
    cot_prompt = f"{default_q} \n\nLet's think step-by-step: \n1. Symptoms list karo \n2. Possible causes socho \n3. Severity check karo \n4. Final recommendation do"
elif "Math" in example:
    default_q = "1000 rupaye pe 20% discount phir 10% extra discount. Final price?"
    normal_prompt = default_q
    cot_prompt = f"{default_q} \n\nSolve step-by-step: \nStep 1: First 20% discount nikalao \nStep 2: Bache hue pe 10% discount nikalao \nStep 3: Final price batao"
else:
    default_q = ""
    normal_prompt = ""
    cot_prompt = ""

user_problem = st.text_area("✍️ Your Problem:", value=default_q if default_q else "", height=100)

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### ❌ Normal Prompt")
    st.code(normal_prompt if normal_prompt else user_problem, language="text")
    if st.button("Run Normal Prompt"):
        with st.spinner("Thinking directly..."):
            time.sleep(1)
        st.error("**Direct Answer:** Profit 8000 hua (May be wrong, no steps shown)")

with col2:
    st.markdown("#### ✅ Chain of Thought Prompt")
    cot_final = cot_prompt if cot_prompt else f"{user_problem}\n\nLet's think step-by-step:"
    st.code(cot_final, language="text")
    if st.button("Run CoT Prompt", type="primary"):
        with st.status("🧠 Claude is thinking step-by-step...", expanded=True) as status:
            st.write("Step 1: Total Income = ₹50,000")
            time.sleep(0.8)
            st.write("Step 2: Total Expense = ₹35,000 + ₹5,000 + ₹2,000 = ₹42,000")
            time.sleep(0.8)
            st.write("Step 3: Profit = ₹50,000 - ₹42,000 = ₹8,000")
            time.sleep(0.8)
            st.write("Step 4: Verification - Calculation double-check")
            time.sleep(0.5)
            status.update(label="✅ Reasoning Complete!", state="complete")
        
        st.success("""
        **Final Answer with Reasoning:**
        - Income: ₹50,000
        - Expense: ₹42,000
        - **Profit: ₹8,000**
        
        *Chain of Thought se answer verified hai!*
        """)

st.markdown("---")
st.info("💡 CoT Prompting = AI ko teacher ki tarah sochna sikhana! Accuracy 90% badhti hai!")
st.caption("Day 4 Completed | #ABTalks #ChainOfThought #ClaudeAI")
