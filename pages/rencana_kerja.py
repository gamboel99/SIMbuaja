import streamlit as st
import pandas as pd
import os
from datetime import date

st.set_page_config(page_title="Form Rencana Kerja", layout="wide")
st.title("📋 Form Rencana Kerja BUMDes Buwana Raharja")

# ======= Helper Dropdown =======
jabatan_list = ["Direktur Utama", "Sekretaris", "Bendahara"]
jenis_kegiatan = ["Harian", "Mingguan", "Bulanan", "Tahunan"]

tujuan_berbasis_jabatan = {
    "Direktur Utama": [
        "Sinkronisasi dengan Sekretaris",
        "Penguatan Laporan Keuangan Bendahara",
        "Monitoring Program Strategis"
    ],
    "Sekretaris": [
        "Dukungan Administratif untuk Direktur",
        "Dokumentasi Kegiatan Bendahara",
        "Laporan Korespondensi"
    ],
    "Bendahara": [
        "Validasi Dana Kegiatan Sekretaris",
        "Penganggaran Program Direktur",
        "Pencatatan Arus Kas"
    ]
}

indikator_default = [
    "Kegiatan Terlaksana",
    "Dokumen Tersusun",
    "Laporan Disampaikan",
    "Output Tercapai",
    "Anggaran Digunakan Efisien"
]

# ====== Form Input ======
with st.form("form_rencana_kerja"):
    col1, col2 = st.columns(2)

    with col1:
        jabatan = st.selectbox("👤 Jabatan", jabatan_list)
        jenis = st.selectbox("📆 Jenis Kegiatan", jenis_kegiatan)
        tanggal_mulai = st.date_input("🗓️ Tanggal Mulai", value=date.today())
    with col2:
        tujuan = st.selectbox("🎯 Tujuan Kegiatan", tujuan_berbasis_jabatan.get(jabatan, []))
        indikator = st.selectbox("✅ Indikator Keberhasilan", indikator_default)
        tanggal_selesai = st.date_input("🗓️ Tanggal Selesai", value=date.today())

    rencana = st.text_area("📝 Rencana Kegiatan (Opsional)", placeholder="Contoh: Menyusun draft rencana kerja mingguan...")
    output = st.text_area("📌 Output yang Diharapkan", placeholder="Contoh: Draft dokumen rencana kerja minggu ke-2...")

    submitted = st.form_submit_button("💾 Simpan Rencana Kerja")

# ====== Simpan Data ======
if submitted:
    if tanggal_mulai > tanggal_selesai:
        st.error("❌ Tanggal mulai tidak boleh melebihi tanggal selesai!")
    else:
        data = {
            "Jabatan": jabatan,
            "Jenis": jenis,
            "Tujuan": tujuan,
            "Rencana": rencana,
            "Indikator": indikator,
            "Output": output,
            "Tanggal Mulai": tanggal_mulai.strftime("%Y-%m-%d"),
            "Tanggal Selesai": tanggal_selesai.strftime("%Y-%m-%d"),
            "Status": "Belum Dilaksanakan"
        }

        df_new = pd.DataFrame([data])
        folder_path = "data/rencana_kerja"
        os.makedirs(folder_path, exist_ok=True)
        file_path = f"{folder_path}/{jabatan.lower().replace(' ', '_')}.csv"

        if os.path.exists(file_path):
            df_existing = pd.read_csv(file_path)
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        else:
            df_combined = df_new

        df_combined.to_csv(file_path, index=False)
        st.success(f"✅ Rencana kerja untuk {jabatan} berhasil disimpan!")

