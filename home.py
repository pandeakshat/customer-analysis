
import streamlit as st

# Sample status dictionary
status = {
    "Customer Churn": True,
    "Sentiment Analysis": True,
    "Segmentation": False,
    "Upsell & Cross-Sell": False,
    "Journey Mapping": False,
    "Dynamic Pricing": False,
    "Marketing Campaigns": False,
    "Demand Forecasting": False,
    "NPS & VOC": False,
    "Geo-Spatial Analysis": True
}

st.set_page_config(page_title="Dashboard Home", layout="wide")
st.title("🧠 Customer Analytics Dashboard")
st.subheader("Module Readiness Overview")

cols = st.columns(3)
i = 0
for module, ready in status.items():
    color = "#4CAF50" if ready else "#F44336"
    icon = "✔️" if ready else "❌"
    with cols[i % 3]:
        st.markdown(
            f"""
            <div style='background-color:{color}; padding:20px; border-radius:10px; text-align:center; color:white'>
                <h4>{module}</h4>
                <p style='font-size:30px'>{icon}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    i += 1
