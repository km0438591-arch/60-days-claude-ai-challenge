# Day 18: Build a Claude Skill for Excel Automation
# By Kanchan from Kanpur - Excel Automation for Kirana Shop

print("📊 Day 18: Claude Skill for Excel Automation - Kanpur Kirana")

# --- Excel Skill Logic ---
# Real me ye SKILL.md file banegi: .claude/skills/excel-automation/SKILL.md

skill_content = """
name: kanpur-excel-automation
description: Automate Kanpur shop bills, stock, sales reports in Excel with Claude
instructions:
    - User says: "Kirana ka monthly report banao"
    - Claude should: Create Excel with 3 sheets: Sales, Stock, Profit
    - Use formulas: SUM, VLOOKUP, conditional formatting for low stock
    - Language: Hindi + English mix for local shopkeeper
"""

print(skill_content)

# --- Python Demo: Claude Excel Automation ---
import pandas as pd
from datetime import datetime

def claude_excel_automation(shop_name):
    print(f"\n--- Claude Excel Skill Running for {shop_name} ---\n")

    # 1. Sample Data - Kanpur Kirana Shop
    sales_data = {
        "Date": ["2026-10-01", "2026-10-02", "2026-10-03", "2026-10-04"],
        "Product": ["Aata", "Chawal", "Tel", "Aata"],
        "Quantity": [10, 20, 15, 12],
        "Price_Per_Kg": [40, 50, 150, 40],
        "Total": [400, 1000, 2250, 480]
    }

    stock_data = {
        "Product": ["Aata", "Chawal", "Tel", "Cheeni"],
        "Current_Stock_Kg": [5, 100, 2, 50], # Low stock alert
        "Min_Stock": [20, 30, 10, 20]
    }

    df_sales = pd.DataFrame(sales_data)
    df_stock = pd.DataFrame(stock_data)

    # 2. Create Excel File with 3 Sheets
    file_name = f"{shop_name}_Report_{datetime.now().strftime('%d-%m-%Y')}.xlsx"
    
    with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
        df_sales.to_excel(writer, sheet_name='Sales', index=False)
        df_stock.to_excel(writer, sheet_name='Stock', index=False)
        
        # Profit Sheet - Auto Formula
        profit = df_sales["Total"].sum()
        df_profit = pd.DataFrame([{"Total_Sales": profit, "Profit_20%": profit * 0.2}])
        df_profit.to_excel(writer, sheet_name='Profit', index=False)

    print(f"✅ Excel File Created: {file_name}")
    print("\n--- Sales Sheet ---")
    print(df_sales)
    print("\n--- Stock Sheet (Claude Analysis) ---")
    for index, row in df_stock.iterrows():
        if row["Current_Stock_Kg"] < row["Min_Stock"]:
            print(f"🚨 LOW STOCK ALERT: {row['Product']} - Only {row['Current_Stock_Kg']}Kg left! Re-order now.")
        else:
            print(f"✅ {row['Product']} - Stock OK: {row['Current_Stock_Kg']}Kg")

    print(f"\n💰 Total Profit (20% margin): Rs {profit * 0.2}")
    print(f"💡 Claude Tip: Aata and Tel need urgent re-order for Kanpur shop!")

# --- Run for Kanpur Shop ---
claude_excel_automation("Kanpur_Kirana_Itaunja")

print("\n--- How to Use as Claude Skill ---")
print("1. User: 'Mere kirana ka bill Excel me banao'")
print("2. Claude Skill auto-creates: Sales, Stock, Profit sheets")
print("3. Adds formulas + Hindi alerts")
print("\nDay 18 Complete - Excel Automation Skill Ready!")
