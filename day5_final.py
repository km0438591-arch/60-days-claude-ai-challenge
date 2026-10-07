# Day 5: Context Engineering
# By Kanchan from Kanpur - 60 Days Claude Challenge

# Context Engineering = AI ko pura background dena taaki sahi jawab de

# Without Context (Bad)
bad_context = "Give me marketing ideas"

# With Context Engineering (Good)
good_context = """
BACKGROUND:
- Business: My uncle's kirana store in Kakadeo, Kanpur
- Location: Near Kanpur University, 80% customers are students & families
- Problem: Sales down 20% after new supermarket opened
- Budget: Rs 0 for marketing, only WhatsApp and posters
- Goal: Get 30 extra customers this week

TASK: Give me 3 marketing ideas that work in Kanpur with zero budget.

CONSTRAINTS:
- Use Hindi + English mix
- Ideas should be doable by one person in 1 hour daily
- Mention UPI, home delivery

Now give answer.
"""

print("BAD (No Context):")
print(bad_context)

print("\nGOOD (Context Engineering):")
print(good_context)

print("\n--- Claude's Expected Output With Good Context ---")
print("""
1. Kakadeo Students Group: University ke WhatsApp groups me daily 'Aaj ka Offer' post karo - Rs 10 sasta.
2. UPI Cashback Board: Dukaan ke bahar bade aksharo me likho 'UPI se pay karo, 5 rupya wapas'.
3. 7 baje ka Home Delivery: Shaam 7-9 baje free delivery Kakadeo me, students ko sabse zyada zarurat tab hoti hai.
""")

print("\nDay 5 Complete - Kanchan")
