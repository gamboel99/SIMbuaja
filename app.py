
import streamlit as st
from login import login_form
import streamlit as st

st.set_page_config(page_title="Rencana Kerja BUMDes", layout="wide")
st.title("📚 Sistem Rencana Kerja BUMDes Buwana Raharja")

st.markdown("""
Selamat datang di sistem manajemen rencana kerja dan evaluasi kinerja.
Silakan gunakan menu di sebelah kiri untuk:
- Mengisi rencana kerja per jabatan
- Melihat tabel rencana
- Menerbitkan SPK
- Mengevaluasi capaian kinerja

💡 Sistem ini terintegrasi antar jabatan dan mendukung pemantauan berkelanjutan.
""")

st.set_page_config(page_title="SIM BUMDes PRO", layout="wide")
st.title("🧮 Sistem Informasi Manajemen BUMDes Buwana Raharja")

role = login_form()

if role == "admin":
    st.success("Login sebagai ADMIN")
    st.markdown("Silakan pilih menu di sidebar untuk mengakses semua fitur.")
elif role == "operator":
    st.warning("Login sebagai OPERATOR")
    st.markdown("Akses terbatas untuk input data unit usaha.")
else:
    st.info("Silakan login untuk melanjutkan.")

import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="SIM BUMDes Buwana Raharja", layout="wide")

with st.sidebar:
    selected = option_menu("Menu", [
        "Beranda",
        "Monitoring Usaha",
        "Laporan Tahunan",
        "Rencana Kerja",  # <== Tambahkan ini
    ])

if selected == "Beranda":
    st.title("Selamat Datang di SIM BUMDes Buwana Raharja")

elif selected == "Monitoring Usaha":
    from pages import monitoring_usaha
    monitoring_usaha.run()

elif selected == "Laporan Tahunan":
    from pages import laporan_tahunan
    laporan_tahunan.run()

elif selected == "Rencana Kerja":
    from pages import rencana_kerja
    rencana_kerja.run()
