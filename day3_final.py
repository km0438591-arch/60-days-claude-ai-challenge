# Day 3 - Kanpur Business Chatbot using Claude
# Created by Kanchan from Kanpur - ABTalks 60 Days Challenge

def kanpur_biz_bot(user_question):
    user_question = user_question.lower()
    
    if "kirana" in user_question or "dukaan" in user_question:
        return "Kanpur ke Kirana store ke liye: 1. WhatsApp Broadcast list banao 2. UPI QR code bada print karke lagao 3. Shaam 6-9 baje special offer rakho."
    
    elif "coaching" in user_question or "student" in user_question:
        return "Kakadeo / KDA coaching ke liye: 1. Instagram pe daily 1 doubt video dalo 2. Test series ka PDF WhatsApp pe bhejo 3. Kanpuriya Hindi me padhao, English me note do."
    
    elif "marketing" in user_question or "customer" in user_question:
        return "Customer badhane ke liye: Claude se 3 kaam karao - 1. Poster banao 2. WhatsApp message likhwao 3. Customer ka feedback summary karwao."
    
    else:
        return f"Aapne pucha: '{user_question}'. Main Kanchan ka Kanpur Business Bot hu! Kirana, Coaching, ya Marketing ke baare me pucho, main Kanpur style me jawab dunga."

# Testing Bot
print("--- Kanpur Bot Testing ---")
print(kanpur_biz_bot("Meri kirana dukaan kaise chalegi?"))
print("\n")
print(kanpur_biz_bot("Coaching me students kaise badhaye?"))
print("\n")
print(kanpur_biz_bot("Marketing idea do"))

print("\nBot Ready! Day 3 Done - Kanchan from Kanpur")
