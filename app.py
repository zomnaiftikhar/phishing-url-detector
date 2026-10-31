import streamlit as st
from predict import predict

st.title("Phishing URL Detector")
url = st.text_input("Enter a URL")
if st.button("Check") and url:
    r = predict(url)
    st.write("Prediction:", r["label"])
    st.write("Phishing probability:", r["phishing_probability"])