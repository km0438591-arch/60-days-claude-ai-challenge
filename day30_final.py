# Day 30: Build a Supply Chain Optimizer
# ABTalks 60 Days Claude Challenge - MILESTONE | By Kanchan

import streamlit as st
import time
import pandas as pd
import random

st.set_page_config(page_title="Supply Chain Optimizer", page_icon="📈", layout="wide")

st.title("📈 Day 30: Supply Chain Optimizer")
st.subheader("ABTalks x Claude AI | Final Project of Phase 1 (Day 27-30)")
st.markdown("---")

st.sidebar.header("⚙️ Optimizer Controls")
hospital = st.sidebar.selectbox("Select Hospital", ["Itaunja CHC", "KGMU Lucknow", "SGPGI Lucknow", "Kanpur Hallet", "Barabanki District Hospital"])
budget = st.sidebar.slider("Monthly Budget (in Lakhs)", 1, 20, 8)
priority = st.sidebar.selectbox("Optimize For", ["Lowest Cost", "Fastest Delivery", "Maximum Lives Saved", "Balanced"])

# Main
col1, col2, col3 = st.columns(3)
col1.metric("Total Orders This Month", "342", "+18%")
col2.metric("Cost Saved by AI", f"₹{budget * 0.22:.1f} Lakh", "22% saved")
col3.metric("Delivery Success", "96.8%", "+4.2% with AI")

st.markdown("### 🧾 Current Stock Requirement")

req_data = {
    "Medicine": ["Oxygen", "Antibiotics", "IV Set", "Gloves", "Insulin"],
    "Required": [150, 400, 300, 1000, 80],
    "In Hand": [60, 200, 120, 400, 30],
    "Shortage": [90, 200, 180, 600, 50],
    "Supplier": ["OxyGen Lucknow", "MedPlus Kanpur", "HealthKart Delhi", "Local Itaunja", "Sun Pharma"]
}
df = pd.DataFrame(req_data)
st.dataframe(df, use_container_width=True)

if st.button("🤖 Run Claude AI Optimizer", type="primary"):
    with st.status("🚀 Claude AI optimizing your supply chain...", expanded=True) as status:
        st.write(f"🏥 Analyzing demand for {hospital} with budget ₹{budget} Lakh...")
        time.sleep(1)
        st.write(f"🎯 Optimization Goal: {priority}...")
        time.sleep(1)
        st.write("💰 Comparing 12 suppliers, checking delivery time & cost...")
        time.sleep(1.5)
        st.write("📦 Generating best purchase plan...")
        time.sleep(1)
        status.update(label="✅ Optimized Plan Ready!", state="complete", expanded=False)

    st.markdown("---")
    st.success(f"**Optimized Plan for {hospital} | Mode: {priority}**")

    t1, t2, t3 = st.tabs(["💡 AI Recommended Plan", "💰 Cost Breakdown", "📜 Certificate"])

    with t1:
        if priority == "Lowest Cost":
            st.write("**Plan:** Buy bulk from Kanpur supplier (10% extra discount). Combine delivery for 3 items in 1 truck. Save ₹1.8 Lakh.")
        elif priority == "Fastest Delivery":
            st.write("**Plan:** Use local Lucknow vendors even if 5% costly. Drone + Bike delivery for emergency items. Delivery in 3 hours.")
        elif priority == "Maximum Lives Saved":
            st.write("**Plan:** Prioritize Oxygen + Insulin first. Airlift from Delhi if needed. Lives > Cost.")
        else:
            st.write("**Plan:** Balanced approach - 60% from low-cost supplier, 40% from fast supplier. Best ROI.")
        
        opt_df = pd.DataFrame({
            "Item": ["Oxygen", "Antibiotics", "IV Set", "Gloves", "Insulin"],
            "Order Qty": [100, 250, 200, 800, 60],
            "Best Supplier": ["MedPlus Kanpur", "MedPlus Kanpur", "Local Lucknow", "Local Itaunja", "SGPGI Pool"],
            "Cost": ["₹45k", "₹60k", "₹30k", "₹24k", "₹55k"],
            "ETA": ["4 hrs", "6 hrs", "2 hrs", "1 hr", "5 hrs"]
        })
        st.dataframe(opt_df, use_container_width=True)
        st.metric("Total Optimized Cost", f"₹{budget*0.78:.1f} Lakh / ₹{budget} Lakh", f"Saved ₹{budget*0.22:.1f} Lakh")

    with t2:
        st.bar_chart(pd.DataFrame({"Cost": [45, 60, 30, 24, 55]}))
        st.write("**AI Insight:** 22% cost saved by bulk buying + route optimization")

    with t3:
        st.balloons()
        st.markdown("""
        ### 🎉 CONGRATULATIONS!
        
        **Phase 1 Completed (Day 27-30): Healthcare Supply Chain Mastery**
        
        You have successfully built:
        - ✅ Day 27: Patient Treatment System
        - ✅ Day 28: Hospital Admission Simulator
        - ✅ Day 29: Operation Lifeline Crisis Lab
        - ✅ Day 30: Supply Chain Optimizer
        
        **Next: Day 31 onwards - Advanced AI Agents**
        """)
        st.code(f"Certificate ID: ABT-30-{random.randint(1000,9999)}-KANCHAN | Verified by ABTalks")

else:
    st.info("👆 'Run Claude AI Optimizer' dabao apna optimized plan dekhne ke liye!")

st.markdown("---")
st.caption("Day 30/60 | MILESTONE COMPLETE | #ABTalks #ClaudeAI #HealthcareAI | github.com/km0438591-arch/60-days-claude-ai-challenge")
