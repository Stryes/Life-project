import streamlit as st 
import pandas as pd
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRmqinK_tqx6_ILzYYKrlGZY3oN3cRThvBCkJlLadYCXnHIIO6sQh-eulslnyXqG0JRDSUxglK6guZe/pub?output=csv')
st.dataframe(voc)
