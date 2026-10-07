# Day 10: Claude Tools & Function Calling
# By Kanchan from Kanpur - 60 Days Claude Challenge
# Use Case: Kanpur Kirana ka Smart Assistant jo Tools use kare

import json
from datetime import datetime

# Mock Tools (Asli me ye Claude automatically call karta hai)
def check_stock(item):
    stock_db = {"aata": 100, "daal": 5, "tel": 40, "biscuit": 8}
    return stock_db.get(item.lower(), 0)

def get_weather_kanpur():
    return "Kanpur me aaj 42°C hai, loo chal rahi hai. Evening me customers kam aayenge."

def send_whatsapp_alert(message):
    return f"WhatsApp sent to Owner: {message}"

def calculate_profit(sales):
    return sales * 0.15  # 15% margin

print("🛠️ Day 10: Claude Tools Demo - Kanpur Kirana Smart Assistant")
print("User Query: 'Daal ka stock check karo aur owner ko alert bhejo'\n")

# Claude's Thinking Process
user_query = "Daal ka stock check karo"

# Tool 1 Call
stock = check_stock("daal")
print(f"[Claude Tool Call 1: check_stock('daal')] -> Result: {stock}kg bacha hai")

if stock < 10:
    # Tool 2 Call
    alert = send_whatsapp_alert(f"ALERT: Daal ka stock low hai - sirf {stock}kg bacha hai, kal Mandi se lana hai")
    print(f"[Claude Tool Call 2: send_whatsapp_alert] -> Result: {alert}")
    
    # Tool 3 Call
    weather = get_weather_kanpur()
    print(f"[Claude Tool Call 3: get_weather_kanpur] -> Result: {weather}")
    print(f"-> Claude Insight: Garmi zyada hai toh Daal kam bikegi, 20kg hi order karo")

# Final Answer by Claude after using Tools
final_answer = f"""
✅ Task Complete!
- Daal Stock: {stock}kg (LOW)
- Action: Owner ko WhatsApp alert bhej diya
- Weather Context: {weather}
- Suggestion: Kal subah 20kg Daal order karo

This is Function Calling - Claude ne khud tools use kiye!
"""

print("\n" + final_answer)
print("\nDay 10 Complete - Tools Mastered! By Kanchan from Kanpur")
