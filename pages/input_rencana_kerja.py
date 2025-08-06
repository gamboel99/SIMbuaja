import streamlit as st
import pandas as pd
from datetime import date

st.title("📝 Form Rencana Kerja")

jabatan = st.selectbox("Pilih Jabatan", ["Direktur Utama", "Sekretaris", "Bendahara"])
frekuensi = st.radio("Frekuensi Kegiatan", ["Harian", "Mingguan", "Bulanan", "Tahunan"])
tanggal = st.date_input("Tanggal Pelaksanaan", date.today())
tujuan = st.text_area("Tujuan Kegiatan", placeholder="Jelaskan tujuan kegiatan")
keterkaitan = st.multiselect("Terkait dengan Jabatan Lain", ["Direktur Utama", "Sekretaris", "Bendahara"])
indikator = st.selectbox("Indikator Keberhasilan", [
    "Terlaksananya kegiatan tepat waktu",
    "Dokumen/SPK diterbitkan",
    "Adanya laporan hasil",
    "Peningkatan efisiensi kerja"
])
status = "Direncanakan"

if st.button("💾 Simpan Rencana Kerja"):
    data = {
        "Tanggal": [tanggal],
        "Frekuensi": [frekuensi],
        "Tujuan": [tujuan],
        "Terkait Dengan": [", ".join(keterkaitan)],
        "Indikator": [indikator],
        "Status": [status]
    }

    df = pd.DataFrame(data)
    filename = f"data/rencana_kerja/{jabatan.lower().replace(' ', '_')}.csv"
    try:
        existing = pd.read_csv(filename)
        df = pd.concat([existing, df], ignore_index=True)
    except:
        pass
    df.to_csv(filename, index=False)
    st.success("✅ Rencana kerja berhasil disimpan!")
