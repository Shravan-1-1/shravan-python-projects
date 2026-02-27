import streamlit as st
import time

print("🌐 SHR AVAN DAY 6 - PROBLEM 3: STREAMLIT PORTFOLIO LIVE!")

# Page config
st.set_page_config(
    page_title="Shravan Portfolio",
    page_icon="🔥",
    layout="wide"
)

# Header
st.title("🔥 Shravan Kumar Sharma")
st.markdown("**Prayagraj, UP | B.Tech CSE | Govt Job + AI Aspirant**")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("📊 Quick Stats")
    st.metric("Projects Complete", "25+")
    st.metric("Days Mastered", "6/30")
    st.metric("GitHub Stars", "0⭐ (Help me!)")
    
    st.markdown("---")
    st.markdown("[GitHub → shravan-python-projects](https://github.com/Shravan-1-1/shravan-python-projects)")

# Featured Projects
st.header("🚀 Featured Projects")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    **Smart Bank** 💳
    - OOP + JSON
    - Deposit/Withdraw
    - Shravan VIP features
    """)
    st.success("✅ Complete")

with col2:
    st.markdown("""
    **Car Showroom** 🚗
    - Classes + Search
    - 10+ cars inventory
    - Filter by price
    """)
    st.success("✅ Complete")

with col3:
    st.markdown("""
    **Job Tracker** 📋
    - Govt exams deadlines
    - JSON alerts
    - Priority sorting
    """)
    st.success("✅ Complete")

with col4:
    st.markdown("""
    **WhatsApp Analyzer** 📱
    - File parsing
    - Stats dashboard
    - Message insights
    """)
    st.success("✅ Complete")

# Skills Progress
st.header("🛠️ Skills Mastered")
skills = {
    "Python Basics": 100,
    "Functions": 100,
    "OOP": 95,
    "File Handling": 100,
    "Git/GitHub": 90,
    "Streamlit": 85
}

for skill, progress in skills.items():
    st.progress(progress / 100)
    st.caption(skill)

# Footer
st.markdown("---")
st.markdown("""
**DAY 6/30 COMPLETE** - *Hirable Python Developer Ready!* 💼✨
**Connect:** [GitHub](https://github.com/Shravan-1-1) | Prayagraj
""")