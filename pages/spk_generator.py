import streamlit as st
import pandas as pd
import qrcode
from fpdf import FPDF
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="Generator SPK", layout="centered")

st.title("📄 Generator Surat Perintah Kerja (SPK)")
st.markdown("Silakan isi data berikut untuk membuat SPK dalam format PDF.")

# Form input data SPK
with st.form("spk_form"):
    nama_pekerjaan = st.text_input("Nama Pekerjaan")
    nomor_spk = st.text_input("Nomor SPK")
    tanggal_spk = st.date_input("Tanggal SPK")
    nama_pelaksana = st.text_input("Nama Pelaksana")
    jabatan_pelaksana = st.text_input("Jabatan Pelaksana")
    uraian_tugas = st.text_area("Uraian Tugas")

    submit = st.form_submit_button("✅ Buat SPK")

if submit:
    # Buat QR Code dari nomor SPK
    qr = qrcode.make(f"SPK: {nomor_spk}")
    qr_bytes = BytesIO()
    qr.save(qr_bytes)
    qr_bytes.seek(0)
    qr_img = Image.open(qr_bytes)

    # Buat file PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="SURAT PERINTAH KERJA", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Nomor: {nomor_spk}", ln=True)
    pdf.cell(200, 10, txt=f"Tanggal: {tanggal_spk.strftime('%d-%m-%Y')}", ln=True)
    pdf.ln(5)
    pdf.multi_cell(0, 10, txt=f"Nama Pekerjaan: {nama_pekerjaan}")
    pdf.multi_cell(0, 10, txt=f"Nama Pelaksana: {nama_pelaksana}")
    pdf.multi_cell(0, 10, txt=f"Jabatan: {jabatan_pelaksana}")
    pdf.multi_cell(0, 10, txt=f"Uraian Tugas:\n{uraian_tugas}")
    pdf.ln(10)
    pdf.cell(0, 10, txt="Tanda tangan pelaksana:", ln=True)
    pdf.ln(20)
    pdf.cell(0, 10, txt=f"( {nama_pelaksana} )", ln=True)

    # Simpan PDF ke memori
    pdf_output = BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    st.success("✅ SPK berhasil dibuat!")
    st.download_button(
        label="📥 Download SPK PDF",
        data=pdf_output,
        file_name=f"SPK_{nomor_spk}.pdf",
        mime="application/pdf"
    )

    # Tampilkan QR Code
    st.image(qr_img, caption="QR Code SPK", width=150)
