import streamlit as st
from time import sleep


st.set_page_config(
    page_title="Prostate cancer Aid",
    page_icon="🧊",
    layout="centered",
)

st.sidebar.success("Select a page below for guidelines")

import streamlit as st

def login():

    # Define username and password
    username = "admin"
    password = "patient"

    # Create login form
    st.title("Login")
    with st.form("login_form"):
        input_username = st.text_input("Username")
        input_password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")

    # Authenticate user
    if submit_button:
        if input_username == username and input_password == password:
            st.session_state["logged_in"]=True
            st.success("Logged in successfully!")
            sleep(0.5)
            st.switch_page("pages/4_🧬_dashboard.py")
        else:
            st.error("Invalid username or password")

if "logged_in" not in st.session_state:
    login()
else:
    login()

