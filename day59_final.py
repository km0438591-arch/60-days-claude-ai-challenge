# Day 59: Build Your AI Final Capstone - Smart Business Assistant
# 60-Day Claude AI Challenge

print("🚀 Day 59: AI Smart Business Assistant")
print("="*60)

# --- Business Data ---
business = {
    "name": "My Business - Kanpur",
    "today_sales": 12500,
    "yesterday_sales": 9800,
    "pending_orders": 12,
    "low_stock_items": ["Leather Shoes", "Hardware Tools"]
}

def ai_assistant():
    print(f"\nBusiness: {business['name']}")
    print(f"Today Sales: Rs. {business['today_sales']}")
    print(f"Yesterday Sales: Rs. {business['yesterday_sales']}")
    
    # Growth Calculation
    growth = ((business['today_sales'] - business['yesterday_sales']) / business['yesterday_sales']) * 100
    print(f"Growth: {growth:.1f}%")

    print("\n--- CLAUDE AI INSIGHTS ---")
    
    if growth > 0:
        print(f"✅ Great! Sales {growth:.1f}% up hai.")
        print("💡 Suggestion: Aaj best-selling product par WhatsApp offer bhejo.")
    else:
        print("⚠️ Sales down hai.")
        print("💡 Suggestion: Old customers ko follow-up message karo.")

    print(f"\n📦 Pending Orders: {business['pending_orders']}")
    print("💡 Suggestion: Sabse pehle pending orders dispatch karo.")
    
    print(f"\n⚠️ Low Stock: {', '.join(business['low_stock_items'])}")
    print("💡 Suggestion: Aaj hi 100 units re-order karo, warna kal loss hoga.")

    print("\n--- TOMORROW PLAN ---")
    print("1. Morning: Stock check")
    print("2. Afternoon: Customer follow-up")
    print("3. Evening: Sales report with Claude")

ai_assistant()

print("\n" + "="*60)
print("✅ Day 59 Complete")
print("Tech: Claude AI, Data Analysis, Business Automation")
print("GitHub: km0438591-arch/60-days-claude-ai-challenge")
