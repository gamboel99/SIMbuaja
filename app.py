import streamlit as st
from streamlit_option_menu import option_menu
from login import login_form

# Konfigurasi halaman
st.set_page_config(page_title="SIM BUMDes Buwana Raharja", layout="wide")

# Judul utama
st.title("🧮 Sistem Informasi Manajemen BUMDes Buwana Raharja")

# Autentikasi pengguna
role = login_form()

# Menampilkan informasi login
if role == "admin":
    st.success("Login sebagai ADMIN")
elif role == "operator":
    st.warning("Login sebagai OPERATOR")
else:
    st.info("Silakan login untuk melanjutkan.")
    st.stop()  # Menghentikan eksekusi jika belum login

# Sidebar navigasi
with st.sidebar:
    selected = option_menu("Menu", [
        "Beranda",
        "Monitoring Usaha",
        "Laporan Tahunan",
        "Rencana Kerja",
    ])

# Routing ke masing-masing halaman
if selected == "Beranda":
    st.markdown("""
    ## 📚 Selamat datang di SIM BUMDes Buwana Raharja

    Silakan gunakan menu di sebelah kiri untuk:
    - Mengisi rencana kerja per jabatan
    - Melihat tabel rencana
    - Menerbitkan SPK
    - Mengevaluasi capaian kinerja

    💡 Sistem ini terintegrasi antar jabatan dan mendukung pemantauan berkelanjutan.
    """)

elif selected == "Monitoring Usaha":
    from pages import monitoring_usaha
    monitoring_usaha.run()

elif selected == "Laporan Tahunan":
    from pages import laporan_tahunan
    laporan_tahunan.run()

elif selected == "Rencana Kerja":
    from pages import rencana_kerja
    rencana_kerja.run()
