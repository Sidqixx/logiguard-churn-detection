# LogiGuard: AI-Powered Customer Retention System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([LINK_DEPLOY_LO_NANTI])
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)

LogiGuard adalah sistem prediksi *customer churn* cerdas yang dirancang khusus untuk industri logistik di Indonesia. Proyek ini menggabungkan **Natural Language Processing (NLP)** dengan **Machine Learning** untuk mendeteksi pelanggan yang berisiko berhenti menggunakan layanan berdasarkan ulasan di Google Play Store.

## Key Features
- **Smart Labeling with IndoBERT**: Menggunakan model `mdhugol/indobert-sentiment-classification` untuk menganalisis sentimen ulasan bintang 3 (gray zone) untuk mendeteksi review yang ambigu.
- **Predictive Modeling**: Menggunakan algoritma **Random Forest** dengan teknik *Class Weighting* untuk menangani data yang tidak seimbang (*imbalanced data*).
- **Interactive Dashboard**: Aplikasi web berbasis Streamlit untuk prediksi *real-time* dan analisis probabilitas.
- **End-to-End Pipeline**: Mulai dari *web scraping* (Play Store), *data cleaning*, hingga *deployment*.

## Model Performance
Model ini telah divalidasi dengan performa yang cukup tinggi, terutama dalam mendeteksi pelanggan yang akan *churn*:
- **Accuracy**: 92.99%
- **Recall (Class: Churn)**: 97%
- **F1-Score (Weighted)**: 0.93

## Tech Stack
- **Languages**: Python
- **Libraries**: Scikit-Learn, Transformers (HuggingFace), Pandas, Matplotlib, Seaborn.
- **Deployment**: Streamlit Cloud
- **Model**: IndoBERT & Random Forest Classifier

# Installation & Usage
1. https://github.com/Sidqixx/logiguard-churn-detection.git
2. pip install -r requirements.txt
3. streamlit run app.py

# Business Insights
Berdasarkan analisis WordCloud, ditemukan bahwa penyebab utama churn pada layanan logistik ini adalah:
-Masalah Operasional: Keterlambatan pengiriman ("lama", "hari", "minggu").
-SDM/Kurir: Interaksi dengan kurir di lapangan ("kurir", "kurirnya").
Keamanan Barang: Risiko kehilangan paket ("hilang").

Developed by **Teuku Sidqi Aulia Rahmad**
