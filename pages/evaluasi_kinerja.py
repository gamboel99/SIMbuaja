import streamlit as st
import pandas as pd

st.title("📈 Evaluasi Capaian Kinerja")

jabatan = st.selectbox("Pilih Jabatan", ["Direktur Utama", "Sekretaris", "Bendahara"])
filename = f"data/rencana_kerja/{jabatan.lower().replace(' ', '_')}.csv"

try:
    df = pd.read_csv(filename)

    idx = st.selectbox("Pilih Kegiatan", df['Tujuan'])
    idx_row = df[df['Tujuan'] == idx].index[0]

    capaian = st.selectbox("Capaian", ["Belum Dilaksanakan", "Sedang Berlangsung", "Selesai"])
    if st.button("✔️ Update Capaian"):
        df.at[idx_row, 'Status'] = capaian
        df.to_csv(filename, index=False)
        st.success("✅ Status kegiatan berhasil diperbarui.")

    st.subheader("📋 Rekap Rencana & Status")
    st.dataframe(df)

except FileNotFoundError:
    st.warning("Belum ada data untuk jabatan ini.")
