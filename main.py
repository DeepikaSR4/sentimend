import streamlit as st
import time
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


st.title("Sentimind")

txt = st.text_area(label="Enter you text")
col1,col2,col3 = st.columns(3)
with col1:
 st.write("")
with col2:
    if (st.button("Analyse the sentiment of a text")):
       analyze_sentiment()    
with col2:
   st.write("")




