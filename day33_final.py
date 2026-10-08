# Claude Challenge - Day 33: Build a Media Integrity Analyzer
# Detects: Clickbait, Fake News Signals, Bias, Image Manipulation Hints

import re
from datetime import datetime

class MediaIntegrityAnalyzer:
    def __init__(self):
        self.clickbait_words = ["shocking", "you won't believe", "viral", "breaking", "exposed", "secret", "100% true", "guaranteed"]
        self.bias_words = ["always", "never", "worst ever", "best ever", "everyone knows"]
        self.unverified_patterns = [r"forwarded", r"whatsapp university", r"source says"]

    def analyze_text(self, text, source="Unknown"):
        score = 100
        flags = []

        # 1. Clickbait Check
        lower = text.lower()
        for word in self.clickbait_words:
            if word in lower:
                score -= 15
                flags.append(f"⚠️ Clickbait word found: '{word}'")

        # 2. ALL CAPS / Excessive Punctuation
        if len(re.findall(r"[A-Z]{4,}", text)) > 2 or "!!!" in text:
            score -= 10
            flags.append("⚠️ Excessive CAPS / !!! - Sensationalism")

        # 3. Bias Check
        for word in self.bias_words:
            if word in lower:
                score -= 10
                flags.append(f"⚠️ Absolute/Bias language: '{word}'")

        # 4. Source Credibility
        trusted_sources = ["reuters", "ap news", "bbc", "the hindu", "pib"]
        if not any(s in source.lower() for s in trusted_sources):
            if source == "Unknown" or "whatsapp" in source.lower():
                score -= 20
                flags.append(f"⚠️ Unverified Source: {source}")

        # 5. No Date / Old News
        if not re.search(r"\d{4}", text):
            flags.append("ℹ️ No date mentioned - Could be old news")

        # Final Verdict
        if score >= 80:
            verdict = "✅ LIKELY AUTHENTIC"
        elif score >= 50:
            verdict = "⚠️ NEEDS VERIFICATION"
        else:
            verdict = "❌ LIKELY MISLEADING / FAKE"

        return {"score": max(0, score), "verdict": verdict, "flags": flags}

    def analyze_image_hint(self, has_metadata=True, is_edited=False):
        # Simple image integrity logic
        if not has_metadata:
            return "❌ No EXIF/metadata - Possibly stripped / edited"
        if is_edited:
            return "⚠️ Editing software detected in metadata"
        return "✅ Metadata present - No obvious manipulation"

# ---- DEMO FOR PROOF OF WORK ----
if __name__ == "__main__":
    analyzer = MediaIntegrityAnalyzer()
    
    samples = [
        ("SHOCKING!!! You won't believe what Modi said - VIRAL secret exposed!!!", "WhatsApp Forward"),
        ("Reuters reports: India GDP grows 7.2% in Q1 2026 as per official data", "Reuters"),
        ("Everyone knows this drink will CURE cancer guaranteed!!! Forwarded", "Unknown")
    ]

    print(f"MEDIA INTEGRITY ANALYZER - Day 33 Report {datetime.now().date()}\n")
    for text, src in samples:
        result = analyzer.analyze_text(text, src)
        print(f"TEXT: {text[:60]}...")
        print(f"SOURCE: {src} | SCORE: {result['score']}/100 | {result['verdict']}")
        for f in result['flags']:
            print(f"  - {f}")
        print("-"*70)
    
    print("\nIMAGE CHECK:")
    print(analyzer.analyze_image_hint(has_metadata=False))
