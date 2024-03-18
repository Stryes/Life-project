import streamlit as st 
import pandas as pd
import numpy as np
voc=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRmqinK_tqx6_ILzYYKrlGZY3oN3cRThvBCkJlLadYCXnHIIO6sQh-eulslnyXqG0JRDSUxglK6guZe/pub?output=csv')
st.dataframe(voc)
l=voc.shape[o]
i= np.random:choice(range(l))
word_fr=voc['Definiton'].values[i]
st.write(world_frt+"  "+word_chi)
