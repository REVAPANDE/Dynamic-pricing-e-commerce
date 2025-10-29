# Dynamic Pricing Optimizer

An AI-powered pricing analytics tool that helps e-commerce businesses determine the optimal selling price to maximize revenue and profit.  
This project uses **Machine Learning** and **Streamlit** to provide real-time pricing insights through an interactive dashboard.

---

## Overview

**Dynamic Pricing Optimizer** simulates real-world e-commerce pricing scenarios by analyzing various factors such as current price, competitor price, cost price, promotions, seasonality, and weekday effects.  
The model predicts three key business metrics:

- Predicted Units Sold  
- Expected Revenue  
- Optimized Price  

The dashboard offers a visual representation of the **Revenue vs. Price** curve, helping decision-makers choose the best pricing strategy.

---

## Features

- Dynamic price prediction based on multiple business parameters  
- Configurable input controls for price, competition, and promotions  
- Real-time prediction of revenue and units sold  
- Interactive visualization of Revenue vs. Price curve  
- Modern Streamlit-based interface with dark theme  

---

## Tech Stack

| Category | Technologies |
|-----------|---------------|
| Frontend/UI | Streamlit |
| Backend | Python |
| Machine Learning | Scikit-learn |
| Data Handling | Pandas, NumPy |
| Visualization | Plotly |
| Deployment | Streamlit Cloud / Localhost |

---

## How It Works

1. **Input Configuration:**  
   Enter product details such as current price, competitor price, cost price, and promotional status.  

2. **Prediction Model:**  
   The trained regression model analyzes the inputs and predicts:  
   - Expected Units Sold  
   - Expected Revenue  
   - Optimized Price  

3. **Visualization:**  
   The app plots a **Revenue vs. Price** curve to show how revenue changes with different pricing points.  

---
