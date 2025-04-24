import streamlit as st
import pandas as pd
from textblob import TextBlob

st.set_page_config(page_title="Sentiment Analysis", layout="wide")
st.title("💬 Sentiment Analysis")

# Explanation section
with st.expander("ℹ️ What is Sentiment Analysis?"):
    st.markdown("""
    **Sentiment Analysis** uses natural language processing (NLP) to determine the emotional tone behind a series of words.
    
    It helps identify positive, negative, or neutral sentiment from customer feedback, reviews, or surveys.

    **Applications:**
    - Understanding customer opinions
    - Analyzing reviews or social media mentions
    - Categorizing feedback into sentiment classes
    
    In this module, you can:
    - Analyze sentiment for reviews in the hospitality or retail industry
    - Visualize sentiment distributions
    """)

# Select industry
industry = st.selectbox("Select Industry", ["Hospitality", "Retail"])

# Example input format based on industry
if industry == "Hospitality":
    st.subheader("🏨 Example Format: Hospitality Industry")
    hospitality_df = pd.DataFrame({
        "customer_id": ["H001", "H002", "H003"],
        "review": ["Great experience, will visit again!", "Service was average, not happy.", "Very disappointed with the service."],
    })
    st.dataframe(hospitality_df)

elif industry == "Retail":
    st.subheader("🛍️ Example Format: Retail Industry")
    retail_df = pd.DataFrame({
        "customer_id": ["R001", "R002", "R003"],
        "review": ["Love the product, highly recommend!", "Product was fine, delivery took too long.", "Very bad experience, won't buy again."],
    })
    st.dataframe(retail_df)

# Function to analyze sentiment
def analyze_sentiment(review):
    blob = TextBlob(review)
    return blob.sentiment.polarity

# Apply sentiment analysis to the reviews
st.subheader("🔍 Sentiment Analysis Output")
if industry == "Hospitality":
    hospitality_df["sentiment_score"] = hospitality_df["review"].apply(analyze_sentiment)
    hospitality_df["sentiment"] = hospitality_df["sentiment_score"].apply(lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Neutral"))
    st.dataframe(hospitality_df)

elif industry == "Retail":
    retail_df["sentiment_score"] = retail_df["review"].apply(analyze_sentiment)
    retail_df["sentiment"] = retail_df["sentiment_score"].apply(lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Neutral"))
    st.dataframe(retail_df)

# Simulated sentiment distribution chart
st.subheader("📊 Sentiment Distribution")
sentiment_counts = hospitality_df["sentiment"].value_counts() if industry == "Hospitality" else retail_df["sentiment"].value_counts()
st.bar_chart(sentiment_counts)

st.markdown("📌 _Sentiment analysis helps businesses understand customer emotions and improve services._")
