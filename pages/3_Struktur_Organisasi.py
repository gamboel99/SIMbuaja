import streamlit as st
import pandas as pd
import os

file_path = "data/struktur.csv"

st.title("Struktur Organisasi")

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    st.dataframe(df)
else:
    st.warning("Struktur organisasi belum tersedia.")
