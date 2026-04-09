\#LogiGuard: AI-Powered Customer Retention System



\[!\[Streamlit App](https://static.streamlit.io/badges/streamlit\_badge\_black\_white.svg)](\[LINK\_DEPLOY\_LO\_NANTI])

\[!\[Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)



LogiGuard adalah sistem prediksi \*customer churn\* cerdas yang dirancang khusus untuk industri logistik di Indonesia. Proyek ini menggabungkan \*\*Natural Language Processing (NLP)\*\* dengan \*\*Machine Learning\*\* untuk mendeteksi pelanggan yang berisiko berhenti menggunakan layanan berdasarkan ulasan di Google Play Store.



\## Key Features

\- \*\*Smart Labeling with IndoBERT\*\*: Menggunakan model `mdhugol/indobert-sentiment-classification` untuk menganalisis sentimen ulasan bintang 3 (zona abu-abu) guna mendeteksi ketidakpuasan tersembunyi.

\- \*\*Predictive Modeling\*\*: Menggunakan algoritma \*\*Random Forest\*\* dengan teknik \*Class Weighting\* untuk menangani data yang tidak seimbang (\*imbalanced data\*).

\- \*\*Interactive Dashboard\*\*: Aplikasi web berbasis Streamlit untuk prediksi \*real-time\* dan analisis probabilitas.

\- \*\*End-to-End Pipeline\*\*: Mulai dari \*web scraping\* (Play Store), \*data cleaning\*, hingga \*deployment\*.



\##Model Performance

Model ini telah divalidasi dengan performa yang cukup tinggi, terutama dalam mendeteksi pelanggan yang akan \*churn\*:



\- \*\*Accuracy\*\*: 92.99%

\- \*\*Recall (Class: Churn)\*\*: 97%

\- \*\*F1-Score (Weighted)\*\*: 0.93





\##Tech Stack

\- \*\*Languages\*\*: Python

\- \*\*Libraries\*\*: Scikit-Learn, Transformers (HuggingFace), Pandas, Matplotlib, Seaborn.

\- \*\*Deployment\*\*: Streamlit Cloud

\- \*\*Model\*\*: IndoBERT \& Random Forest Classifier



⚙️ Installation \& Usage

1. git clone
2. pip install -r requirements.txt
3. streamlit run app.py



Gemini berkata

Siaap! README.md itu ibarat "sampul buku". Kalau sampulnya menarik, HRD atau Senior Engineer bakal betah baca kodingan lo. Karena lo anak CS BINUS, kita bikin yang strukturnya engineering-ready tapi tetep ada bumbu bisnisnya.



Ini template README.md yang udah gua susun khusus buat proyek lo. Lo tinggal copy-paste, terus ganti bagian yang di dalam kurung siku \[...].



Markdown

\# 📦 LogiGuard: AI-Powered Customer Retention System



\[!\[Streamlit App](https://static.streamlit.io/badges/streamlit\_badge\_black\_white.svg)](\[LINK\_DEPLOY\_LO\_NANTI])

\[!\[Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)



LogiGuard adalah sistem prediksi \*customer churn\* cerdas yang dirancang khusus untuk industri logistik di Indonesia. Proyek ini menggabungkan kekuatan \*\*Natural Language Processing (NLP)\*\* dengan \*\*Machine Learning\*\* untuk mendeteksi pelanggan yang berisiko berhenti menggunakan layanan berdasarkan ulasan di Google Play Store.



\## 🚀 Key Features

\- \*\*Smart Labeling with IndoBERT\*\*: Menggunakan model `mdhugol/indobert-sentiment-classification` untuk menganalisis sentimen ulasan bintang 3 (zona abu-abu) guna mendeteksi ketidakpuasan tersembunyi.

\- \*\*Predictive Modeling\*\*: Menggunakan algoritma \*\*Random Forest\*\* dengan teknik \*Class Weighting\* untuk menangani data yang tidak seimbang (\*imbalanced data\*).

\- \*\*Interactive Dashboard\*\*: Aplikasi web berbasis Streamlit untuk prediksi \*real-time\* dan analisis probabilitas.

\- \*\*End-to-End Pipeline\*\*: Mulai dari \*web scraping\* (Play Store), \*data cleaning\*, hingga \*deployment\*.



\## 📊 Model Performance

Model ini telah divalidasi dengan performa yang cukup tinggi, terutama dalam mendeteksi pelanggan yang akan \*churn\*:



\- \*\*Accuracy\*\*: 92.99%

\- \*\*Recall (Class: Churn)\*\*: 97%

\- \*\*F1-Score (Weighted)\*\*: 0.93







\## 🛠️ Tech Stack

\- \*\*Languages\*\*: Python

\- \*\*Libraries\*\*: Scikit-Learn, Transformers (HuggingFace), Pandas, Matplotlib, Seaborn.

\- \*\*Deployment\*\*: Streamlit Cloud

\- \*\*Model\*\*: IndoBERT \& Random Forest Classifier



\## 📁 Project Structure

```text

LogiGuard-AI/

├── models/

│   ├── model\_churn\_rf.pkl       # Trained Random Forest Model

│   └── tfidf\_vectorizer.pkl    # TF-IDF Vectorizer

├── notebooks/

│   ├── 01\_scraping.ipynb

│   ├── 02\_cleaning\_eda.ipynb

│   └── 03\_modeling.ipynb

├── app.py                      # Main Streamlit Application

├── requirements.txt            # Project Dependencies

└── README.md

⚙️ Installation \& Usage

Clone repository ini:



Bash

git clone \[https://github.com/](https://github.com/)\[USERNAME\_LO]/LogiGuard-AI.git

Install dependencies:



Bash

pip install -r requirements.txt

Jalankan aplikasi secara lokal:



Bash

streamlit run app.py

💡 Business Insights

Berdasarkan analisis WordCloud, ditemukan bahwa penyebab utama churn pada layanan logistik ini adalah:



Masalah Operasional: Keterlambatan pengiriman ("lama", "hari", "minggu").



SDM/Kurir: Interaksi dengan kurir di lapangan ("kurir", "kurirnya").



Keamanan Barang: Risiko kehilangan paket ("hilang").

