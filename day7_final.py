# Day 7: Claude Model Selection & Reasoning Effort
# By Kanchan from Kanpur

def choose_claude_model(task_type):
    task_type = task_type.lower()
    
    if "simple" in task_type or "poster" in task_type or "message" in task_type:
        return "Use Claude 3.5 Haiku - Fast & Cheap. Example: 'Kirana ke liye Diwali poster ka text likh do' - 2 sec me ho jayega"
    
    elif "thinking" in task_type or "business plan" in task_type or "profit" in task_type:
        return "Use Claude 3.5 Sonnet with Extended Thinking - Soch samajh ke jawab dega. Example: 'Kakadeo me nayi dukaan kholne ka profit calculation karo step-by-step'"
    
    elif "code" in task_type or "dashboard" in task_type:
        return "Use Claude 3.5 Sonnet - Best for Coding. Example: 'Python me dashboard code likho'"
    
    else:
        return "Default: Claude 3.5 Sonnet - Balanced for most tasks"

# Testing
print("Task 1: Kirana ka WhatsApp message likhna")
print(choose_claude_model("simple poster"))
print("\n")

print("Task 2: Kirana store ka 1 saal ka business plan banana")
print(choose_claude_model("thinking business plan"))
print("\n")

print("Task 3: AI Dashboard ka code banana")
print(choose_claude_model("code dashboard"))
print("\n")

# Reasoning Effort Example
print("--- Reasoning Effort Demo ---")
print("Low Effort: 'Dukaan ka naam batao' -> Quick answer")
print("High Effort: 'Dukaan kyu fail hui? Profit, location, customer sab soch ke batao' -> Deep thinking with steps")

print("\nDay 7 Complete - Kanchan")
