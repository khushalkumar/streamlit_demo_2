import streamlit as st
st.title("Welcome to streamlit")

agree = st.checkbox('Display Widget')

if agree:
    st.write('Showing the Widget')


status = st.radio(
    "What's your Gender",
    ["male", "Female"],
)

if (status == "male"):
    st.success("Male")
else:
    st.success("Female")