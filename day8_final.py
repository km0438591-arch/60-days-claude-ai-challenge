# Day 8: Build Your First AI-Powered Dashboard with Claude Artifacts
# By Kanchan from Kanpur - Kanpur Kirana Sales Dashboard

# This code is designed to run with Claude Artifacts / Streamlit

dashboard_code = """
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Kanpur Kirana Dashboard", page_icon="🏪")

st.title("🏪 Kanpur Kirana Store - Daily Sales Dashboard")
st.write("Created by Kanchan from Kanpur | Day 8 - ABTalks Challenge")

# Sample Data for Kakadeo Kirana Store
data = {
    "Item": ["Aata", "Daal", "Chawal", "Tel", "Namkeen", "Biscuit"],
    "Morning Sales": [20, 15, 25, 10, 30, 40],
    "Evening Sales": [30, 20, 15, 25, 50, 60],
    "Stock Left": [100, 50, 80, 40, 20, 10]
}

df = pd.DataFrame(data)

# Show Table
st.subheader("📊 Aaj ki Sales Report")
st.dataframe(df)

# Insights using Claude-style thinking
st.subheader("🤖 Claude AI Insights")
st.success("Insight 1: Shaam ko Namkeen & Biscuit sabse zyada bikta hai - Kal se 10 extra packet laana.")
st.warning("Insight 2: Tel ka stock sirf 40 bacha hai - Kal subah supplier ko phone karna.")
st.info("Insight 3: Students shaam 6-9 baje zyada aate hain - Usi time offer lagao.")

st.metric(label="Aaj ki Total Sale", value="Rs 8,450", delta="+12% from yesterday")

st.write("---")
st.write("How to run: streamlit run day8_final.py")
"""

print(dashboard_code)

# Simple version without Streamlit (for GitHub run)
print("\n\n--- SIMPLE DASHBOARD OUTPUT (Without Streamlit) ---")
print("🏪 KANPUR KIRANA STORE - DAILY SALES")
print("Item\t\tMorning\tEvening\tStock Left")
print("Aata\t\t20kg\t30kg\t100kg")
print("Daal\t\t15kg\t20kg\t50kg")
print("Chawal\t\t25kg\t15kg\t80kg")
print("Tel\t\t10L\t25L\t40L (LOW STOCK!)")
print("Namkeen\t\t30 pkt\t50 pkt\t20 pkt (REORDER!)")
print("Biscuit\t\t40 pkt\t60 pkt\t10 pkt (REORDER!)")
print("\nTotal Sale Today: Rs 8,450 (+12%)")
print("\nClaude Insight: Evening me snacks zyada bik rahe hain, kal se stock double rakho!")

print("\nDay 8 Complete - Dashboard Ready!")
