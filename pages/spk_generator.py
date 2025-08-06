import streamlit as st
import pandas as pd
from datetime import date

st.title("📄 Penerbitan SPK dari Rencana Kerja")

jabatan = st.selectbox("Pilih Jabatan", ["Direktur Utama", "Sekretaris", "Bendahara"])
filename = f"data/rencana_kerja/{jabatan.lower().replace(' ', '_')}.csv"

try:
    df = pd.read_csv(filename)
    harian = df[df['Frekuensi'] == 'Harian']
    pilihan = st.selectbox("Pilih Kegiatan Harian", harian['Tujuan'].tolist())

    if st.button("📥 Terbitkan SPK"):
        st.success(f"✅ SPK untuk kegiatan: '{pilihan}' berhasil diterbitkan!")
        st.info("📎 Fitur cetak/download SPK dalam format PDF bisa ditambahkan di tahap selanjutnya.")

except FileNotFoundError:
    st.warning("Belum ada data harian untuk jabatan ini.")

