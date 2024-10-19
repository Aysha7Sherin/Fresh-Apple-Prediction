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
    st.subheader('How it works?')
with st.container():
    st.write('-----')
    left_column,right_column=st.columns(2)
    with left_column:
        st.write('##')
        st.write("By training a Deep Learning model using images of fresh apples and rotten apples we can predict from a new picture of apple is rotten or not."
                 "Link to source code of the project is available below. ")
        st.write(
            "[Code to Kaggle Notebook🔍](https://www.kaggle.com/code/ayshasherin7/fresh-or-rotten/edit)")
    with right_column:
        st_lottie(lottie_coding,height=350,key='coding')