# pages/rencana_kerja.py

import streamlit as st
import pandas as pd
from datetime import datetime

st.title("📋 Rencana Kerja Manajemen BUMDes")
    "jabatan": "Direktur Utama",  # atau Sekretaris / Bendahara
    "tingkat": "Harian",  # atau Mingguan, Bulanan, Tahunan
    "tanggal": "2025-08-07",
    "nama_kegiatan": "Koordinasi rutin dengan sekretaris",
    "tujuan": "Sinkronisasi data SPK dan laporan keuangan",  # dropdown terkait jabatan lain
    "indikator_keberhasilan": "Tersusun notulen dan laporan ringkas",  # pilihan + custom
    "output": "Notulen rapat",  # isian opsional
    "catatan": "Dilakukan via Zoom karena Direktur di luar kota",
    "status": "Belum Dilaksanakan"  # bisa diganti jadi dropdown update

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
