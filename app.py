import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load("pricing_model.pkl")

st.set_page_config(page_title="🛒 Dynamic Pricing Optimizer", layout="wide")

# --- Header ---
st.title("🧠 AI Dynamic Pricing for E-Commerce")
st.markdown("""
This app predicts **product demand** and suggests the **optimal price** that maximizes revenue.  
Built with **Machine Learning (XGBoost)** and **Streamlit**.
""")

# Sidebar inputs
st.sidebar.header("📦 Product Features")
price = st.sidebar.number_input("Current Price (₹)", min_value=50, max_value=5000, value=500)
competitor_price = st.sidebar.number_input("Competitor Price (₹)", min_value=50, max_value=5000, value=520)
cost_price = st.sidebar.number_input("Cost Price (₹)", min_value=10, max_value=4000, value=300)
promo_flag = st.sidebar.selectbox("Promo Active?", [0, 1])
day_of_week = st.sidebar.slider("Day of Week (0=Mon, 6=Sun)", 0, 6, 3)
is_weekend = st.sidebar.selectbox("Is Weekend?", [0, 1])
month = st.sidebar.slider("Month (1–12)", 1, 12, 6)

# Create DataFrame
input_data = pd.DataFrame({
    "price": [price],
    "competitor_price": [competitor_price],
    "cost_price": [cost_price],
    "promo_flag": [promo_flag],
    "day_of_week": [day_of_week],
    "is_weekend": [is_weekend],
    "month": [month]
})

# Predict demand
predicted_units = model.predict(input_data)[0]
revenue = price * predicted_units

# Simulate multiple price points
prices = np.linspace(price * 0.8, price * 1.2, 10)
revenues = []
for p in prices:
    sample = input_data.copy()
    sample["price"] = p
    demand = model.predict(sample)[0]
    revenues.append(demand * p)
opt_idx = np.argmax(revenues)
optimal_price = prices[opt_idx]
max_revenue = revenues[opt_idx]

# --- Display ---
col1, col2 = st.columns(2)

with col1:
    st.metric("Predicted Units Sold", f"{predicted_units:.1f}")
    st.metric("Expected Revenue", f"₹{revenue:,.2f}")

with col2:
    st.metric("Optimized Price", f"₹{optimal_price:,.2f}")
    st.metric("Optimized Revenue", f"₹{max_revenue:,.2f}")

st.markdown("---")
st.subheader("📊 Revenue Optimization Curve")
st.line_chart(pd.DataFrame({"Price": prices, "Revenue": revenues}).set_index("Price"))

st.success("✅ Model successfully deployed with interactive pricing optimizer!")
