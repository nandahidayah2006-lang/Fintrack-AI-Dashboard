import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv('main_data.csv')
df['tanggal'] = pd.to_datetime(df['tanggal'])

# Mapping
cat_map = {0: 'Kebutuhan', 1: 'Keinginan', 2: 'Tabungan'}
status_labels = {0: 'Hemat', 1: 'Normal', 2: 'Boros'}

# Set Seaborn Style
sns.set(style="whitegrid")

# --- HEADER ---
st.title("Personal Finance Insight & Prediction")
st.markdown("---")

# --- RQ1: PIE CHART (Sesuai Gambar 3) ---
st.header("1. Analisis Alokasi Dana (RQ1)")
df_exp = df[df['tipe'] == 1].copy()
df_exp['nama_kategori_label'] = df_exp['nama_kategori'].map(cat_map)
persentase_kategori = df_exp.groupby('nama_kategori_label')['jumlah'].sum()

fig1, ax1 = plt.subplots(figsize=(8, 8))
ax1.pie(persentase_kategori, labels=persentase_kategori.index, autopct='%1.1f%%', 
        colors=['#FF9999', '#66B3FF', '#99FF99'], explode=[0.05, 0.05, 0.05], shadow=True)
ax1.set_title('Proporsi Pengeluaran untuk Memahami Kondisi Keuangan (RQ1)')
st.pyplot(fig1)

# --- RQ2: BAR CHART (Sesuai Gambar 4) ---
st.header("2. Ambang Batas Pengeluaran (RQ2)")
df['status_label'] = df['Status'].map(status_labels)
avg_spend_status = df[df['tipe'] == 1].groupby('status_label')['jumlah'].mean().sort_values()

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x=avg_spend_status.index, y=avg_spend_status.values, palette='OrRd', ax=ax2)
ax2.axhline(avg_spend_status['Normal'], color='blue', linestyle='--', label='Batas Normal')
ax2.set_title('Rata-rata Nominal Pengeluaran per Status (Dasar Rekomendasi RQ2)')
ax2.set_ylabel('Rata-rata Jumlah (Rp)')
ax2.legend()
st.pyplot(fig2)
st.info("💡 Rekomendasi: Hindari transaksi di atas rata-rata 'Normal' agar saldo tetap terjaga.")

# --- RQ3: HEATMAP & SCATTER (Sesuai Gambar 5) ---
st.header("3. Tren Saldo & Prediksi AI (RQ3)")
fig3, (ax3a, ax3b) = plt.subplots(1, 2, figsize=(15, 6))

# Heatmap
corr = df[['tipe', 'jumlah', 'sisa_saldo', 'Status']].corr()
sns.heatmap(corr, annot=True, cmap='RdYlGn', fmt=".2f", ax=ax3a)
ax3a.set_title('Matriks Korelasi Fitur AI')

# Scatter
sns.scatterplot(x='sisa_saldo', y='jumlah', hue='status_label', data=df, palette='viridis', alpha=0.6, ax=ax3b)
ax3b.set_title('Sebaran Data: Jumlah vs Sisa Saldo')
st.pyplot(fig3)

# --- ANALISIS LANJUTAN: RFM (Sesuai Gambar 6) ---
st.header("4. Analisis Lanjutan: RFM Per Kategori")
rfm_data = df.groupby('nama_kategori').agg({
    'tanggal': lambda x: (df['tanggal'].max() - x.max()).days,
    'tipe': 'count',
    'jumlah': 'sum'
}).rename(columns={'tanggal': 'Recency', 'tipe': 'Frequency', 'jumlah': 'Monetary'}).reset_index()
rfm_data['nama_kategori_label'] = rfm_data['nama_kategori'].map(cat_map)

fig4, ax4a = plt.subplots(figsize=(12, 6))
sns.barplot(x='nama_kategori_label', y='Monetary', data=rfm_data, ax=ax4a, palette='Blues_d', alpha=0.7)
ax4a.set_ylabel('Total Monetary (Rp)', color='b')

ax4b = ax4a.twinx()
sns.lineplot(x='nama_kategori_label', y='Frequency', data=rfm_data, marker='o', color='red', ax=ax4b, linewidth=3)
ax4b.set_ylabel('Frequency (Jumlah Transaksi)', color='r')
ax4a.set_title('Analisis Lanjutan: RFM Per Kategori (Monetary vs Frequency)')
st.pyplot(fig4)
