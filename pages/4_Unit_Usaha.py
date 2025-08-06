import streamlit as st
import pandas as pd
import os

file_path = "data/unit_usaha.csv"

st.title("Manajemen Unit Usaha")

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    st.dataframe(df)

st.subheader("Tambah Unit Usaha")
with st.form("form_usaha"):
    nama = st.text_input("Nama Unit Usaha")
    jenis = st.selectbox("Jenis", ["Perdagangan", "Jasa", "Pertanian", "Digital", "Lainnya"])
    if st.form_submit_button("Simpan"):
        new = pd.DataFrame([[nama, jenis]], columns=["Nama", "Jenis"])
        df = pd.concat([df, new], ignore_index=True) if os.path.exists(file_path) else new
        df.to_csv(file_path, index=False)
        st.success("Unit usaha ditambahkan.")
