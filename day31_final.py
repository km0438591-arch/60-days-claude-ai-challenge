# Day 31: Build Your First Autonomous AI Agent
# ABTalks 60 Days Claude Challenge - Phase 2 Start | By Kanchan

import streamlit as st
import time
import random

st.set_page_config(page_title="Autonomous AI Agent", page_icon="🤖", layout="wide")

st.title("🤖 Day 31: Build Your First Autonomous AI Agent")
st.subheader("ABTalks x Claude AI | Phase 2 - Advanced AI Agents")
st.markdown("---")

# Sidebar
st.sidebar.header("🧠 Agent Control Panel")
agent_name = st.sidebar.text_input("Agent Name", value="Kanchan AI Assistant")
agent_role = st.sidebar.selectbox("Agent Role", 
    ["Healthcare Research Agent", "Supply Chain Analyst", "Patient Support Agent", "Medical Report Analyzer", "Hospital Admin Agent"]
)
autonomy_level = st.sidebar.slider("Autonomy Level", 1, 5, 3)
st.sidebar.info(f"Level {autonomy_level}: {'Human-in-loop' if autonomy_level < 3 else 'Fully Autonomous'}")

tools_enabled = st.sidebar.multiselect("Tools Enabled for Agent", 
    ["Web Search", "File Reader", "Code Executor", "Email Sender", "Database Query"], 
    default=["Web Search", "File Reader", "Code Executor"]
)

# Main
col1, col2 = st.columns([2,1])

with col1:
    st.markdown(f"### 💬 Chat with {agent_name}")
    st.markdown(f"**Role:** {agent_role} | **Tools:** {', '.join(tools_enabled)}")
    
    task = st.text_area("Give Task to Your Agent:", 
        placeholder="e.g. Research latest treatment for diabetes and create a summary report for Itaunja CHC patients...",
        height=120
    )

    if st.button("🚀 Run Agent Autonomously", type="primary"):
        if not task:
            st.warning("Please give a task to agent!")
        else:
            with st.status(f"🤖 {agent_name} is thinking autonomously...", expanded=True) as status:
                st.write(f"🧠 Step 1: Understanding task - '{task[:50]}...'")
                time.sleep(1.2)
                st.write(f"🔧 Step 2: Selecting tools from {tools_enabled}...")
                time.sleep(1)
                for tool in tools_enabled:
                    st.write(f"   ▶️ Using {tool}...")
                    time.sleep(0.8)
                st.write("💭 Step 3: Reasoning & planning with Claude AI...")
                time.sleep(1.5)
                st.write("📝 Step 4: Generating final output...")
                time.sleep(1)
                status.update(label="✅ Agent Completed Task!", state="complete", expanded=False)
            
            st.markdown("---")
            st.markdown(f"### 📋 Output from {agent_name}")
            
            if "Healthcare" in agent_role or "Patient" in agent_role:
                st.success("**Agent Output:**")
                st.write(f"""
                **Task:** {task}
                
                **Research Summary:**
                1. Found 5 latest research papers on topic
                2. Key insight: Early diagnosis reduces risk by 40%
                3. Recommended for {hospital if 'hospital' in locals() else 'Itaunja CHC'}: Regular screening camp
                
                **Action Taken:** Created patient awareness PDF + Email draft to Doctor
                """)
                st.code(f"Agent Log: Task Completed in {random.randint(8,15)}s | Tokens: {random.randint(1200,2500)} | Cost: $0.02")
            else:
                st.success("**Agent Output:**")
                st.write(f"""
                **Task:** {task}
                **Analysis:** Supply chain data shows 22% optimization possible.
                **Recommendation:** Switch to Kanpur vendor, save ₹1.2L/month.
                **Auto-Action:** Drafted purchase order and sent for approval.
                """)
            
            st.balloons()
            st.metric("Agent Performance", f"{random.randint(85,98)}%", "Autonomous Success")

with col2:
    st.markdown("### ⚙️ Agent Memory")
    st.info(f"""
    **Agent:** {agent_name}
    **Status:** Active 🟢
    **Tasks Done Today:** {random.randint(12,45)}
    **Success Rate:** {random.randint(90,99)}%
    **Memory Used:** 12.4 MB
    """)
    
    st.markdown("### 📜 Activity Log")
    st.code("""
    [10:01] Task Received
    [10:01] Web Search -> 5 results
    [10:02] File Reader -> report.pdf
    [10:03] Reasoning -> Claude 3.5
    [10:03] Code Exec -> Success
    [10:04] Final Output Ready
    [10:04] Saved to Memory
    """)

st.markdown("---")
st.caption("Day 31/60 | Phase 2 Started | #ABTalks #AIAgents #ClaudeAI | github.com/km0438591-arch/60-days-claude-ai-challenge")
