# Day 26: Build Your Personal Brand & AI Content Studio with Claude
# By Kanchan from Kanpur - Personal Brand for Founder

print("🎨 Day 26: Personal Brand & AI Content Studio")

def ai_content_studio():
    print("\n--- AI Content Studio - For Kanchan Personal Brand ---\n")
    
    # Your Brand
    niche = "Kanpur Girl Building AI for Kirana Shops"
    platform = "LinkedIn + Instagram"
    
    print(f"👩‍💼 Brand: {niche}")
    print(f"📱 Platform: {platform}")
    print("\n" + "="*60)
    
    # Claude Generates 7 Days Content Calendar
    print("\n📅 7 DAYS CONTENT CALENDAR (Claude Generated):")
    
    content_plan = [
        {"Day": "Mon", "Topic": "My Story", "Hook": "Kanpur ki ladki, laptop pe AI - kaise start kiya?", "Format": "LinkedIn Text + Photo"},
        {"Day": "Tue", "Topic": "Build in Public - Day 18", "Hook": "Excel automation se 5 Kirana kaise bachaya Rs 10k", "Format": "Carousel"},
        {"Day": "Wed", "Topic": "Tech Tutorial", "Hook": "Claude AI se 10 min me Kirana dashboard kaise banaye", "Format": "Reel - Hindi"},
        {"Day": "Thu", "Topic": "Shark Tank Pitch", "Hook": "AI Sharks ne mere idea ko 8% pe deal diya!", "Format": "Video - Day 25 story"},
        {"Day": "Fri", "Topic": "Kanpur Special", "Hook": "Itaunja ke Ramesh ji kaise use kar rahe mera AI?", "Format": "Customer Interview"},
        {"Day": "Sat", "Topic": "Failure Story", "Hook": "Day 19 me code fail hua, kaise fix kiya Claude se", "Format": "Honest Post"},
        {"Day": "Sun", "Topic": "Weekly Wins", "Hook": "Week me 1000+ views, 5 shops onboarded - Kanpur rocks!", "Format": "Stats + Thanks"},
    ]
    
    for post in content_plan:
        print(f"\n   {post['Day']} - {post['Topic']}:")
        print(f"     Hook: {post['Hook']}")
        print(f"     Format: {post['Format']}")
    
    # Claude Content Generator
    print("\n" + "="*60)
    print("\n✍️ CLAUDE CONTENT GENERATOR - Today's Post:")
    
    def generate_post(topic):
        prompt = f"Write LinkedIn post for {niche} about {topic} in Hinglish, with emoji, CTA"
        # Simulated Claude Output
        post_text = f"""
        Kanpur se ek ladki AI bana rahi hai! 🚀

        {topic} - Ye maine Claude AI se seekha

        60 Days Challenge ka Day 26 - Personal Brand banana mushkil tha,
        par Claude ne 7 din ka calendar bana diya!

        Itaunja se start kiya, ab 5 Kirana shops use kar rahe hai.
        Agar aap bhi small town se ho, toh AI aapke liye hai!

        Agla post: Mera Shark Tank wala experience 🦈

        #BuildInPublic #Kanpur #ClaudeAI #WomenInTech #ABTalks

        ---
        CTA: Comment karo - Aapka shop me kaunsa problem hai?
        """
        return post_text
    
    print(generate_post("Personal Brand is not showoff, it's sharing journey"))
    
    # Hashtag & Best Time
    print("\n📊 AI ANALYTICS (Claude Insights):")
    print("   Best Time to Post: 8 PM (Kanpur/Lucknow audience active)")
    print("   Best Hashtags: #Kanpur #BuildInPublic #ClaudeAI #WomenInTech #StartupIndia")
    print("   Growth Hack: Har post pe 10 logon ko tag karo - ABTalks community")
    
    print("\n✅ CONTENT STUDIO READY!")
    print("📁 All posts saved in /content_calendar/")

ai_content_studio()

# Streamlit Code for ABTalks
studio_code = '''
import streamlit as st

st.title("🎨 AI Content Studio - Day 26")
st.write("By Kanchan from Kanpur")

niche = st.text_input("Your Niche", "Kanpur Girl Building AI for Kirana")
topic = st.text_input("Today's Topic", "How I built Kirana AI in 7 days")

if st.button("Generate Content with Claude"):
    st.write(f"### Post for: {topic}")
    st.write(f"""
    Kanpur se ek ladki AI bana rahi hai! 🚀

    {topic}

    60 Days Claude Challenge - Day 26

    #BuildInPublic #Kanpur #ClaudeAI
    """)
    st.success("Post Generated! Copy to LinkedIn")
    st.balloons()
'''

print("\n--- Streamlit Code for ABTalks Deliverable ---")
print(studio_code)
print("\nDay 26 Complete - Personal Brand Ready!")
