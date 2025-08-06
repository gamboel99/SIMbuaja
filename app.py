import streamlit as st
from auth.login import login

st.set_page_config(page_title="SIM BUMDes Buwana Raharja", layout="wide")

if 'authenticated' not in st.session_state or not st.session_state['authenticated']:
    login()
else:
    st.title("Selamat Datang di SIM BUMDes Buwana Raharja")
    st.write("Gunakan menu di sidebar untuk navigasi modul.")
