# Day 2: What Is Prompt Engineering
# By Kanchan, Kanpur
# Concept: Clear, Specific, Context + Instruction + Example = Good Prompt

# BAD Prompt vs GOOD Prompt
bad_prompt = "Write about kirana store"

good_prompt = """
Context: You are helping a Kirana store owner in Kakadeo, Kanpur.
Task: Write 3 WhatsApp marketing messages in Hindi + English mix.
Audience: Local families in Kanpur
Tone: Friendly, Kanpuriya
Constraint: Each message < 30 words, include UPI payment mention.
Example: "Namaste! Aaj daal pe 10% off hai, Kakadeo store me. UPI se pay karo!"
Now generate 3 new messages.
"""

print("BAD PROMPT:")
print(bad_prompt)
print("\nGOOD PROMPT (Prompt Engineering Applied):")
print(good_prompt)
print("\nDay 2 Done - Kanchan")
