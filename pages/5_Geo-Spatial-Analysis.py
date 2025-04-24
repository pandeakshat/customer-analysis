import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static


st.set_page_config(page_title="Geo-Spatial Analysis", layout="wide")
st.title("🗺️ Geo-Spatial Analysis")

# Explanation section
with st.expander("ℹ️ What is Geo-Spatial Analysis?"):
    st.markdown("""
    **Geo-Spatial Analysis** helps visualize, interpret, and analyze spatial data (location-based data) to uncover patterns, trends, and correlations.
    
    **Applications:**
    - Customer distribution maps
    - Store performance by region
    - Delivery zones optimization
    - Geographical clustering for market targeting

    In this module, you can:
    - View customer distribution maps
    - Visualize customer density and other spatial patterns
    """)

# Select industry
industry = st.selectbox("Select Industry", ["Hospitality", "Retail"])

# Example input format based on industry
if industry == "Hospitality":
    st.subheader("🏨 Example Format: Hospitality Industry")
    hospitality_df = pd.DataFrame({
        "customer_id": ["H001", "H002", "H003"],
        "latitude": [51.5074, 48.8566, 40.7128],  # London, Paris, NYC latitudes
        "longitude": [-0.1278, 2.3522, -74.0060],  # London, Paris, NYC longitudes
    })
    st.dataframe(hospitality_df)

elif industry == "Retail":
    st.subheader("🛍️ Example Format: Retail Industry")
    retail_df = pd.DataFrame({
        "customer_id": ["R001", "R002", "R003"],
        "latitude": [34.0522, 40.7306, 41.8781],  # LA, NY, Chicago latitudes
        "longitude": [-118.2437, -73.9352, -87.6298],  # LA, NY, Chicago longitudes
    })
    st.dataframe(retail_df)

# Create a map visualization for customer locations
st.subheader("📍 Customer Location Map")
map_center = [51.5074, -0.1278]  # Default center (London)
m = folium.Map(location=map_center, zoom_start=2)

# Add markers with customer locations
marker_cluster = MarkerCluster().add_to(m)
for idx, row in hospitality_df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"Customer ID: {row['customer_id']}",
        icon=folium.Icon(color='blue')
    ).add_to(marker_cluster)

# Display map
st.markdown("### Customer Locations on Map")
folium_static(m)

# Simulated Geo-Spatial Insights (mock analysis)
st.subheader("🔍 Geo-Spatial Analysis Insights (Mock Example)")
st.markdown("📌 **Customer Density**: Higher concentration of customers in urban areas like New York and London.")
st.markdown("📌 **Target Areas**: We can target regions with fewer customers for marketing campaigns.")
