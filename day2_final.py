# Day 2 - Smart Prompt Generator for Kanpur Businesses
# Created by Kanchan - Kanpur

def generate_prompt(business_type, goal):
    prompt = f"""
    You are an AI expert for {business_type} in Kanpur.
    Goal: {goal}
    Location: Kanpur, Uttar Pradesh
    Language: Mix of Hindi + English (Kanpuriya style)
    Task: Create a detailed, helpful, step-by-step plan.
    Make it practical for local audience.
    """
    return prompt

# Example 1 - Kirana Store
print("--- PROMPT 1 ---")
print(generate_prompt("Kirana Store in Kakadeo", "Increase daily sales using WhatsApp"))

# Example 2 - Coaching
print("\n--- PROMPT 2 ---")
print(generate_prompt("IIT Coaching in Kanpur", "Get more students from KDA market"))

# Example 3 - Your Goal
print("\n--- PROMPT 3 ---")
print(generate_prompt("AI Tools for Kanpur", "Help local shopkeepers go digital"))
