import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Customer Journey Mapping", layout="wide")
st.title("🛤️ Customer Journey Mapping")

# Explanation section
with st.expander("ℹ️ What is Customer Journey Mapping?"):
    st.markdown("""
    **Customer Journey Mapping** is the process of creating a visual representation of the steps a customer takes when interacting with a company.
    
    This includes touchpoints like:
    - Awareness (Social Media, Ads)
    - Consideration (Website, Product Pages)
    - Conversion (Purchase, Sign-Up)
    - Retention (Support, Feedback)

    Mapping the customer journey helps identify pain points, opportunities for engagement, and areas to optimize customer experience.
    """)

# Select industry
industry = st.selectbox("Select Industry", ["Hospitality", "Retail"])

# Example input format based on industry
if industry == "Hospitality":
    st.subheader("🏨 Example Format: Hospitality Industry")
    hospitality_df = pd.DataFrame({
        "customer_id": ["H001", "H002", "H003"],
        "journey_steps": [
            ["Awareness", "Consideration", "Conversion", "Retention"],
            ["Awareness", "Conversion", "Retention"],
            ["Consideration", "Conversion", "Retention"]
        ]
    })
    st.dataframe(hospitality_df)

elif industry == "Retail":
    st.subheader("🛍️ Example Format: Retail Industry")
    retail_df = pd.DataFrame({
        "customer_id": ["R001", "R002", "R003"],
        "journey_steps": [
            ["Awareness", "Consideration", "Conversion"],
            ["Consideration", "Conversion"],
            ["Awareness", "Conversion"]
        ]
    })
    st.dataframe(retail_df)

# Simulate Journey Mapping Visualization
st.subheader("🔍 Customer Journey Mapping (Mock Example)")
if industry == "Hospitality":
    journey_data = hospitality_df.explode("journey_steps")
elif industry == "Retail":
    journey_data = retail_df.explode("journey_steps")

# Visualize the journey steps using a bar plot
journey_counts = journey_data["journey_steps"].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
journey_counts.plot(kind="bar", ax=ax, color="skyblue")
ax.set_title("Customer Journey Step Frequency")
ax.set_xlabel("Journey Step")
ax.set_ylabel("Frequency")
st.pyplot(fig)

st.markdown("📌 _Customer journey mapping helps identify which stages customers drop off and optimize the experience to improve conversions._")
