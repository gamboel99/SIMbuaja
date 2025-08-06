import streamlit as st
from spk_generator import SPKGenerator

st.title("📄 Generator SPK BUMDes BUWANA RAHARJA")

with st.form("spk_form"):
    nama_kegiatan = st.text_input("Nama Kegiatan")
    tanggal_mulai = st.date_input("Tanggal Mulai")
    tanggal_selesai = st.date_input("Tanggal Selesai")
    lokasi = st.text_input("Lokasi Kegiatan")
    penerima_tugas = st.text_input("Nama Penerima Tugas")
    uraian_tugas = st.text_area("Uraian Tugas")

    submitted = st.form_submit_button("🔐 Generate SPK")

if submitted:
    generator = SPKGenerator(
        nama_kegiatan,
        tanggal_mulai.strftime("%d-%m-%Y"),
        tanggal_selesai.strftime("%d-%m-%Y"),
        lokasi,
        penerima_tugas,
        uraian_tugas
    )
    pdf_file = generator.generate_pdf()

    st.success("✅ SPK berhasil dibuat!")
    st.download_button(
        label="📥 Download SPK (PDF)",
        data=pdf_file,
        file_name=f"SPK_{penerima_tugas.replace(' ', '_')}.pdf",
        mime="application/pdf"
    )
