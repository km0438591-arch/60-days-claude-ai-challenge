# Day 9: Prompt Chaining - Multi-Step AI Workflow
# By Kanchan from Kanpur - 60 Days Claude Challenge
# Use Case: Kanpur Kirana ke liye Auto Content Generator

print("🔗 Day 9: Prompt Chaining Demo - Kanpur Kirana")

# Step 1, 2, 3 ko jodna hi Prompt Chaining hai

def prompt_chain_for_kirana(product):
    
    # CHAIN STEP 1: Idea Generation
    prompt1 = f"You are a Kanpur local marketing expert. Give 1 catchy offer idea for {product} for Kakadeo students."
    output1 = f"Offer Idea for {product}: 'Student Combo - Buy 1kg {product} + Free Kurkure for Rs 99 only!'"
    print(f"\n[CHAIN 1 - Idea]: {prompt1}")
    print(f"-> Output 1: {output1}")

    # CHAIN STEP 2: Convert to WhatsApp Message
    prompt2 = f"Convert this offer '{output1}' into a short WhatsApp message in Hinglish with emojis."
    output2 = f"🏪 Kakadeo Offer! 📚 {product} ka Student Combo sirf Rs 99 me + FREE Kurkure! Aaj shaam 9 baje tak only! Jaldi aao! 🏃‍♀️"
    print(f"\n[CHAIN 2 - WhatsApp]: {prompt2}")
    print(f"-> Output 2: {output2}")

    # CHAIN STEP 3: Create Poster Text + Action Plan
    prompt3 = f"For this message '{output2}', give poster headline + shop action plan"
    output3 = f"Poster Headline: 'KAKADEO STUDENT DHAMAKA - {product.upper()} @ 99/-' | Action: 1. Print A4 poster 2. WhatsApp Status 3. Announce in shop"
    print(f"\n[CHAIN 3 - Poster & Action]: {prompt3}")
    print(f"-> Output 3: {output3}")

    print(f"\n✅ FINAL CHAIN RESULT FOR {product.upper()}: Ready to post!")

# Test with 2 products
prompt_chain_for_kirana("Aata")
print("\n" + "="*60 + "\n")
prompt_chain_for_kirana("Biscuit")

print("\nDay 9 Complete - Prompt Chaining Mastered!")
print("By Kanchan from Kanpur")
