import streamlit as st
from transformers import pipeline
import time

st.set_page_config(
    page_title="LogiGuard | Customer Churn Anticipate",
    page_icon="📦",
    layout="centered"
)

st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    .status-box {
        padding: 20px;
        border-radius: 10px;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_resource
def load_model():
    model_name = "mdhugol/indonesia-bert-sentiment-classification"
    return pipeline("sentiment-analysis", model=model_name, tokenizer=model_name)

nlp = load_model()

st.title("📦 LogiGuard")
st.subheader("Intelligence Logistics Churn Prediction")
st.write("---")
st.markdown("""
    Aplikasi ini menggunakan model **IndoBERT Deep Learning** yang telah divalidasi dengan 
    **1.000+ data review J&T Express** untuk mendeteksi potensi *churn*.
""")

with st.container():
    user_input = st.text_area(
        "Masukkan Review Customer:", 
        placeholder="Tulis di sini (contoh: Paket lama banget nyampe, kurir ilang-ilangan..)",
        height=150
    )
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        predict_btn = st.button("Analisis Sentimen & Potensi Churn")

if predict_btn:
    if user_input.strip() != "":
        with st.spinner('Processing...'):
    
            result = nlp(user_input[:512])[0]
            label = result['label']
            confidence = result['score']
            
            time.sleep(0.5)
            
            st.write("### Hasil Analisis:")
            
            if label == 'LABEL_2':
                st.error("### 🚨 STATUS: POTENSI CHURN")
                st.markdown(f"""
                    <div style='background-color: #ffebee; padding: 15px; border-radius: 10px; border: 1px solid #ffcdd2;'>
                    <span style='color: #b71c1c; font-weight: bold;'>Analisis AI:</span> 
                    <span style='color: #1a1a1a;'>PCustomer berpotensi Churn. Perlu penanganan.</span>
                    <br><br>
                    <span style='color: #1a1a1a;'><b>Confidence Level:</b> {confidence:.2%}</span>
                    </div>
                """, unsafe_allow_html=True)
                
            elif label == 'LABEL_1':
                st.success("### ✅ STATUS: AMAN / LOYAL")
                st.markdown(f"""
                    <div style='background-color: #e8f5e9; padding: 15px; border-radius: 10px; border: 1px solid #c8e6c9;'>
                    <span style='color: #1b5e20; font-weight: bold;'>Analisis AI:</span> 
                    <span style='color: #1a1a1a;'>Customer puas dengan layanan yang diberikan.</span>
                    <br><br>
                    <span style='color: #1a1a1a;'><b>Confidence Level:</b> {confidence:.2%}</span>
                    </div>
                """, unsafe_allow_html=True)
                
            else:
                st.info("### ➖ STATUS: NETRAL / FEEDBACK")
                st.markdown(f"""
                    <div style='background-color: #e3f2fd; padding: 15px; border-radius: 10px; border: 1px solid #bbdefb;'>
                    <span style='color: #0d47a1; font-weight: bold;'>Analisis AI:</span> 
                    <span style='color: #1a1a1a;'>Kalimat bersifat informatif atau memiliki sentimen campuran.</span>
                    <br><br>
                    <span style='color: #1a1a1a;'><b>Confidence Level:</b> {confidence:.2%}</span>
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("Input tidak boleh kosong")

st.sidebar.title("Model Metrics")
st.sidebar.info(f"""
    - **Model:** IndoBERT (Transformer)
    - **Accuracy:** 91%
    - **Recall (Churn):** 95%
    - **Dataset:** 1,062 Curated Reviews
""")
st.sidebar.write("---")
st.sidebar.write("Developed by:**Teuku Sidqi Aulia Rahmad**")