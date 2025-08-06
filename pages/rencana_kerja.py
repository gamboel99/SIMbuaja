# pages/rencana_kerja.py

import streamlit as st
import pandas as pd
from datetime import datetime

st.title("📋 Rencana Kerja Manajemen BUMDes")

jabatan = st.selectbox("Pilih Jabatan", ["Direktur Utama", "Sekretaris", "Bendahara"])
periode = st.selectbox("Pilih Periode", ["Harian", "Mingguan", "Bulanan", "Tahunan"])
tanggal = st.date_input("Tanggal Rencana", value=datetime.today())
kegiatan = st.text_input("Kegiatan")
tujuan = st.text_area("Tujuan Kegiatan (kaitkan dengan jabatan lain)")
indikator = st.text_area("Indikator Keberhasilan")

if st.button("Simpan Rencana Kerja"):
    new_data = {
        "Tanggal": tanggal,
        "Jabatan": jabatan,
        "Periode": periode,
        "Kegiatan": kegiatan,
        "Tujuan": tujuan,
        "Indikator": indikator,
    }
    df = pd.DataFrame([new_data])
    try:
        df.to_csv("data/rencana_kerja.csv", mode="a", header=False, index=False)
        st.success("✅ Rencana kerja berhasil disimpan!")
    except Exception as e:
        st.error(f"❌ Gagal menyimpan: {e}")

# Tampilkan semua rencana kerja
st.subheader("📄 Daftar Rencana Kerja Tersimpan")
try:
    rencana_df = pd.read_csv("data/rencana_kerja.csv")
    st.dataframe(rencana_df)
except:
    st.info("Belum ada rencana kerja yang tersimpan.")
