# Day 47 - Content Intelligence Studio - By Kanchan Maurya
import streamlit as st
import time

st.set_page_config(page_title="Content Intelligence Studio - Day 47", page_icon="📊", layout="wide")
st.title("📊 Content Intelligence Studio")
st.subheader("Day 47 - Claude Challenge | By Kanchan Maurya")
st.markdown("### AI-Powered Content Analysis Platform - Content daalo, Report le lo!")

content = st.text_area("✍️ Apna Content Yaha Paste Karo", "I love data analysis! Python is amazing. I built 3 projects in OIBSIP internship with 99.7% accuracy. Data is future!")
platform = st.selectbox("Platform", ["Instagram", "LinkedIn", "YouTube", "Blog", "Twitter"])
content_type = st.selectbox("Content Type", ["Post", "Caption", "Blog", "Script", "Reel"])

if st.button("🚀 Analyze My Content"):
    with st.spinner("AI Content padh raha hai..."):
        time.sleep(2)
    
    words = len(content.split())
    chars = len(content)
    
    # Sentiment simple logic
    positive_words = ["love", "amazing", "great", "best", "awesome", "future", "success", "happy"]
    negative_words = ["bad", "sad", "fail", "worst", "hate", "boring"]
    pos = sum(1 for w in positive_words if w.lower() in content.lower())
    neg = sum(1 for w in negative_words if w.lower() in content.lower())
    
    if pos > neg:
        sentiment = "😊 Positive"
        sentiment_score = 85
    elif neg > pos:
        sentiment = "😞 Negative"
        sentiment_score = 30
    else:
        sentiment = "😐 Neutral"
        sentiment_score = 55
    
    seo_score = 60 + (words//2)
    if seo_score > 95: seo_score = 92
    if "#" in content: seo_score += 5
    engage = 70 + pos*5
    if engage > 95: engage = 94
    readability = 80 if words < 100 else 65

    st.success("✅ Analysis Complete!")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Words", words)
    with col2:
        st.metric("SEO Score", f"{seo_score}/100")
    with col3:
        st.metric("Engagement", f"{engage}%")
    with col4:
        st.metric("Readability", f"{readability}/100")

    st.markdown(f"### 🎭 Sentiment: {sentiment} - {sentiment_score}%")
    st.progress(sentiment_score/100)

    st.markdown(f"### 📈 Viral Prediction: {engage}% Chance Viral Hoga!")
    st.progress(engage/100)
    if engage >= 80:
        st.balloons()
        st.markdown("### 🔥 VIRAL HONE WALA HAI! Post kar de!")
    else:
        st.markdown("### 🟡 Thoda improve kar - fir viral hoga!")

    st.markdown("---")
    st.markdown("### 🏷️ Topic Detected:")
    if "data" in content.lower() or "python" in content.lower():
        st.info("📊 Topic: Data Science / Python - Trending hai!")
    elif "love" in content.lower():
        st.info("❤️ Topic: Motivation / Lifestyle")
    else:
        st.info("📌 Topic: General - Education")

    st.markdown("### 💡 AI Suggestions to Improve:")
    st.write("✅ Hook strong kar - Pehli line me number daal - 99.7% jaisa")
    st.write("✅ Hashtag add kar - 5-10 hashtags")
    st.write("✅ CTA add kar - 'Comment karo' 'Share karo'")
    st.write("✅ Emoji add kar - 3-4 emoji")
    st.write(f"✅ {platform} ke liye best time - 9 AM / 7 PM")

    st.markdown("### 🔥 Improved Version - COPY KAR LE:")
    st.code(content + "\n\n🚀 Follow for more! | #DataAnalyst #Python #OIBSIP #DataScience\n\n👉 Comment karo - Tumhe kaunsa topic chahiye?")

    st.markdown("### 📊 Platform Optimization:")
    st.write(f"Platform: {platform} | Type: {content_type} | Best Length: {words} words - Perfect hai!")

st.markdown("---")
st.markdown("**Made by Kanchan Maurya | Day 47 - Claude Challenge**")
