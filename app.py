import requests
import streamlit as st

# Define News API endpoint and API key
NEWS_API_ENDPOINT = "https://newsapi.org/v2/top-headlines"
NEWS_API_KEY = "ac3f3e2ed56f4528b58c17e7471ab1fd"

# Define parameters for API request
params = {"country": "us", "pageSize": 20}

# Make API request and handle errors
response = requests.get(NEWS_API_ENDPOINT, params=params, headers={"Authorization": f"Bearer {NEWS_API_KEY}"})
if response.status_code != 200:
    st.error("Failed to fetch news from News API.")
    st.stop()

# Extract news headlines from API response
articles = response.json()["articles"]

# Display headlines in a Streamlit app
st.write("# Top Headlines")
for article in articles:
    st.write(f'- [{article["title"]}]({article["url"]})')
