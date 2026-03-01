import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Shravan's WhatsApp AI", layout="wide")
st.title("🤖 Shravan's WhatsApp Chat Analyzer")

# File upload
uploaded_file = st.file_uploader("Upload WhatsApp chat (.txt)", type="txt")

if uploaded_file:
    # Read chat
    chat_data = uploaded_file.read().decode('utf-8')
    
    # Parse WhatsApp format
    messages = []
    for line in chat_data.split('\n'):
        if re.match(r'\[\d{1,2}/\d{1,2}/\d{2}', line):
            date_time = line[:17]
            rest = line[17:]
            sender = rest.split(': ')[0] if ': ' in rest else 'Unknown'
            msg = ': '.join(rest.split(': ')[1:]) if ': ' in rest else rest
            messages.append({'date': date_time, 'sender': sender, 'message': msg})
    
    df = pd.DataFrame(messages)
    df['date'] = pd.to_datetime(df['date'], format='%m/%d/%y, %I:%M %p')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Total Messages", len(df))
        st.metric("Unique People", df['sender'].nunique())
        st.metric("Avg Messages/Day", round(len(df)/30, 1))
    
    with col2:
        top_sender = df['sender'].value_counts().index[0]
        st.metric("Most Active", top_sender)
        st.metric("Your Messages", len(df[df['sender']=='Shravan']))
    
    # Charts
    tab1, tab2, tab3 = st.tabs(["📊 Activity", "😊 Sentiment", "☁️ Words"])
    
    with tab1:
        daily_activity = df.groupby(df['date'].dt.date).size()
        fig1 = px.line(x=daily_activity.index, y=daily_activity.values, 
                      title="Daily Messages")
        st.plotly_chart(fig1)
    
    with tab2:
        st.write("Sentiment Analysis Coming Soon! 🚀")
    
    with tab3:
        st.write("Word Cloud Coming Soon! 🌈")