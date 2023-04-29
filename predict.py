from input import mechine_learning as a
import streamlit as st
st.header("NB Text Classifier")
input = st.text_area("Enter the text", value="")
l=[]
l.append(input)
if st.button("Predict"):
    vec = a.vector.transform(l).toarray()
    x=(str(list(a.naivebayes.predict(vec))[0]).replace('0', 'TECH').replace('1', 'BUSINESS').replace('2', 'SPORTS').replace('3','ENTERTAINMENT').replace('4','POLITICS'))
    st.write("label:",x)
