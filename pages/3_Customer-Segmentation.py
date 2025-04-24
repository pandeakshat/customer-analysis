import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Segmentation", layout="wide")
st.title("🧭 Customer Segmentation")

# Explanation section
with st.expander("ℹ️ What is Customer Segmentation?"):
    st.markdown("""
    **Customer Segmentation** involves dividing a customer base into distinct groups based on shared characteristics.
    
    This enables personalized marketing, targeted promotions, better service delivery, and higher retention.

    **Common segmentation techniques:**
    - RFM (Recency, Frequency, Monetary) Analysis
    - K-Means Clustering
    - Demographic or Behavioral Grouping

    **Applications in Hospitality:**
    - Identifying Business Travelers vs. Leisure Guests
    - Segmenting by spend and booking frequency

    **Applications in Retail:**
    - Loyalty-based tiering
    - High spenders vs. discount-seekers
    """)

# Select industry
industry = st.selectbox("Select Industry", ["Hospitality", "Retail"])

# Example input format based on industry
if industry == "Hospitality":
    st.subheader("🏨 Example Format: Hospitality Industry")
    hospitality_df = pd.DataFrame({
        "customer_id": ["H001", "H002", "H003"],
        "total_stays": [10, 3, 15],
        "avg_stay_value": [150, 100, 250],
        "recency_days": [15, 90, 7],
    })
    st.dataframe(hospitality_df)

elif industry == "Retail":
    st.subheader("🛍️ Example Format: Retail Industry")
    retail_df = pd.DataFrame({
        "customer_id": ["R001", "R002", "R003"],
        "total_orders": [20, 5, 30],
        "avg_order_value": [50, 25, 70],
        "recency_days": [12, 45, 5],
    })
    st.dataframe(retail_df)

# Simulated Segmentation Output
st.subheader("🔍 Segmentation Output Example (Mock)")
segment_result = pd.DataFrame({
    "customer_id": ["H001", "H002", "H003"],
    "Segment": ["Premium", "Budget", "Loyalist"]
})
st.dataframe(segment_result)

st.markdown("📌 _These segments are created using K-Means or RFM clustering based on customer behavior._")
