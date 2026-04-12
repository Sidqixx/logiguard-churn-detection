# LogiGuard: Intelligence Logistics Churn Prediction

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://logiguard-churn-detection-mry5m9kxvkz97hdhnrpyxc.streamlit.app/)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)

LogiGuard adalah sistem deteksi *customer churn* berbasis **Deep Learning** yang dirancang khusus untuk industri logistik Indonesia (Studi Kasus: J&T Express). Menggunakan arsitektur Transformer (IndoBERT), sistem ini mampu memahami konteks ulasan pelanggan secara mendalam untuk memitigasi risiko kehilangan pelanggan.

## Key Features
- **Transformer-Based Analysis**: Menggunakan model `IndoBERT` untuk menangani nuansa bahasa, sarkasme, dan konteks spesifik logistik.
- **Hybrid Smart Labeling**: Metodologi labeling cerdas yang menggabungkan rating user (1-5) dan analisis sentimen untuk memvalidasi 'Gray Zone' (Bintang 3).
- **Optimized Data Pipeline**: Melalui tahap *scraping*, *deduplication*, dan *strategic undersampling* untuk memastikan model yang objektif (tidak bias).
- **Real-time Deployment**: Dashboard interaktif berbasis Streamlit untuk prediksi instan.

## Model Performance
Setelah melalui tahap validasi pada **1.062 ulasan terkurasi**, model ini mencatatkan performa luar biasa:
- **Accuracy**: 91%
- **Recall (Class: Churn)**: 95% (Sangat efektif mendeteksi pelanggan yang kecewa)
- **F1-Score**: 0.91

## Tech Stack
- **Core**: Python 3.12
- **AI/ML**: Transformers (HuggingFace), PyTorch, Scikit-Learn.
- **Data**: Google-Play-Scraper.
- **Deployment**: Streamlit Cloud.

# Installation & Usage
1. https://github.com/Sidqixx/logiguard-churn-detection.git
2. pip install -r requirements.txt
3. streamlit run app.py

Developed by **Teuku Sidqi Aulia Rahmad**
