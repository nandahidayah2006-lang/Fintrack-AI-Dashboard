# 💰 Personal Finance Insight & Prediction Dashboard

Aplikasi Dashboard interaktif berbasis Python yang dirancang untuk menganalisis perilaku keuangan pengguna, memberikan rekomendasi strategis, dan memprediksi kondisi keuangan menggunakan pendekatan Machine Learning dan analisis statistik RFM.

## 🚀 Fitur Utama

*   **Analisis Alokasi Dana (RQ1):** Visualisasi proporsi pengeluaran (Kebutuhan, Keinginan, Tabungan) menggunakan Pie Chart untuk memahami distribusi finansial secara objektif.
*   **Sistem Rekomendasi Ambang Batas (RQ2):** Menentukan batas pengeluaran "Normal" melalui analisis rata-rata transaksi guna mencegah perilaku "Boros".
*   **Prediksi Kondisi Keuangan (RQ3):** Pemanfaatan Matriks Korelasi dan Scatter Plot untuk melihat hubungan antar variabel (Jumlah vs Saldo) sebagai basis prediksi AI.
*   **Analisis Lanjutan RFM:** Segmentasi perilaku transaksi berdasarkan *Recency* (waktu terakhir), *Frequency* (intensitas), dan *Monetary* (nominal) untuk melihat pola "Bocor Alus" pada keuangan.

## 🛠️ Tech Stack

*   **Bahasa:** Python 3.x
*   **Library:** Pandas, Matplotlib, Seaborn
*   **Framework:** Streamlit (Web Dashboard)
*   **Analisis:** RFM Analysis, Correlation Matrix, Feature Engineering

## 📂 Struktur Repositori

| File | Deskripsi |
| :--- | :--- |
| `app.py` | Script utama untuk menjalankan dashboard Streamlit |
| `main_data.csv` | Dataset keuangan yang telah melalui proses *cleaning* & *labeling* |
| `requirements.txt` | Daftar library Python yang diperlukan |
| `README.md` | Dokumentasi lengkap proyek |

## ⚙️ Cara Menjalankan

1. **Clone Repositori:**
   ```bash
   git clone [https://github.com/username-kamu/nama-repo.git](https://github.com/username-kamu/nama-repo.git)
   cd nama-repo
