import streamlit as st
from fpdf import FPDF
import qrcode
from io import BytesIO

class SPKGenerator:
    def __init__(self, nama_kegiatan, tanggal_mulai, tanggal_selesai, lokasi, penerima_tugas, uraian_tugas):
        self.nama_kegiatan = nama_kegiatan
        self.tanggal_mulai = tanggal_mulai
        self.tanggal_selesai = tanggal_selesai
        self.lokasi = lokasi
        self.penerima_tugas = penerima_tugas
        self.uraian_tugas = uraian_tugas

    def generate_qr(self, text):
        qr = qrcode.QRCode(box_size=2, border=1)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buf = BytesIO()
        img.save(buf)
        return buf

    def generate_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 14)

        # Header
        pdf.cell(0, 10, "BADAN USAHA MILIK DESA (BUMDes)", ln=True, align="C")
        pdf.cell(0, 10, "BUWANA RAHARJA", ln=True, align="C")
        pdf.set_font("Arial", "", 10)
        pdf.cell(0, 10, "Alamat: Jl. Raya Keling, Bukaan, Keling, Kec. Kepung, Kabupaten Kediri, Jawa Timur 64293", ln=True, align="C")
        pdf.ln(10)

        # Judul
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "SURAT PERINTAH KERJA (SPK)", ln=True, align="C")
        pdf.ln(5)

        # Isi
        pdf.set_font("Arial", "", 11)
        pdf.multi_cell(0, 8, f"Dengan ini memberikan perintah kepada:\n\nNama\t\t\t: {self.penerima_tugas}\n\n"
                             f"Untuk melaksanakan kegiatan:\n\nJudul Kegiatan\t: {self.nama_kegiatan}\n"
                             f"Lokasi\t\t\t: {self.lokasi}\n"
                             f"Tanggal Mulai\t: {self.tanggal_mulai}\n"
                             f"Tanggal Selesai\t: {self.tanggal_selesai}\n\n"
                             f"Uraian Tugas:\n{self.uraian_tugas}\n")

        pdf.ln(5)

        # QR Code
        qr_buf = self.generate_qr(f"{self.nama_kegiatan} - {self.penerima_tugas}")
        pdf.image(qr_buf, x=165, y=pdf.get_y(), w=30)

        pdf.ln(35)

        # Tanda Tangan
        pdf.cell(0, 8, "Mengetahui,", ln=True)
        pdf.cell(0, 8, "Direktur BUMDes BUWANA RAHARJA", ln=True)
        pdf.ln(20)
        pdf.cell(0, 8, "____________________________", ln=True)

        pdf.ln(15)
        pdf.cell(0, 8, "Pemberi Perintah,", ln=True)
        pdf.cell(0, 8, "Nama: ______________________", ln=True)
        pdf.cell(0, 8, "Jabatan: ____________________", ln=True)

        # Output PDF
        output = BytesIO()
        pdf.output(output)
        return output
