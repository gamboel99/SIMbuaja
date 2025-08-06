import streamlit as st
import pandas as pd
import os

file_path = "data/dokumentasi.csv"

st.title("Dokumentasi Kegiatan BUMDes")

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    st.dataframe(df)
else:
    st.warning("Belum ada dokumentasi kegiatan.")
