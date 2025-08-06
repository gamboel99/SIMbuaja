
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Laporan Keuangan", layout="wide")
st.title("📊 Laporan Keuangan BUMDes Buwana Raharja")

# Simulasi data
data = pd.DataFrame({
    'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'],
    'Pemasukan': [12000000, 15000000, 11000000, 17000000, 16000000, 18000000],
    'Pengeluaran': [8000000, 7000000, 6000000, 9000000, 9500000, 10000000]
})

data['Laba'] = data['Pemasukan'] - data['Pengeluaran']

st.subheader("Grafik Keuangan")
fig, ax = plt.subplots(figsize=(10, 4))
data.plot(x='Bulan', y=['Pemasukan', 'Pengeluaran', 'Laba'], kind='bar', ax=ax)
st.pyplot(fig)

st.subheader("Tabel Laporan")
st.dataframe(data)

# Ekspor ke Excel
st.subheader("Ekspor")
if st.button("📥 Unduh sebagai Excel"):
    data.to_excel("laporan_keuangan.xlsx", index=False)
    with open("laporan_keuangan.xlsx", "rb") as f:
        st.download_button("Download File Excel", f, file_name="laporan_keuangan.xlsx")
