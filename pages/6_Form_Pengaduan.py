import streamlit as st
import pandas as pd
import os

file_path = "data/pengaduan.csv"

st.title("Form Pengaduan Masyarakat")

with st.form("form_pengaduan"):
    nama = st.text_input("Nama")
    isi = st.text_area("Isi Pengaduan")
    if st.form_submit_button("Kirim"):
        new = pd.DataFrame([[nama, isi]], columns=["Nama", "Pengaduan"])
        df = pd.read_csv(file_path) if os.path.exists(file_path) else pd.DataFrame(columns=["Nama", "Pengaduan"])
        df = pd.concat([df, new], ignore_index=True)
        df.to_csv(file_path, index=False)
        st.success("Pengaduan dikirim.")

if os.path.exists(file_path):
    st.subheader("Daftar Pengaduan")
    df = pd.read_csv(file_path)
    st.dataframe(df)
