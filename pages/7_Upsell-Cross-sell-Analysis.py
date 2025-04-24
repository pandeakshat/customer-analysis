import streamlit as st
import pandas as pd
import itertools

st.set_page_config(page_title="Upsell & Cross-Sell Analysis", layout="wide")
st.title("🔄 Upsell & Cross-Sell Analysis")

# Explanation section
with st.expander("ℹ️ What is Upsell & Cross-Sell Analysis?"):
    st.markdown("""
    **Upsell and Cross-Sell** strategies are used to maximize customer value by encouraging them to purchase more expensive items (upsell) or complementary products (cross-sell).
    
    **Upselling**:
    - Encourages the customer to buy a higher-value product.
    
    **Cross-Selling**:
    - Encourages the customer to buy complementary products.

    **Applications:**
    - Identifying products that frequently get purchased together (association rules)
    - Creating personalized product recommendations
    
    In this module, you can:
    - Discover frequently co-purchased products
    - Suggest products for upselling or cross-selling based on customer behavior
    """)

# Select industry
industry = st.selectbox("Select Industry", ["Hospitality", "Retail"])

# Example input format based on industry
if industry == "Hospitality":
    st.subheader("🏨 Example Format: Hospitality Industry")
    hospitality_df = pd.DataFrame({
        "customer_id": ["H001", "H002", "H003"],
        "products_purchased": [["Room1", "Spa"], ["Room2", "Pool"], ["Room1", "Gym"]],
    })
    st.dataframe(hospitality_df)

elif industry == "Retail":
    st.subheader("🛍️ Example Format: Retail Industry")
    retail_df = pd.DataFrame({
        "customer_id": ["R001", "R002", "R003"],
        "products_purchased": [["Shirt", "Pants"], ["Shoes", "Socks"], ["Hat", "Scarf"]],
    })
    st.dataframe(retail_df)

# Function to generate product pairs for upsell/cross-sell
def generate_pairs(products_list):
    pairs = list(itertools.combinations(products_list, 2))
    return pairs

# Generate product pairs for cross-sell recommendations
st.subheader("🔍 Cross-Sell Product Recommendations (Mock Example)")

if industry == "Hospitality":
    hospitality_df["product_pairs"] = hospitality_df["products_purchased"].apply(generate_pairs)
    all_pairs = list(itertools.chain(*hospitality_df["product_pairs"]))
    pair_df = pd.DataFrame(all_pairs, columns=["Product A", "Product B"])
    st.dataframe(pair_df)

elif industry == "Retail":
    retail_df["product_pairs"] = retail_df["products_purchased"].apply(generate_pairs)
    all_pairs = list(itertools.chain(*retail_df["product_pairs"]))
    pair_df = pd.DataFrame(all_pairs, columns=["Product A", "Product B"])
    st.dataframe(pair_df)

# Simulate the best cross-sell pairs based on frequency (mock)
st.subheader("📊 Cross-Sell Pair Frequency")
pair_frequency = pair_df.value_counts().reset_index(name='Frequency')
pair_frequency.columns = ["Product A", "Product B", "Frequency"]
st.dataframe(pair_frequency)

st.markdown("📌 _Upsell and Cross-Sell strategies can improve your business’s revenue by identifying valuable combinations of products._")
