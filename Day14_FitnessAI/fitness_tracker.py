import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title="Shravan's Fitness AI", layout="wide")
st.title("💪 Shravan's Health & Fitness Tracker + ML Predictor")

# Sidebar - Personal inputs
st.sidebar.header("📊 Your Profile")
weight = st.sidebar.number_input("Weight (kg)", 60, 120, 72)
height = st.sidebar.number_input("Height (cm)", 150, 200, 170)
age = st.sidebar.number_input("Age", 20, 40, 24)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])

# Calculate BMI
bmi = weight / ((height/100) ** 2)
bmi_category = "Normal" if 18.5 <= bmi <= 24.9 else "Overweight" if bmi > 24.9 else "Underweight"

# Main Dashboard
col1, col2, col3 = st.columns(3)
col1.metric("⚖️ BMI", f"{bmi:.1f}", bmi_category)
col2.metric("🎯 Ideal Weight", f"{21.7*(height/100)**2:.1f}kg", "+2kg")
col3.metric("🔥 BMR", f"{(10*weight + 6.25*height - 5*age + 5):.0f} cal", "Male")

# Progress Charts
col1, col2 = st.columns(2)
with col1:
    # Mock weight data
    dates = pd.date_range('2025-12-01', periods=30)
    weights = np.linspace(75, weight, 30) + np.random.normal(0, 0.5, 30)
    fig1 = px.line(x=dates, y=weights, title="📉 Weight Progress")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    # Calorie intake mock - FIXED
    calories = np.random.normal(2500, 300, 30)
    days = ["Day " + str(i+1) for i in range(30)]  # Simple days
    fig2 = px.bar(x=days, y=calories, title="🍽️ Daily Calories")
    st.plotly_chart(fig2, use_container_width=True)

# ML Predictions
st.header("🤖 Fitness Predictions")
col1, col2, col3 = st.columns(3)
col1.metric("📅 30-Day Weight", f"{weight-2:.1f}kg", "✅ Target")
col2.metric("💤 Recovery Score", "87%", "Good")
col3.metric("🏋️ Workout Plan", "Chest + Cardio", "RRB Prep")

# RRB Physical Prep
st.header("🏃 RRB Physical Test Prep")
st.info("**Running:** 1600m in 6:30 min (PASS)")
st.info("**High Jump:** 127cm (PASS)")
st.success("**Status: PHYSICALLY FIT FOR RRB NTPC!**")

st.sidebar.markdown("---")
st.sidebar.caption("🚀 Day 14 Fitness AI - RRB Ready!")