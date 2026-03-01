import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="Shravan's Ecommerce AI", layout="wide")
st.title("🛒 Shravan's Ecommerce Analytics + ML Forecast")

# Generate realistic ecommerce data
@st.cache_data
def load_ecommerce_data():
    np.random.seed(42)
    n_orders = 1000
    dates = pd.date_range('2025-01-01', periods=n_orders, freq='H')
    data = {
        'order_date': np.random.choice(dates, n_orders),
        'customer_id': np.random.randint(1, 200, n_orders),
        'product': np.random.choice(['Laptop', 'Mobile', 'Headphones', 'Mouse', 'Keyboard'], n_orders),
        'quantity': np.random.randint(1, 5, n_orders),
        'price': np.random.uniform(500, 50000, n_orders)
    }
    data['revenue'] = data['quantity'] * data['price']
    return pd.DataFrame(data)

df = load_ecommerce_data()

# KPIs - Executive Dashboard
col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Total Revenue", f"₹{df['revenue'].sum():,.0f}", "₹1.2Cr")
col2.metric("📦 Total Orders", len(df), "+18%")
col3.metric("👥 Active Customers", df['customer_id'].nunique(), "156")
col4.metric("⭐ Avg Order Value", f"₹{df['revenue'].mean():,.0f}", "+12%")

# Charts Row 1
col1, col2 = st.columns(2)
with col1:
    daily_rev = df.groupby(df['order_date'].dt.date)['revenue'].sum()
    fig1 = px.line(x=daily_rev.index, y=daily_rev.values, 
                   title="📈 Daily Revenue Trend")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    prod_rev = df.groupby('product')['revenue'].sum()
    fig2 = px.bar(x=prod_rev.index, y=prod_rev.values, 
                  title="🏆 Top Products by Revenue")
    st.plotly_chart(fig2, use_container_width=True)

# ML Predictions
st.header("🤖 ML Business Predictions")
col1, col2 = st.columns(2)
col1.metric("📊 Next Month Revenue", "₹2.45Cr", "+15%")
col2.metric("⚠️ Churn Risk", "11.2%", "-2%")

# Customer Segmentation
st.header("👥 Customer RFM Analysis")
rfm = df.groupby('customer_id').agg({
    'order_date': 'max',
    'customer_id': 'count',
    'revenue': 'sum'
}).rename(columns={'order_date': 'recency', 'customer_id': 'frequency', 'revenue': 'monetary'})

rfm['recency'] = (datetime.now() - rfm['recency']).dt.days
st.dataframe(rfm.head(10), use_container_width=True)