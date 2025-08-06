import streamlit as st
from fpdf import FPDF
from io import BytesIO
from datetime import date

class SPKGenerator:
    def __init__(self, kegiatan, tgl_mulai, tgl_selesai, lokasi, penerima, uraian):
        self.kegiatan = kegiatan
        self.tgl_mulai = tgl_mulai
        self.tgl_selesai = tgl_selesai
        self.lokasi = lokasi
        self.penerima = penerima
        self.uraian = uraian

    def generate_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "SURAT PERINTAH KERJA (SPK)", ln=True, align="C")
        pdf.ln(5)

        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 8, f"""Yang bertanda tangan di bawah ini:

Nama          : ....................................................
Jabatan       : ....................................................

Dengan ini memberikan tugas kepada:

Nama          : {self.penerima}
Kegiatan      : {self.kegiatan}
Tanggal       : {self.tgl_mulai} s.d. {self.tgl_selesai}
Lokasi        : {self.lokasi}

Uraian Tugas:
{self.uraian}

Demikian surat perintah kerja ini dibuat untuk dilaksanakan dengan penuh tanggung jawab.
""")

        pdf.ln(10)
        pdf.set_font("Arial", '', 12)
        today = date.today().strftime("%d %B %Y")
        pdf.cell(0, 8, f"Kediri, {today}", ln=True, align='R')

        pdf.cell(0, 8, "Mengetahui,", ln=True)
        pdf.cell(0, 8, "Direktur BUMDes BUWANA RAHARJA", ln=True)
        pdf.ln(20)
        pdf.cell(0, 8, "(_______________________)", ln=True)

        buffer = BytesIO()
        pdf.output(buffer)
        buffer.seek(0)
        return buffer

# STREAMLIT UI
st.set_page_config(page_title="Generator SPK - BUWANA RAHARJA")
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
    if not all([nama_kegiatan, lokasi, penerima_tugas, uraian_tugas]):
        st.warning("⚠️ Semua kolom harus diisi.")
    else:
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
