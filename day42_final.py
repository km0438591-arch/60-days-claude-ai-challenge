# Day 42 - Financial Command Center - By Kanchan Maurya
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Financial Command Center - Day 42", page_icon="💰", layout="wide")
st.title("💰 Personal Financial Command Center")
st.subheader("Day 42 - Claude Challenge | By Kanchan Maurya")
st.markdown("### AI-Powered Finance Dashboard - Paisa ka Full Control!")

col1, col2 = st.columns(2)
with col1:
    salary = st.number_input("💵 Monthly Income / Salary", 0, 1000000, 30000)
    rent = st.number_input("🏠 Rent", 0, 50000, 5000)
    food = st.number_input("🍔 Food", 0, 50000, 4000)
with col2:
    shopping = st.number_input("🛍️ Shopping", 0, 50000, 3000)
    travel = st.number_input("🚗 Travel", 0, 50000, 2000)
    other = st.number_input("📦 Other", 0, 50000, 2000)

total_expense = rent + food + shopping + travel + other
saving = salary - total_expense
saving_percent = int((saving / salary * 100)) if salary>0 else 0

st.markdown("---")
colA, colB, colC, colD = st.columns(4)
with colA: st.metric("Income", f"Rs {salary}")
with colB: st.metric("Expense", f"Rs {total_expense}")
with colC: st.metric("Saving", f"Rs {saving}")
with colD: st.metric("Saving %", f"{saving_percent}%")

st.progress(max(saving_percent,0)/100)

if saving_percent >= 40:
    st.success("🟢 EXCELLENT! Tu to saving queen hai!")
    st.balloons()
elif saving_percent >= 20:
    st.markdown("### 🟡 GOOD! Thoda aur bacha sakti hai!")
else:
    st.markdown("### 🔴 WARNING! Kharcha zyada hai - Control kar!")

# Chart
st.markdown("### 📊 Expense Chart:")
labels = ["Rent", "Food", "Shopping", "Travel", "Other"]
values = [rent, food, shopping, travel, other]
fig, ax = plt.subplots()
ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
ax.set_title("Kaha Paisa Ja Raha Hai?")
st.pyplot(fig)

st.markdown("### 🤖 AI Financial Advisor:")
if shopping > 5000:
    st.warning("⚠️ Shopping pe zyada kharcha ho raha hai - 2000 kam kar - 2000 save ho jayega!")
if food > 5000:
    st.warning("⚠️ Food pe zyada hai - Ghar ka khana kha - 1500 bachega!")
st.info(f"💡 Agar tu har mahine Rs {saving} bachayegi - to 1 saal me Rs {saving*12} ho jayega! 5 saal me Rs {saving*60}!")
st.success(f"🎯 Goal: Emergency fund Rs 50000 - {int(50000/max(saving,1))} mahine me ho jayega!")

st.markdown("### 📈 Investment Plan:")
st.write("✅ 50% Saving - Bank / FD")
st.write("✅ 30% Saving - SIP - Mutual Fund")
st.write("✅ 20% Saving - Gold / Emergency")
st.write("✅ Har mahine 500 SIP se start kar - bada ban jayega!")

st.markdown("---")
st.markdown("**Made by Kanchan Maurya | Day 42 - Claude Challenge**")
