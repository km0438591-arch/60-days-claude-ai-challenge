# Day 9: Build & Enhance an AI Nutrition Analytics App
# By Kanchan from Kanpur - ABTalks 60 Days Claude Challenge

print("🥗 Day 9: AI Nutrition Analytics App - Kanpur Thali Edition")

# Kanpur ki Thali ka Data
food_items = {
    "Samosa (1pc)": {"calories": 250, "protein": 4, "carbs": 30, "fat": 15, "note": "High Fat - Avoid daily"},
    "Dal Chawal (1 plate)": {"calories": 350, "protein": 12, "carbs": 50, "fat": 8, "note": "Balanced - Good for lunch"},
    "Lassi (1 glass)": {"calories": 180, "protein": 6, "carbs": 20, "fat": 7, "note": "Good Protein"},
    "Biscuit (4pc)": {"calories": 200, "protein": 2, "carbs": 28, "fat": 9, "note": "High Sugar - Students avoid"},
    "Chana (100g)": {"calories": 180, "protein": 9, "carbs": 25, "fat": 3, "note": "Best for VVDN interview energy"}
}

def analyze_meal(items_eaten):
    total_cal = 0
    total_protein = 0
    print(f"\n--- Your Meal Analysis: {items_eaten} ---")
    for item in items_eaten:
        if item in food_items:
            data = food_items[item]
            total_cal += data["calories"]
            total_protein += data["protein"]
            print(f"{item}: {data['calories']} cal | {data['note']}")

    print(f"\nTotal Calories: {total_cal}")
    print(f"Total Protein: {total_protein}g")

    # Claude AI Insight
    if total_cal > 600:
        print("🤖 Claude Alert: Calories zyada hain! Shaam ko halka khana khao.")
    if total_protein < 10:
        print("🤖 Claude Suggestion: Protein kam hai - Chana / Lassi add karo.")

# Test 1: Student Diet
analyze_meal(["Samosa (1pc)", "Biscuit (4pc)"])
print("\n" + "="*40)
# Test 2: Healthy Diet
analyze_meal(["Dal Chawal (1 plate)", "Chana (100g)"])

print("\nDay 9 Complete - Nutrition App Ready!")
