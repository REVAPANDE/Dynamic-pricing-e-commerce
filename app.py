import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go

# -------------------------------
# Load Model
# -------------------------------
model = joblib.load("pricing_model.pkl")

# -------------------------------
# Streamlit Page Config
# -------------------------------
st.set_page_config(
    page_title="Dynamic Pricing Dashboard",
    page_icon="💰",
    layout="wide",
)

# -------------------------------
# Custom CSS for Aesthetic Look
# -------------------------------
st.markdown("""
    <style>
    body {
        background-color: #f8f9fa;
        color: #333333;
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 2px 15px rgba(0,0,0,0.05);
    }
    h1, h2, h3 {
        color: #2b6777;
        font-family: 'Poppins', sans-serif;
    }
    .metric-card {
        background: #f0f5f9;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0px 1px 8px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Header Section
# -------------------------------
st.markdown("<h1 style='text-align:center;'>🛍️ Dynamic Pricing Optimizer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:16px;'>Adjust prices smartly to maximize revenue using machine learning</p>", unsafe_allow_html=True)
st.markdown("---")

# -------------------------------
# Sidebar Inputs
# -------------------------------
st.sidebar.title("⚙️ Product Configuration")

price = st.sidebar.number_input("Current Price (₹)", min_value=50, max_value=5000, value=500)
competitor_price = st.sidebar.number_input("Competitor Price (₹)", min_value=50, max_value=5000, value=520)
cost_price = st.sidebar.number_input("Cost Price (₹)", min_value=10, max_value=4000, value=300)
promo_flag = st.sidebar.selectbox("Promo Active?", [0, 1])
day_of_week = st.sidebar.slider("Day of Week", 0, 6, 3)
is_weekend = st.sidebar.selectbox("Is Weekend?", [0, 1])
month = st.sidebar.slider("Month", 1, 12, 6)

# -------------------------------
# Data Preparation
# -------------------------------
input_data = pd.DataFrame({
    "price": [price],
    "competitor_price": [competitor_price],
    "cost_price": [cost_price],
    "promo_flag": [promo_flag],
    "day_of_week": [day_of_week],
    "is_weekend": [is_weekend],
    "month": [month]
})

# -------------------------------
# Prediction
# -------------------------------
predicted_units = model.predict(input_data)[0]
revenue = price * predicted_units

# Simulate multiple price points for optimization
prices = np.linspace(price * 0.8, price * 1.2, 20)
revenues = []
for p in prices:
    sample = input_data.copy()
    sample["price"] = p
    demand = model.predict(sample)[0]
    revenues.append(demand * p)
opt_idx = np.argmax(revenues)
optimal_price = prices[opt_idx]
max_revenue = revenues[opt_idx]

# -------------------------------
# Display Results
# -------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"<div class='metric-card'><h3>Predicted Units Sold</h3><h2>{predicted_units:.1f}</h2></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='metric-card'><h3>Expected Revenue</h3><h2>₹{revenue:,.2f}</h2></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='metric-card'><h3>Optimized Price</h3><h2>₹{optimal_price:,.2f}</h2></div>", unsafe_allow_html=True)

st.markdown("---")

# -------------------------------
# Revenue Curve (Plotly)
# -------------------------------
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=prices,
    y=revenues,
    mode='lines+markers',
    line=dict(color='#2b6777', width=3),
    marker=dict(size=7),
    name='Revenue Curve'
))
fig.add_vline(x=optimal_price, line=dict(color='green', width=2, dash='dot'),
              annotation_text="Optimal Price", annotation_position="top right")
fig.update_layout(
    title="📊 Revenue vs. Price Curve",
    xaxis_title="Price (₹)",
    yaxis_title="Revenue (₹)",
    template="plotly_white",
    height=400,
    margin=dict(l=30, r=30, t=60, b=30),
)
st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# Footer
# -------------------------------
st.markdown("""
<hr>
<p style='text-align:center; font-size:14px; color:gray;'>
Developed for academic use • Dynamic Pricing System © 2025
</p>
""", unsafe_allow_html=True)
