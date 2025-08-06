import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.title("📋 Rencana Kerja Terpadu BUMDes")

st.info("Silakan input rencana kerja sesuai posisi Anda dan pastikan semua rencana saling mendukung.")

# File penyimpanan
DATA_PATH = "data/rencana_kerja.csv"
if not os.path.exists("data"):
    os.makedirs("data")

# Posisi
roles = ["Direktur Utama", "Sekretaris", "Bendahara"]
jenis_rencana = ["Harian", "Mingguan", "Bulanan", "Tahunan"]

# Form Input
with st.form("rencana_form"):
    tanggal = st.date_input("Tanggal Rencana")
    posisi = st.selectbox("Posisi", roles)
    jenis = st.selectbox("Jenis Rencana", jenis_rencana)
    uraian = st.text_area("Uraian Rencana Kerja", placeholder="Contoh: Menyusun draft SPK pembelian alat...")
    terkait_dengan = st.text_input("Terkait dengan rencana (dari posisi lain)", placeholder="Contoh: Evaluasi laporan mingguan Bendahara")

    submitted = st.form_submit_button("Simpan")

    if submitted:
        new_data = pd.DataFrame([{
            "timestamp": datetime.now().isoformat(),
            "tanggal": tanggal,
            "posisi": posisi,
            "jenis": jenis,
            "uraian": uraian,
            "terkait_dengan": terkait_dengan
        }])

        if os.path.exists(DATA_PATH):
            existing = pd.read_csv(DATA_PATH)
            df = pd.concat([existing, new_data], ignore_index=True)
        else:
            df = new_data

        df.to_csv(DATA_PATH, index=False)
        st.success("✅ Rencana kerja berhasil disimpan!")

# Tampilkan Data
st.subheader("📊 Daftar Rencana Kerja")
if os.path.exists(DATA_PATH):
    data = pd.read_csv(DATA_PATH)
    st.dataframe(data.sort_values(by="tanggal", ascending=False), use_container_width=True)
else:
    st.warning("Belum ada rencana kerja yang disimpan.")
