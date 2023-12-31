"""
This streamlit thing is purely a front end, you need to
run this using streamlit run, separately from the
uvicorn fastapi server.
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
operation_dict = {"Addition":"+", "Subtraction":"-", "Multiplication":"*", "Division":"/"}

# when the user clicks on button it will fetch the API
# IMPORTANT something like this saves compute
if st.button("Calculate"):
    # json.dumps converts the inputs dictionary to json
    res = requests.post(url = "http://fastapi:8000/calculate", data = json.dumps(inputs))
    st.subheader(f"{x} {operation_dict[option]} {y} = {res.text}")

    st.subheader(f"Response from API = {res.text}")

st.write("**Actual json:**\n\n", json.dumps(inputs))

