import streamlit as st
import pandas as pd

st.title("📊 Tabel Rencana Kerja")

jabatan = st.selectbox("Pilih Jabatan", ["Direktur Utama", "Sekretaris", "Bendahara"])

filename = f"data/rencana_kerja/{jabatan.lower().replace(' ', '_')}.csv"

try:
    df = pd.read_csv(filename)
    st.dataframe(df)
except FileNotFoundError:
    st.warning("Belum ada rencana kerja untuk jabatan ini.")
