import streamlit as st
from time import sleep

st.sidebar.success("Select a page")

st.header("Thank you you can logout")
def log_out():
    st.session_state["logged_in"] = False
    st.success("Logged out!")
    sleep(0.5)

   
if st.button("Logout"):
    log_out()  
    st.switch_page("1_🩺_aid.py")


