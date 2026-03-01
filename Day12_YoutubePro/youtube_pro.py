import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Shravan's YouTube Pro AI", layout="wide")
st.title("🌐 Shravan's YouTube Pro - Live Trends + Sentiment")

# Enhanced mock data (Real API Day 13)
@st.cache_data
def load_pro_data():
    data = {
        'title': [
            'RRB NTPC 2026 Complete Strategy | 100% Selection', 
            'Python Data Science Roadmap 2026 | Govt Jobs',
            'SBI PO 2026 Mock Test | 150 Questions',
            'Streamlit Portfolio Projects | Interview Ready',
            'Pandas Advanced | Data Analyst Interview'
        ],
        'channel': ['GovtExamMaster', 'TechCareer360', 'BankingGuru', 
                   'DataScienceHub', 'PythonPro'],
        'views': [245000, 189000, 156000, 112000, 98000],
        'likes': [18500, 14200, 11800, 8900, 7200],
        'comments': [3200, 2100, 1870, 1450, 980],
        'sentiment': [0.87, 0.92, 0.79, 0.94, 0.88],
        'viral_score': [9.2, 9.5, 8.8, 9.7, 9.1]
    }
    return pd.DataFrame(data)

df = load_pro_data()

# KPIs - 2 Rows
col1, col2, col3, col4 = st.columns(4)
col1.metric("📈 Live Videos", len(df), 12)
col2.metric("👀 Total Views", f"{df['views'].sum():,.0f}", "+15%")
col3.metric("❤️ Engagement", f"{df['likes'].sum():,.0f}", "+22%")
col4.metric("🤖 Top Sentiment", f"{df['sentiment'].max():.2f}", "Positive")

# Charts Row 1
col1, col2 = st.columns(2)
with col1:
    fig1 = px.bar(df.sort_values('views', ascending=False), 
                  x='views', y='title', orientation='h',
                  title="🏆 Top Videos by Views", color='viral_score')
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.scatter(df, x='views', y='sentiment', size='likes',
                     color='viral_score', hover_name='title',
                     title="🎯 Viral vs Quality Matrix")
    st.plotly_chart(fig2, use_container_width=True)

# Recommendations + Export
st.header("🚀 AI Career Recommendations")
rec_df = df.nlargest(5, 'viral_score').copy()
for idx, row in rec_df.iterrows():
    st.success(f"**🎥 {row['title']}**")
    st.caption(f"👤 {row['channel']} | 📊 Views:{row['views']:,.0f} | ❤️ {row['likes']:,.0f} | 🤖 {row['sentiment']:.2f}")

# CSV Download
csv = df.to_csv(index=False)
st.download_button("💾 Export Trends CSV", csv, "youtube_trends.csv", "text/csv")

st.sidebar.markdown("---")
st.sidebar.caption("🚀 Day 12 Complete - 11:59 PM Target!")