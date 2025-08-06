
import streamlit as st

def login_form():
    st.sidebar.title("Login Pengguna")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    login_btn = st.sidebar.button("Login")
    if login_btn:
        if username == "admin" and password == "admin123":
            return "admin"
        elif username == "operator" and password == "operator123":
            return "operator"
        else:
            st.sidebar.error("Login gagal")
    return None
