from fpdf import FPDF
from io import BytesIO
from datetime import date

class SPKGenerator:
    def __init__(self, nama_kegiatan, tanggal_mulai, tanggal_selesai, lokasi, penerima_tugas, uraian_tugas):
        self.nama_kegiatan = nama_kegiatan
        self.tanggal_mulai = tanggal_mulai
        self.tanggal_selesai = tanggal_selesai
        self.lokasi = lokasi
        self.penerima_tugas = penerima_tugas
        self.uraian_tugas = uraian_tugas

    def generate_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.set_title("Surat Perintah Kerja")

        # Header
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "SURAT PERINTAH KERJA", ln=True, align="C")
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, "BUMDes BUWANA RAHARJA", ln=True, align="C")
        pdf.ln(10)

        # Isi SPK
        pdf.multi_cell(0, 8, f"Dengan ini memberikan tugas kepada:")
        pdf.multi_cell(0, 8, f"Nama           : {self.penerima_tugas}")
        pdf.multi_cell(0, 8, f"Untuk melaksanakan kegiatan sebagai berikut:")
        pdf.multi_cell(0, 8, f"Nama Kegiatan  : {self.nama_kegiatan}")
        pdf.multi_cell(0, 8, f"Lokasi         : {self.lokasi}")
        pdf.multi_cell(0, 8, f"Durasi         : {self.tanggal_mulai} s.d. {self.tanggal_selesai}")
        pdf.multi_cell(0, 8, f"Uraian Tugas   :\n{self.uraian_tugas}")
        pdf.ln(10)

        # Tanggal
        pdf.multi_cell(0, 8, f"Demikian surat perintah ini dibuat untuk dapat dilaksanakan sebagaimana mestinya.")
        pdf.ln(20)

        # Tanda tangan
        pdf.cell(100, 10, "Mengetahui,", ln=0)
        pdf.cell(0, 10, "Kepala/Pemberi Perintah,", ln=1)
        pdf.cell(100, 10, "Direktur BUMDes", ln=0)
        pdf.cell(0, 10, "(Nama dan Jabatan)", ln=1)

        # Kosongkan tempat tanda tangan
        pdf.ln(20)
        pdf.cell(100, 10, "(............................)", ln=0)
        pdf.cell(0, 10, "(............................)", ln=1)

        # Output sebagai file dalam memori
        pdf_output = BytesIO()
        pdf.output(pdf_output)
        pdf_output.seek(0)
        return pdf_output
