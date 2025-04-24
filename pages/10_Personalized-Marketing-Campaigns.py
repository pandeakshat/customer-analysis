import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Personalized Marketing Campaigns", layout="wide")
st.title("🎯 Personalized Marketing Campaigns")

# Explanation section
with st.expander("ℹ️ What is Personalized Marketing?"):
    st.markdown("""
    **Personalized Marketing** uses customer data and analytics to create targeted campaigns
    tailored to individual preferences, behaviors, and needs.

    **Applications:**
    - Email campaigns based on customer preferences
    - Targeting specific segments with tailored offers
    - Predicting customer needs using historical data

    **Benefits:**
    - Increased engagement
    - Higher conversion rates
    - Improved loyalty

    In this module, you can:
    - Create customer segments based on behavior
    - Suggest personalized offers based on customer data
    """)

# Select industry
industry = st.selectbox("Select Industry", ["Hospitality", "Retail"])

# Build DataFrame per industry
if industry == "Hospitality":
    st.subheader("🏨 Example Format: Hospitality Industry")
    df = pd.DataFrame({
        "customer_id": ["H001", "H002", "H003"],
        "total_spend":   [1200, 800, 1500],
        "average_rating":[4.5, 3.8, 4.9],
        "loyalty_points":[200, 100, 250],  # use this instead of purchase_frequency
    })
elif industry == "Retail":
    st.subheader("🛍️ Example Format: Retail Industry")
    df = pd.DataFrame({
        "customer_id": ["R001", "R002", "R003"],
        "total_spend":       [500, 300, 700],
        "purchase_frequency":[15, 8, 20],  # use this for retail
        "last_purchase_date":["2025-02-01", "2025-03-15", "2025-01-10"],
    })

st.dataframe(df)

# Campaign targeting function
def campaign_targeting(row, industry):
    if industry == "Hospitality":
        # use loyalty_points for hospitality
        if row["total_spend"] > 1000 and row["loyalty_points"] > 150:
            return "Target with Special Offer"
        elif row["total_spend"] > 500:
            return "Target with Discount"
        else:
            return "Send Loyalty Reminder"
    else:  # Retail
        if row["total_spend"] > 1000 and row["purchase_frequency"] > 10:
            return "Target with Special Offer"
        elif row["total_spend"] > 500:
            return "Target with Discount"
        else:
            return "Send Loyalty Reminder"

# Apply targeting
df["campaign_targeting"] = df.apply(lambda r: campaign_targeting(r, industry), axis=1)
st.subheader("🔍 Personalized Campaign Targeting (Mock Example)")
st.dataframe(df)

# Visualization
st.subheader("📊 Campaign Targeting Distribution")
counts = df["campaign_targeting"].value_counts()
fig, ax = plt.subplots(figsize=(8,5))
counts.plot(kind="bar", ax=ax)
ax.set_title("Campaign Type Counts")
ax.set_xlabel("Campaign Type")
ax.set_ylabel("Number of Customers")
st.pyplot(fig)

st.markdown("📌 _This logic uses loyalty points in Hospitality and purchase frequency in Retail to decide which campaign to run._")
