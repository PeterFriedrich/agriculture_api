"""
This streamlit thing is purely a front end, 
"""
import streamlit as st
import json
import requests

st.title("Basic Calculator App")

# taking operation inputs
option = st.selectbox("What operation you want to perform?",
                      ("Addition", "Subtraction", "Multiplication", "Division"))

# drawing sliders, taking number inputs
st.write("")
st.write("Select the numbers from slider below")
x = st.slider("X", 0, 100, 20)
y = st.slider("Y", 0, 130, 10)

# converting the inputs into a json format
inputs = {"operation": option, "x": x, "y": y}

# when the user clicks on button it will fetch the API
# IMPORTANT something like this saves compute
if st.button("Calculate"):
    # json.dumps converts the inputs dictionary to json
    res = requests.post(url = "http://127.0.0.1:8000/calculate", data = json.dumps(inputs))

    st.subheader(f"Response from API = {res.text}")

st.write("**Actual json:**\n\n", json.dumps(inputs))

