import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data Bersih
df = pd.read_csv('main_data.csv')
df['tanggal'] = pd.to_datetime(df['tanggal'])

# Dictionary Mapping (Hanya di memori, tidak nambah kolom ke CSV)
cat_map = {0: 'Kebutuhan', 1: 'Keinginan', 2: 'Tabungan'}
status_map = {0: 'Hemat', 1: 'Normal', 2: 'Boros'}

st.title("Personal Finance Insight & Prediction")

# --- RQ1: PIE CHART ---
st.header("1. Analisis Alokasi Dana (RQ1)")
df_exp = df[df['tipe'] == 1].copy()
# Kita bikin variabel sementara untuk grafik, bukan nambah kolom ke df utama
label_tmp = df_exp['nama_kategori'].map(cat_map)
data_pie = df_exp.groupby(label_tmp)['jumlah'].sum()

fig1, ax1 = plt.subplots()
ax1.pie(data_pie, labels=data_pie.index, autopct='%1.1f%%', colors=['#FF9999','#66B3FF','#99FF99'])
st.pyplot(fig1)

# --- RQ2: BAR CHART ---
st.header("2. Ambang Batas Pengeluaran (RQ2)")
# Mapping status hanya untuk sumbu X grafik
status_x = df[df['tipe'] == 1]['Status'].map(status_map)
avg_spend = df[df['tipe'] == 1].groupby(status_x)['jumlah'].mean()

fig2, ax2 = plt.subplots()
sns.barplot(x=avg_spend.index, y=avg_spend.values, palette='OrRd', ax=ax2)
ax2.set_ylabel('Rata-rata Rp')
st.pyplot(fig2)

# --- ANALISIS LANJUTAN: RFM ---
st.header("3. Analisis RFM")
rfm = df.groupby('nama_kategori').agg({'jumlah': 'sum', 'tipe': 'count'}).reset_index()
rfm['Kategori'] = rfm['nama_kategori'].map(cat_map)

fig3, ax3 = plt.subplots()
sns.barplot(data=rfm, x='Kategori', y='jumlah', ax=ax3)
st.pyplot(fig3)
