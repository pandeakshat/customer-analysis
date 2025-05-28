import streamlit as st

st.set_page_config(page_title="Customer Analytics Dashboard", layout="wide")

st.sidebar.title("Customer Analytics Dashboard")

import streamlit as st

# Module readiness and corresponding links
status = {
    "Customer Churn": {"ready": True, "link": "/Customer-Churn"},
    "Customer Segmentation": {"ready": True, "link": "/Customer-Segmentation"},
    "NPS & VOC": {"ready": True, "link": "/NPS-VOC-Analysis"},
    "Geo-Spatial Analysis": {"ready": True, "link": "/Geo-Spatial-Analysis"},
    "Sentiment Analysis": {"ready": True, "link": "/Sentiment-Analysis"},
    "Upsell & Cross-Sell": {"ready": True, "link": "/Upsell-Cross-sell-Analysis"},
    "Journey Mapping": {"ready": True, "link": "/Customer-Journey-Mapping"},
    "Dynamic Pricing": {"ready": True, "link": "/Dynamic-Pricing-Optimization"},
    "Marketing Campaigns": {"ready": True, "link": "/Personalized-Marketing-Campaigns"},
    "Demand Forecasting": {"ready": True, "link": "/Demand-Forecasting"},

}

st.title("🧠 Customer Analytics Dashboard")
st.subheader("Module Readiness Overview")

cols_per_row = 3
i = 0
columns = st.columns(cols_per_row)  # initialize first row

for module, meta in status.items():
    ready = meta["ready"]
    link = meta["link"]
    color = "#4CAF50" if ready else "#F44336"
    icon = "✔️" if ready else "❌"

    card_html = f"""
    <a href="{link}" style="text-decoration: none;">
        <div style='background-color:{color}; padding:20px; border-radius:10px; text-align:center; color:white'>
            <h4>{module}</h4>
            <p style='font-size:30px'>{icon}</p>
        </div>
    </a>
    """

    with columns[i % cols_per_row]:
        st.markdown(card_html, unsafe_allow_html=True)

    i += 1

    if i % cols_per_row == 0:
        st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
        columns = st.columns(cols_per_row)  # start a new row
