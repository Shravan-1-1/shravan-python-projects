import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="Shravan Job Tracker", layout="wide")

# Job Data (Fixed!)
JOBS = {
    "RRB Section Controller": {"deadline": "2026-04-15", "status": "Applied", "priority": "High"},
    "SBI CBO": {"deadline": "2026-05-20", "status": "Prepare", "priority": "High"},
    "RBI Assistant": {"deadline": "2026-06-10", "status": "Prepare", "priority": "Medium"},
    "SSC CGL": {"deadline": "2026-07-01", "status": "Plan", "priority": "Medium"}
}

# Session state
if 'progress' not in st.session_state:
    st.session_state.progress = {job: 20 for job in JOBS}

# Sidebar
st.sidebar.title("🔥 Shravan Job Tracker")
st.sidebar.markdown("**Day 8 - Data Science Dashboard**")

# Main Dashboard
st.title("🎯 SHR AVAN JOB TRACKER DASHBOARD")
st.markdown("**RRB • SBI • RBI • SSC | Progress + Deadlines**")

# Metrics Row - FIXED!
col1, col2, col3, col4 = st.columns(4)
total_jobs = len(JOBS)
high_priority = sum(1 for job_data in JOBS.values() if job_data["priority"] == "High")

with col1:
    st.metric("Total Jobs", total_jobs)
with col2:
    st.metric("High Priority", high_priority)
with col3:
    avg_progress = sum(st.session_state.progress.values()) / len(JOBS)
    st.metric("Avg Progress", f"{avg_progress:.0f}%")
with col4:
    # FIXED: JOBS[job]["deadline"] instead of job["deadline"]
    urgent = sum(1 for job in JOBS if (datetime.strptime(JOBS[job]["deadline"], "%Y-%m-%d") - datetime.now()).days < 30)
    st.metric("Urgent", urgent)

# Progress Chart
st.subheader("📊 Progress Overview")
df_progress = pd.DataFrame([
    {"Job": job, "Progress": st.session_state.progress[job], "Priority": JOBS[job]["priority"]}
    for job in JOBS
])
fig_progress = px.bar(df_progress, x="Job", y="Progress", 
                     color="Priority", title="Job Progress")
st.plotly_chart(fig_progress, use_container_width=True)

# Deadline Timeline
st.subheader("⏰ Deadline Timeline")
df_deadlines = pd.DataFrame([
    {"Job": job, "Deadline": datetime.strptime(JOBS[job]["deadline"], "%Y-%m-%d")}
    for job in JOBS
])
fig_timeline = px.timeline(df_deadlines, x_start="Deadline", x_end="Deadline", y="Job", 
                          title="Exam Deadlines")
st.plotly_chart(fig_timeline, use_container_width=True)

# Job Cards with Progress Sliders
st.subheader("⚡ Quick Actions")
for i, job in enumerate(JOBS):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"**{job}**")
        st.caption(f"Deadline: {JOBS[job]['deadline']} | {JOBS[job]['priority']}")
    with col2:
        progress = st.slider(f"{job}", 0, 100, 
                           st.session_state.progress[job], key=f"slider_{i}")
        st.session_state.progress[job] = progress

# Urgent Alerts - FIXED!
st.subheader("🚨 URGENT ALERTS")
urgent_jobs = [job for job in JOBS 
              if (datetime.strptime(JOBS[job]["deadline"], "%Y-%m-%d") - datetime.now()).days < 60]
for job in urgent_jobs:
    days_left = (datetime.strptime(JOBS[job]["deadline"], "%Y-%m-%d") - datetime.now()).days
    st.error(f"⏰ {job}: {days_left} days left!")