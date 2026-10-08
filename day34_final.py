# Claude Challenge - Day 34: Become a Marketing Detective
# Task: Reverse engineer a brand's marketing strategy

class MarketingDetective:
    def __init__(self, brand_name, ad_text, landing_page_url):
        self.brand = brand_name
        self.ad = ad_text
        self.landing = landing_page_url

    def investigate(self):
        print(f"\n🕵️ MARKETING DETECTIVE REPORT FOR: {self.brand}\n")
        
        # 1. Hook Analysis
        print("1. AD HOOK ANALYSIS:")
        hooks = []
        if "free" in self.ad.lower(): hooks.append("Freebie Hook (Lead Magnet)")
        if any(x in self.ad.lower() for x in ["you", "your"]): hooks.append("You-focused copy (Personalization)")
        if any(x in self.ad.lower() for x in ["limited","hurry","last"]): hooks.append("Scarcity/Urgency")
        if not hooks: hooks.append("Direct Benefit Hook")
        print(f"   Ad: '{self.ad}'")
        print(f"   Detected Hooks: {', '.join(hooks)}")

        # 2. Funnel Detection
        print("\n2. FUNNEL TYPE:")
        if "shop" in self.landing or "buy" in self.landing:
            funnel = "D2C Direct Sales Funnel (Ad -> Product Page -> Checkout)"
        elif "webinar" in self.landing or "free" in self.landing:
            funnel = "Lead Gen Funnel (Ad -> Free Value -> Email -> Sale)"
        else:
            funnel = "Content Funnel (Ad -> Blog/Video -> Retarget -> Sale)"
        print(f"   Landing: {self.landing}")
        print(f"   Funnel: {funnel}")

        # 3. Target Audience Guess
        print("\n3. TARGET AUDIENCE (Guessed from Ad):")
        if "student" in self.ad.lower():
            audience = "Students 18-24, Price sensitive, Instagram/TikTok"
        elif "professional" in self.ad.lower() or "productivity" in self.ad.lower():
            audience = "Working Professionals 24-32, Time-poor, LinkedIn/YouTube"
        else:
            audience = "Gen-Z 20-28, Interested in lifestyle, Instagram Reels"
        print(f"   {audience}")

        # 4. What They Are Doing Right / Wrong
        print("\n4. DETECTIVE INSIGHTS:")
        print("   ✅ What's Working: Strong hook, Clear CTA, Social Proof (if present)")
        print("   ❌ What's Missing: No urgency, No testimonial, Weak landing page copy")
        
        # 5. How I Would Beat Them
        print("\n5. MY COUNTER-STRATEGY (To Grow Faster Than Them):")
        print("   -> Same hook + Better offer: Add 10% OFF + Free Shipping")
        print("   -> Better creative: Use UGC video instead of stock image")
        print("   -> Retargeting: Show testimonial ad to people who clicked but didn't buy")

# ---- PROOF OF WORK DEMO ----
if __name__ == "__main__":
    # Example 1: Real brand jaisa
    case1 = MarketingDetective(
        brand_name="BrewSoul Coffee",
        ad_text="Free sample! Coffee that keeps you productive without jitters - for professionals",
        landing_page_url="brewsoul.com/free-sample"
    )
    case1.investigate()

    print("\n" + "="*70 + "\n")

    # Example 2: Tu yahan apna target brand daal de
    case2 = MarketingDetective(
        brand_name="Your Target Brand from Task",
        ad_text="Limited offer - Eco-friendly bottle loved by 10k+ students",
        landing_page_url="ecosip.com/shop"
    )
    case2.investigate()
