import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your Name :")

if name:
    st.write(f"Hello, {name}")

age = st.slider("Select your age :", 0, 100,25)
st.write(f"Your age is {age}")

data = {
    "Name": ["charan", "manoj", "harsha", "hemath", "shekhar"],
    "Age": [23, 23, 22, 23, 23],
    "City": ["Bangalore", "Bangalore", "Bangalore", "Bangalore", "hyderabad"]
}

df = pd.DataFrame(data)
st.write(df)


upload = st.file_uploader("Choose your file", type="csv")

if upload is not None:
    uploaded_df = pd.read_csv(upload)
    st.write("Uploaded Data:")
    st.write(uploaded_df)
