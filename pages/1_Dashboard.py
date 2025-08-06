import streamlit as st
import pandas as pd
import os

st.title("Dashboard BUMDes")

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Unit Usaha", 13)
with col2:
    st.metric("Pengaduan Masuk", 2)

st.subheader("Grafik Placeholder (Akan dikembangkan)")
st.info("Grafik perkembangan keuangan dan kegiatan akan ditampilkan di sini.")
