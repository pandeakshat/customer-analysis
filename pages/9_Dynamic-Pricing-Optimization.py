import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dynamic Pricing Optimization", layout="wide")
st.title("💸 Dynamic Pricing Optimization")

# Explanation section
with st.expander("ℹ️ What is Dynamic Pricing Optimization?"):
    st.markdown("""
    **Dynamic Pricing Optimization** is the process of adjusting the price of a product or service
    based on real-time market demand, competition, and other factors.

    **Use Cases**:
    - Adjusting hotel room prices based on occupancy
    - Pricing airline tickets based on demand and time to flight
    - Offering personalized discounts for customers based on purchasing behavior

    **Factors influencing dynamic pricing**:
    - Time of day, week, or season
    - Product availability
    - Competitor pricing
    - Customer purchasing behavior

    In this module, you can:
    - Simulate price adjustments based on demand
    - Visualize pricing strategies and optimize revenue
    """)

# Select industry
industry = st.selectbox("Select Industry", ["Hospitality", "Retail"])

# Build DataFrame and ensure it always has a 'demand_factor' column
if industry == "Hospitality":
    st.subheader("🏨 Example Format: Hospitality Industry")
    hospitality_df = pd.DataFrame({
        "room_type": ["Standard", "Deluxe", "Suite"],
        "base_price": [100, 150, 250],
        "occupancy_rate": [0.6, 0.8, 0.9],
        "competitor_price": [120, 170, 240]
    })
    # Map occupancy_rate onto demand_factor so the pricing function works uniformly:
    hospitality_df["demand_factor"] = hospitality_df["occupancy_rate"]
    df = hospitality_df

elif industry == "Retail":
    st.subheader("🛍️ Example Format: Retail Industry")
    retail_df = pd.DataFrame({
        "product_name": ["Shirt", "Jeans", "Jacket"],
        "base_price": [30, 50, 100],
        "demand_factor": [0.8, 1.2, 1.0],
        "competitor_price": [35, 55, 95]
    })
    df = retail_df

st.dataframe(df)

# Pricing function now always uses 'demand_factor'
def apply_dynamic_pricing(row):
    adjusted_price = row["base_price"] * row["demand_factor"]
    price_adjustment = adjusted_price - row["competitor_price"]
    return adjusted_price, price_adjustment

# Apply dynamic pricing adjustments
df[["adjusted_price", "price_adjustment"]] = df.apply(
    apply_dynamic_pricing, axis=1, result_type="expand"
)
st.subheader("🔍 Dynamic Pricing Optimization (Mock Example)")
st.dataframe(df)

# Visualization
st.subheader("📊 Pricing Strategy Visualization")
fig, ax = plt.subplots(figsize=(10, 6))

if industry == "Hospitality":
    df.plot(
        kind="bar",
        x="room_type",
        y=["base_price", "adjusted_price"],
        ax=ax
    )
elif industry == "Retail":
    df.plot(
        kind="bar",
        x="product_name",
        y=["base_price", "adjusted_price"],
        ax=ax
    )

ax.set_title("Base Price vs Adjusted Price")
ax.set_ylabel("Price ($)")
st.pyplot(fig)

st.markdown("📌 _Dynamic pricing helps businesses adjust to market changes in real-time, maximizing revenue based on demand._")
