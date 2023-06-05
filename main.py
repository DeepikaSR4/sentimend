import streamlit as st
import time
import requests
import json
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import string
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('stopwords')

css_file = open("style.css", "r")
css_text = css_file.read()
st.markdown(f'<style>{css_text}</style>', unsafe_allow_html=True)

def preprocess_text(texts):
    texts = ''.join([char for char in texts if char not in string.punctuation])
    texts = texts.lower()
    words = nltk.word_tokenize(texts)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    processed_text = ' '.join(words)
    return processed_text

def get_sentiment_color(sentiment_score):
    if sentiment_score > 0:
        return 'green'
    elif sentiment_score < 0:
        return 'red'
    else:
        return 'yellow'

def analyze_sentiment(texts):
    st.write("")
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
    st.success('Analysis Finished')

    processed_text = preprocess_text(texts)

    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(processed_text)
    overall_sentiment = sentiment_scores["compound"]

    st.subheader("Overall Sentiment")
    if overall_sentiment >= 0.05:
        st.success("Positive")
    elif overall_sentiment <= -0.05:
        st.error("Negative")
    else:
        st.warning("Neutral")

    words = processed_text.split()
    word_sentiments = []
    colors = []
    word_labels = []
    
    threshold = 50
    count = 0
    
    for word in words:
        word_sentiment = sid.polarity_scores(word)["compound"]
        if word_sentiment != 0 and count < threshold:
            word_sentiments.append(word_sentiment)
            colors.append(get_sentiment_color(word_sentiment))
            word_labels.append(word)
            count += 1

    plt.figure(figsize=(12, 6))
    plt.bar(range(len(word_labels)), word_sentiments, color=colors)
    plt.xticks(range(len(word_labels)), word_labels, rotation=90)
    plt.xlabel("Words")
    plt.ylabel("Sentiment Score")
    plt.title("Word-level Sentiments")
    st.pyplot(plt)

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    texts = soup.get_text(separator=' ')
    analyze_sentiment(texts)

st.title("Sentimind")

txt = st.text_area(label="Enter your input")
type = st.radio("Classify your Input👇", ["Text", "URL"])
col1, col2, col3 = st.columns(3)

with col1:
    st.write("")

with col2:
    if st.button("Analyze the sentiment"):
        if txt == "":
            st.error("The input cannot be empty")
        elif type == "URL":
            scraped_data = scrape_website(txt)
        else:
            analyze_sentiment(txt)

with col2:
    st.write("")
