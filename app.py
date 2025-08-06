
import streamlit as st
from login import login_form

st.set_page_config(page_title="SIM BUMDes PRO", layout="wide")
st.title("🧮 Sistem Informasi Manajemen BUMDes Buwana Raharja")

role = login_form()

if role == "admin":
    st.success("Login sebagai ADMIN")
    st.markdown("Silakan pilih menu di sidebar untuk mengakses semua fitur.")
elif role == "operator":
    st.warning("Login sebagai OPERATOR")
    st.markdown("Akses terbatas untuk input data unit usaha.")
else:
    st.info("Silakan login untuk melanjutkan.")
