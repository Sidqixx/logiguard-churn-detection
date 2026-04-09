import streamlit as st
import joblib
import pandas as pd


model = joblib.load('models/model_churn_rf.pkl')
tfidf = joblib.load('models/tfidf_vectorizer.pkl')

st.set_page_config(page_title="LogiGuard AI", page_icon="🚀", layout="wide")

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/128/679/679821.png", width=100)
    st.title("LogiGuard Engine")
    st.info("Sistem ini didukung oleh **IndoBERT** & **Random Forest** dengan akurasi **92.99%**.")
    st.divider()
    st.write("Apps by: **Teuku Sidqi Aulia Rahmad**")
    st.write("Project: Customer Retention Analysis")

st.title("📦 Smart Logistics Churn Detector")
st.subheader("Analisis Sentimen & Prediksi Loyalitas Customer")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### **Input Review Customer**")
    user_review = st.text_area("Masukkan Review:", height=150, placeholder="Contoh: Paket saya sudah 2 minggu tidak sampai, kurir tidak bisa dihubungi!")
    btn_predict = st.button("🚀 Prediksi Status Customer", use_container_width=True)

if btn_predict:
    if user_review:
        # Transform & Predict
        text_vector = tfidf.transform([user_review])
        prediction = model.predict(text_vector)
        prob = model.predict_proba(text_vector)
        
        with col2:
            st.markdown("### **Hasil Analisis**")
            if prediction[0] == 1:
                st.error("🚨 **POTENSI CHURN**")
                # Bikin Gauge/Metric sederhana
                st.metric(label="Risk Level", value=f"{prob[0][1]*100:.1f}%")
                st.warning("Customer ini kemungkinan besar akan berhenti menggunakan jasa karena bad experience.")
            else:
                st.success("✅ **LOYAL CUSTOMER**")
                st.metric(label="Safety Level", value=f"{prob[0][0]*100:.1f}%")
                st.info("Customer merasa puas menggunakan layanan.")
            
            # Tambah bar chart probabilitas
            prob_df = pd.DataFrame({
                'Status': ['Aman', 'Churn'],
                'Probability': [prob[0][0], prob[0][1]]
            })
            st.bar_chart(prob_df.set_index('Status'))
    else:
        st.warning("Isi dulu teks review-nya!")

st.divider()
st.caption("© 2026 LogiGuard AI System- Teuku Sidqi Aulia Rahmad")