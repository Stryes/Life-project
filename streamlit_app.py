import streamlit as st 
import pandas as pd
voc=pd.read_csv('lien')
st.dataframe(voc)
