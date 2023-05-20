import streamlit as st
import time
import requests
import json
css_file = open("style.css", "r")
css_text = css_file.read()
st.markdown(f'<style>{css_text}</style>', unsafe_allow_html=True)



def analyze_sentiment():
   st.write("")
   my_bar = st.progress(0)
   for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)
   st.success('Analysis Finished', icon="✅")
   url = "https://api.apilayer.com/sentiment/analysis"
   payload = "{body}".encode("utf-8")
   headers= {
   "apikey": "b8Lk9wuGFpbazSoVuRVwOGYrmy9YijlG"
   }
   response = requests.request("POST", url, headers=headers, data = payload)
   result = response.text
   response_data = json.loads(result)
   sentiment = response_data["sentiment"]
   if(sentiment == "neutral"):
      st.warning("Your content has a neutral sentiment")
   elif(sentiment == "postive"):
      st.success("Your content has a postive sentiment")
   else:
      st.error("Your content has a negative sentiment")


st.title("Sentimind")

txt = st.text_area(label="Enter you text")
col1,col2,col3 = st.columns(3)
with col1:
 st.write("")
with col2:
    if (st.button("Analyse the sentiment of a text")):
       if txt == "":
         st.error("The input cannot be empty")
       else:
          analyze_sentiment()    
with col2:
   st.write("")




