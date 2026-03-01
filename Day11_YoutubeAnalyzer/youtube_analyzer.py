import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Shravan's YouTube AI", layout="wide")
st.title("🎥 Shravan's YouTube Trend Analyzer + ML Recommender")

# Mock trending data (Real YouTube API coming Day 12)
@st.cache_data
def load_trending_data():
    data = {
        'title': ['Python for Data Science in 1 Hour', 'RRB NTPC 2026 Full Prep', 
                 'Streamlit Dashboard Tutorial', 'Pandas 50 Exercises', 'SBI PO Mock Test'],
        'channel': ['TechBit', 'GovtExamGuru', 'DataProf', 'CodeWithHarry', 'BankingMaster'],
        'views': [125000, 85000, 45000, 32000, 21000],
        'likes': [8500, 6200, 3800, 2800, 1800],
        'viral_score': [8.2, 7.9, 9.1, 8.8, 7.5]
    }
    return pd.DataFrame(data)

df = load_trending_data()

# Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Videos", len(df))
col2.metric("Avg Views", f"{df['views'].mean():,.0f}")
col3.metric("Top Viral Score", f"{df['viral_score'].max():.1f}")
col4.metric("Govt Job Videos", len(df[df['channel'].str.contains('Govt|RRB|SBI')]))

# Charts
col1, col2 = st.columns(2)
with col1:
    fig1 = px.bar(df, x='channel', y='views', title="Views by Channel")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.scatter(df, x='views', y='viral_score', 
                     size='likes', hover_name='title',
                     title="Viral Potential Matrix")
    st.plotly_chart(fig2, use_container_width=True)

# ML Recommendations
st.header("🤖 AI Career Recommendations")
rec_df = df.nlargest(3, 'viral_score')
for idx, row in rec_df.iterrows():
    st.success(f"🎯 **{row['title']}** by {row['channel']}")
    st.info(f"📊 Views: {row['views']:,.0f} | Viral Score: {row['viral_score']:.1f}")