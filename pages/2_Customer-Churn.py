import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Churn", layout="wide")
st.title("🚪 Customer Churn Prediction")

# Section: Introduction & Explanation
with st.expander("ℹ️ What is Customer Churn Prediction?"):
    st.markdown("""
    **Customer Churn Prediction** is the process of identifying customers who are likely to stop using a product or service.
    
    This prediction helps businesses take proactive actions to retain valuable customers and reduce revenue loss.

    **Typical features include:**
    - Recency of last interaction or transaction
    - Frequency of purchases or bookings
    - Customer satisfaction scores (ratings or reviews)
    - Lifetime value and spending behavior
    - Industry-specific behaviors (e.g., stay history in hospitality, purchases in retail)
    
    In this module, you can:
    - View example data formats for different industries
    - Explore test predictions for demo data
    - Upload your own data in future versions to get churn predictions
    """)

# Section: Industry selection
industry = st.selectbox("Select Industry", ["Hospitality", "Retail"])

# Section: Example data per industry
if industry == "Hospitality":
    st.subheader("🏨 Example Format: Hospitality Industry")
    hospitality_df = pd.DataFrame({
        "customer_id": ["C001", "C002", "C003"],
        "last_stay_date": ["2024-12-01", "2025-01-15", "2025-03-10"],
        "total_bookings": [5, 2, 8],
        "total_spend": [1200, 400, 2000],
        "avg_review_score": [4.5, 3.8, 4.9],
        "has_churned": [0, 1, 0]  # target
    })
    st.dataframe(hospitality_df)

elif industry == "Retail":
    st.subheader("🛍️ Example Format: Retail Industry")
    retail_df = pd.DataFrame({
        "customer_id": ["R001", "R002", "R003"],
        "last_purchase_date": ["2025-02-01", "2025-01-20", "2025-03-05"],
        "total_orders": [10, 3, 12],
        "lifetime_value": [500, 120, 850],
        "avg_rating": [4.2, 3.5, 4.8],
        "has_churned": [1, 1, 0]  # target
    })
    st.dataframe(retail_df)

# Section: Mock test predictions
st.subheader("🔮 Churn Prediction Example (Mock Data)")
test_data = pd.DataFrame({
    "customer_id": ["T001", "T002"],
    "last_purchase_date": ["2025-03-15", "2025-02-10"],
    "total_orders": [7, 2],
    "lifetime_value": [300, 100],
    "avg_rating": [4.0, 3.2],
})
st.dataframe(test_data)

st.markdown("✅ **Prediction Output (Mock):**")
st.success("- T001 → Not likely to churn")
st.error("- T002 → High risk of churn")

# Footer note
st.markdown("---")
st.markdown("📌 _In future versions, you will be able to upload your own dataset and generate predictions in real-time using trained machine learning models._")
