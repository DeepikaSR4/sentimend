import streamlit as st
import time
import requests
import json
from bs4 import BeautifulSoup
css_file = open("style.css", "r")
css_text = css_file.read()
st.markdown(f'<style>{css_text}</style>', unsafe_allow_html=True)



def analyze_sentiment(texts):
    st.write("")
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
    st.success('Analysis Finished')
    
    url = "https://api.apilayer.com/sentiment/analysis"
    payload = texts.encode("utf-8")
    headers = {
        "apikey": "b8Lk9wuGFpbazSoVuRVwOGYrmy9YijlG"
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    result = response.text
    
    try:
        response_data = json.loads(result)
        sentiment = response_data.get("sentiment")  # Use .get() to handle missing key gracefully
        if sentiment == "neutral":
            st.warning("Your content has a neutral sentiment")
        elif sentiment == "positive":
            st.success("Your content has a positive sentiment")
        else:
            st.error("Your content has a negative sentiment")
    except json.JSONDecodeError:
        st.error("Error decoding API response")



def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    texts = soup.get_text(separator=' ')
    analyze_sentiment(texts)




st.title("Sentimind")

txt = st.text_area(label="Enter you input")
type = st.radio("Classify your Input👇",["Text","URL"])
col1,col2,col3 = st.columns(3)
with col1:
 st.write("")
with col2:
    if (st.button("Analyse the sentiment")):
      if txt == "":
            st.error("The input cannot be empty")
      elif type == "URL":
            scraped_data = scrape_website(txt)
      else:
            analyze_sentiment(txt)  
with col2:
   st.write("")




