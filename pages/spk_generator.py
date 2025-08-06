import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
import python-barcode
from barcode.writer import ImageWriter
from PIL import Image
import os
from datetime import datetime
import io

def generate_barcode(spk_number):
    ean = barcode.get('code128', spk_number, writer=ImageWriter())
    filename = f"barcode_{spk_number}"
    fullname = ean.save(filename)
    return fullname

def generate_spk_pdf(spk_number, kegiatan, nama_penerima, jabatan_penerima):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Header
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width/2, height - 2*cm, "SURAT PERINTAH KERJA (SPK)")
    c.setFont("Helvetica", 12)
    c.drawCentredString(width/2, height - 2.7*cm, "BUMDes BUWANA Raharja")

    # Nomor SPK
    c.setFont("Helvetica", 11)
    c.drawString(2.5*cm, height - 4*cm, f"Nomor SPK: {spk_number}")
    c.drawString(2.5*cm, height - 5*cm, f"Tanggal: {datetime.now().strftime('%d-%m-%Y')}")

    # Isi
    c.drawString(2.5*cm, height - 6.5*cm, "Dengan ini memerintahkan kepada:")

    c.setFont("Helvetica-Bold", 11)
    c.drawString(3.5*cm, height - 7.5*cm, f"Nama      : {nama_penerima}")
    c.drawString(3.5*cm, height - 8.2*cm, f"Jabatan   : {jabatan_penerima}")

    c.setFont("Helvetica", 11)
    c.drawString(2.5*cm, height - 9.5*cm, "Untuk melaksanakan kegiatan:")
    c.setFont("Helvetica-Bold", 11)
    textobject = c.beginText(3*cm, height - 10.5*cm)
    for line in kegiatan.split('\n'):
        textobject.textLine(f"- {line}")
    c.drawText(textobject)

    # Mengetahui dan tanda tangan
    c.setFont("Helvetica", 11)
    c.drawString(2.5*cm, 6.5*cm, "Mengetahui,")
    c.drawString(2.5*cm, 5.9*cm, "Direktur BUMDes")
    c.drawString(2.5*cm, 4.8*cm, "(___________________)")

    c.drawString(11.5*cm, 6.5*cm, "Pemberi Perintah,")
    c.drawString(11.5*cm, 5.9*cm, "Nama:")
    c.drawString(11.5*cm, 5.3*cm, "Jabatan:")
    c.drawString(11.5*cm, 4.3*cm, "(___________________)")

    # Barcode
    barcode_path = generate_barcode(spk_number)
    c.drawImage(barcode_path, width - 6*cm, 1.5*cm, width=4.5*cm, preserveAspectRatio=True)

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer

def run():
    st.title("📄 Generator SPK BUMDes BUWANA Raharja")

    with st.form("spk_form"):
        spk_number = st.text_input("Nomor SPK", value=f"SPK-{datetime.now().strftime('%Y%m%d%H%M%S')}")
        nama_penerima = st.text_input("Nama Penerima Perintah")
        jabatan_penerima = st.text_input("Jabatan Penerima")
        kegiatan = st.text_area("Rincian Kegiatan", height=150)
        submitted = st.form_submit_button("📝 Generate SPK")

    if submitted:
        pdf_buffer = generate_spk_pdf(spk_number, kegiatan, nama_penerima, jabatan_penerima)
        st.success("✅ SPK berhasil dibuat!")

        st.download_button(
            label="⬇️ Unduh SPK PDF",
            data=pdf_buffer,
            file_name=f"{spk_number}.pdf",
            mime="application/pdf"
        )

        # Hapus barcode sementara
        try:
            os.remove(f"barcode_{spk_number}.png")
        except:
            pass
