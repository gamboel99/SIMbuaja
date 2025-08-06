import streamlit as st
import pandas as pd
import os

file_path = "data/unit_usaha.csv"

st.title("Manajemen Data Unit Usaha")

if os.path.exists(file_path):
    data = pd.read_csv(file_path)
    st.dataframe(data)
else:
    st.warning("Data unit usaha belum tersedia.")

with st.form("Tambah Unit Usaha"):
    nama = st.text_input("Nama Unit Usaha")
    kategori = st.selectbox("Kategori", ["Perdagangan", "Jasa", "Digital", "Pertanian", "Lainnya"])
    if st.form_submit_button("Simpan"):
        new = pd.DataFrame([[nama, kategori]], columns=["Nama", "Kategori"])
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            df = pd.concat([df, new], ignore_index=True)
        else:
            df = new
        df.to_csv(file_path, index=False)
        st.success("Unit usaha berhasil ditambahkan.")
