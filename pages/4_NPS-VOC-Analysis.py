import streamlit as st
import pandas as pd

st.set_page_config(page_title="NPS & VOC Analysis", layout="wide")
st.title("🌟 NPS & VOC (Voice of Customer) Analysis")

# Explanation section
with st.expander("ℹ️ What is NPS & VOC Analysis?"):
    st.markdown("""
    **Net Promoter Score (NPS)** measures customer loyalty by asking how likely a customer is to recommend a business to others.
    
    NPS is calculated using the following scale:
    - **Promoters (9-10)**: Loyal customers who will keep buying and refer others.
    - **Passives (7-8)**: Satisfied but unenthusiastic customers.
    - **Detractors (0-6)**: Unhappy customers who could damage the brand through negative word of mouth.

    **Voice of Customer (VOC)** captures customer feedback through surveys, reviews, and interactions to understand customer satisfaction.

    NPS helps measure customer sentiment over time and VOC analyzes specific customer feedback for actionable insights.
    """)

# Select industry
industry = st.selectbox("Select Industry", ["Hospitality", "Retail"])

# Example input format based on industry
if industry == "Hospitality":
    st.subheader("🏨 Example Format: Hospitality Industry")
    hospitality_df = pd.DataFrame({
        "customer_id": ["H001", "H002", "H003"],
        "nps_score": [9, 7, 3],
        "feedback": ["Great experience", "Good stay, but food could improve", "Terrible service"],
    })
    st.dataframe(hospitality_df)

elif industry == "Retail":
    st.subheader("🛍️ Example Format: Retail Industry")
    retail_df = pd.DataFrame({
        "customer_id": ["R001", "R002", "R003"],
        "nps_score": [10, 8, 5],
        "feedback": ["Highly satisfied with my purchase", "Good product, fast delivery", "Product broke after a week"],
    })
    st.dataframe(retail_df)

# Simulated NPS Calculation
st.subheader("🔍 NPS Calculation (Mock Example)")
nps_data = pd.DataFrame({
    "customer_id": ["H001", "H002", "H003"],
    "nps_score": [9, 7, 3]
})

# NPS Categories
promoters = nps_data[nps_data["nps_score"] >= 9].shape[0]
passives = nps_data[(nps_data["nps_score"] >= 7) & (nps_data["nps_score"] <= 8)].shape[0]
detractors = nps_data[nps_data["nps_score"] <= 6].shape[0]

# Calculate NPS
total_respondents = len(nps_data)
nps_score = ((promoters - detractors) / total_respondents) * 100

st.write(f"Promoters: {promoters}, Passives: {passives}, Detractors: {detractors}")
st.write(f"✅ NPS Score: {nps_score:.2f}%")

# Simulated VOC (Voice of Customer) feedback summary
st.subheader("📊 VOC Feedback Analysis (Mock)")
voc_data = pd.DataFrame({
    "customer_id": ["H001", "H002", "H003"],
    "feedback": ["Great experience", "Good stay, but food could improve", "Terrible service"],
})

st.write("Customer Feedback Summary:")
st.write(voc_data["feedback"].value_counts())

st.markdown("📌 _The NPS score helps measure customer loyalty while VOC gives insights into areas needing improvement._")
