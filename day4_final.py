# Day 4 - Kanpur Social Media Content Generator
# Created by Kanchan from Kanpur - 60 Days Claude Challenge

def generate_post(business, festival, offer):
    print(f"--- Post for {business} ---")
    
    # Instagram Post
    insta_post = f"""
    🚀 {business} - Kanpur Special!
    {festival} ka dhamaka offer! 🎉
    
    {offer}
    
    📍 Location: Kanpur
    📞 DM for orders
    #Kanpur #KanpurBusiness #{business.replace(' ', '')} #ABTalks #ClaudeAI
    
    Created by Kanchan
    """
    
    # WhatsApp Message
    whatsapp_msg = f"""
    *{business}* - {festival} Offer! 🙏
    {offer}
    Jaldi aaiye, offer limited hai!
    - Kanchan, Kanpur
    """
    
    print("INSTAGRAM POST:")
    print(insta_post)
    print("\nWHATSAPP MESSAGE:")
    print(whatsapp_msg)
    print("\n" + "="*40 + "\n")

# Testing - 3 examples for Kanpur
generate_post("Kakadeo Chai Wala", "Diwali", "Har Chai pe 1 Samosa FREE! Shaam 5-8 baje tak.")
generate_post("KDA Coaching Center", "New Year", "IIT-JEE Batch me 50% OFF, sirf pehle 20 students ke liye.")
generate_post("Kanpur Kirana Store", "Holi", "Har 500 ki kharid pe 50 ka cashback, UPI pe!")

print("Day 4 Done - Kanchan from Kanpur")
