import streamlit as st

def login():
    st.title("Login Admin/Operator BUMDes")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.session_state['authenticated'] = True
            st.success("Login berhasil")
        else:
            st.error("Username atau password salah")
