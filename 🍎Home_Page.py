import streamlit as st
from streamlit_lottie import st_lottie
import requests
st.set_page_config(page_title='Fresh Apple',page_icon='🍎',layout='wide')

def lottie_url(url):
    r= requests.get(url)
    if r.status_code!=200:
        return  None
    return r.json()

lottie_coding=lottie_url('https://lottie.host/b8b678d0-4d3a-4505-9684-dad04e5a1ccd/z2IpFFU12T.json')

with st.container():
    st.subheader('👋 Welcome to')
    st.header('Apple Freshness Prediction App')
    st.write("# Let's check if your apple is Fresh or Rotten?🤔 ")
with st.container():
    st.write('-----')
    left_column,right_column=st.columns(2)
    with left_column:
        st_lottie(lottie_coding, height=350, key='coding')
    with right_column:
        st.write('##')
        st.write('Upload a picture of apple and see whether it is rotten or fresh.')
        st. write('Other applications of this prediction:')
        st.write('1. Automating Quality Control in Food Industry')
        st.write('2. Retail Industry (Supermarkets, Grocery Stores)')
        st.write('3. Smart Packaging Solutions')
        st.write('4. Food Waste Reduction')
        st.write('5. Smart Fridges or Automated Vending Machines')
