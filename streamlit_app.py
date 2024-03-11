import streamlit as st 
input="lapin"
list_possibilies=["rabbit","raco","vorpal","bun"]
correct_answer="rabbit"
st.write("comment dit on ? "+ input+ "en anglais")
for i in range(len(list_possibilities)):
  st.but (list_possibilities[i])
