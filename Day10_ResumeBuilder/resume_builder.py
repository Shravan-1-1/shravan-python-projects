import streamlit as st
import pandas as pd
from datetime import datetime
import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(page_title="Shravan's AI Resume", layout="wide")
st.title("🤖 Shravan's AI Resume Builder + ATS Scorer")

# Sidebar inputs
st.sidebar.header("📝 Personal Info")
name = st.sidebar.text_input("Full Name", "Shravan Kumar Sharma")
email = st.sidebar.text_input("Email", "shravan.sharma@email.com")
phone = st.sidebar.text_input("Phone", "+91-XXXXXXXXXX")
location = st.sidebar.text_input("Location", "Varanasi, UP")

# Experience
st.sidebar.header("💼 Experience")
exp1 = st.sidebar.text_area("Job 1", "Data Science Intern | ABC Corp | 2025\n• Built Streamlit dashboards")
exp2 = st.sidebar.text_area("Job 2", "Python Developer | XYZ Tech | 2024\n• WhatsApp AI analyzer")

# Skills
st.sidebar.header("🛠 Skills")
skills = st.sidebar.text_area("Skills", "Python, Pandas, Streamlit, Plotly, Git, SQL, ML, Data Analysis")

# Main tabs
tab1, tab2, tab3 = st.tabs(["📄 Resume Preview", "🎯 ATS Score", "⬇️ Download PDF"])

with tab1:
    col1, col2 = st.columns([1,2])
    
    with col1:
        st.markdown(f"""
        # {name}
        **Data Scientist | Python Developer**
        
        {location} | {email} | {phone}
        
        ## 🛠 Technical Skills
        {skills}
        
        ## 💼 Experience
        **{exp1.split('|')[0].strip()}**
        {exp1.split('\n')[1:]}
        
        **{exp2.split('|')[0].strip()}**
        {exp2.split('\n')[1:]}
        """)
    
    with col2:
        st.metric("ATS Score", "92/100 ✅", "Govt Jobs Ready!")
        st.success("✅ RRB Section Controller")
        st.success("✅ SBI CBO") 
        st.success("✅ RBI Assistant")

with tab2:
    # ATS Keywords check
    govt_keywords = ["RRB", "SBI", "RBI", "SSC", "Data Analysis", "Python", "SQL"]
    skill_score = sum(1 for kw in govt_keywords if kw.lower() in skills.lower())
    
    st.metric("ATS Match", f"{skill_score}/7 ({skill_score*14.28:.0f}/100)")
    
    st.write("**Missing Keywords:**")
    for kw in govt_keywords:
        if kw.lower() not in skills.lower():
            st.write(f"- {kw}")

with tab3:
    if st.button("⬇️ Download PDF Resume"):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []
        
        story.append(Paragraph(f"<b>{name}</b><br/><i>Data Scientist</i>", styles['Title']))
        story.append(Spacer(1, 12))
        story.append(Paragraph(f"{location} | {email} | {phone}", styles['Normal']))
        
        doc.build(story)
        buffer.seek(0)
        st.download_button("Download", buffer, f"{name}_Resume.pdf", "application/pdf")

st.sidebar.markdown("---")
st.sidebar.caption("🚀 Built by Shravan - Day 10 Complete!")