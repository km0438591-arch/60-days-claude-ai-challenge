# Day 1 - AI Assistant (No API Key Needed)
print("🤖 Claude Assistant - Day 1 Challenge")
print("Type 'exit' to quit\n")

while True:
    question = input("You: ")
    if question.lower() == "exit":
        print("Bye! Day 1 Done ✅")
        break
    
    # Simple intelligent replies
    if "who are you" in question.lower():
        print("Assistant: I am your Day 1 AI Assistant built with Python! 🚀")
    elif "python" in question.lower():
        print("Assistant: Python is a powerful language for AI. You are learning it on Day 1!")
    elif "name" in question.lower():
        print("Assistant: I am built by Kanchan for the 60-day challenge!")
    else:
        print(f"Assistant: Great question! '{question}' - This is Day 1 of my 60-day Claude AI journey. I will make this smarter with APIs soon!")
