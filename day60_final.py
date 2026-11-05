# Day 60: FINAL CAPSTONE - Complete AI Business Dashboard
# 60-Day Claude AI Challenge - GRADUATION DAY

print("🎓 Day 60: FINAL CAPSTONE - Complete AI Business Dashboard")
print("="*65)
print("By Kanchan | Kanpur | 60-Day Claude AI Challenge Complete!")
print("="*65)

# --- Full Business Data (Day 1 to Day 60 Journey) ---
sales_data = [
    {"day": "Day 1-10", "sales": 45000, "orders": 45},
    {"day": "Day 11-20", "sales": 68000, "orders": 62},
    {"day": "Day 21-30", "sales": 82000, "orders": 78},
    {"day": "Day 31-40", "sales": 95000, "orders": 90},
    {"day": "Day 41-50", "sales": 112000, "orders": 105},
    {"day": "Day 51-60", "sales": 135000, "orders": 128},
]

customers = [
    {"name": "Rajat", "city": "Noida", "status": "Active", "last_order": "Today"},
    {"name": "Priya", "city": "Kanpur", "status": "Pending", "last_order": "Yesterday"},
    {"name": "Aman", "city": "Lucknow", "status": "Active", "last_order": "Today"},
]

def final_dashboard():
    print("\n📊 --- 60 DAYS SALES REPORT ---")
    total_sales = 0
    total_orders = 0
    
    for data in sales_data:
        print(f"{data['day']} | Sales: Rs.{data['sales']} | Orders: {data['orders']}")
        total_sales += data['sales']
        total_orders += data['orders']

    print(f"\n💰 TOTAL 60 DAYS SALES: Rs.{total_sales}")
    print(f"📦 TOTAL ORDERS: {total_orders}")
    
    avg = total_sales // 6
    print(f"📈 AVERAGE PER 10 DAYS: Rs.{avg}")
    
    print("\n--- CLAUDE AI FINAL INSIGHTS ---")
    print("✅ Sales har 10 din me badhi hai - Business Growing hai!")
    print("💡 Suggestion: Ab Noida me naya branch kholo.")
    print("💡 Suggestion: Top customers ko Diwali Offer bhejo.")

    print("\n👥 --- CUSTOMER STATUS ---")
    for c in customers:
        icon = "✅" if c['status'] == "Active" else "⏳"
        print(f"{icon} {c['name']} | {c['city']} | {c['status']} | Last Order: {c['last_order']}")

    print("\n🏆 --- MY 60 DAYS JOURNEY ---")
    print("Day 1: Claude Setup")
    print("Day 2: Pattern Logic")
    print("Day 31: Supply Chain Tower")
    print("Day 35: Prompt Puzzle Game")
    print("Day 59: Smart Business Assistant")
    print("Day 60: Final Capstone Dashboard - DONE!")

final_dashboard()

print("\n" + "="*65)
print("🎓 CONGRATULATIONS! 60-DAY CHALLENGE COMPLETE!")
print("Status: GRADUATED - v1.0.0 SHIPPED")
print("GitHub: km0438591-arch/60-days-claude-ai-challenge")
print("="*65)
