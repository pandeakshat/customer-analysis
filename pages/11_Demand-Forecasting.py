import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prophet import Prophet

st.set_page_config(page_title="Demand Forecasting", layout="wide")
st.title("📈 Demand Forecasting")

# Explanation section
with st.expander("ℹ️ What is Demand Forecasting?"):
    st.markdown("""
    **Demand Forecasting** is the process of predicting future demand for products or services, based on historical data, trends, and seasonality.
    
    **Applications:**
    - Predicting product sales for inventory management
    - Forecasting hotel room bookings or restaurant demand
    - Anticipating customer traffic for optimal staffing

    In this module, you can:
    - Apply time series forecasting models (e.g., ARIMA, Prophet)
    - Visualize demand trends and predictions
    """)

# Select industry
industry = st.selectbox("Select Industry", ["Hospitality", "Retail"])

# Example input format based on industry
if industry == "Hospitality":
    st.subheader("🏨 Example Format: Hospitality Industry")
    dates = pd.date_range("2023-01-01", "2023-12-31", freq="D")
    bookings = np.random.poisson(lam=20, size=len(dates))
    hospitality_df = pd.DataFrame({"ds": dates, "y": bookings})
    st.dataframe(hospitality_df)

else:  # Retail
    st.subheader("🛍️ Example Format: Retail Industry")
    dates = pd.date_range("2023-01-01", "2023-12-31", freq="W")
    sales = np.random.poisson(lam=500, size=len(dates))
    retail_df = pd.DataFrame({"ds": dates, "y": sales})
    st.dataframe(retail_df)

# Forecasting function
def forecast_demand(df, periods, freq):
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=periods, freq=freq)
    forecast = model.predict(future)
    return forecast

st.subheader("🔍 Demand Forecasting")

# Run and display forecasts
if industry == "Hospitality":
    # daily data → 365 days ahead
    forecast_hospitality = forecast_demand(hospitality_df, periods=365, freq="D")
    st.write("Forecast for next year (Hospitality):")
    st.dataframe(forecast_hospitality[["ds", "yhat", "yhat_lower", "yhat_upper"]])

else:
    # weekly data → 52 weeks ahead
    forecast_retail = forecast_demand(retail_df, periods=52, freq="W")
    st.write("Forecast for next year (Retail):")
    st.dataframe(forecast_retail[["ds", "yhat", "yhat_lower", "yhat_upper"]])

# Visualization
st.subheader("📊 Demand Forecast Visualization")
fig, ax = plt.subplots(figsize=(10, 6))

if industry == "Hospitality":
    forecast_hospitality.set_index("ds")["yhat"].plot(ax=ax)
elif industry == "Retail":
    forecast_retail.set_index("ds")["yhat"].plot(ax=ax)

ax.set_title("Demand Forecast")
ax.set_xlabel("Date")
ax.set_ylabel("Demand")
st.pyplot(fig)

st.markdown("📌 _Demand forecasting helps businesses plan for the future by predicting customer demand trends._")
