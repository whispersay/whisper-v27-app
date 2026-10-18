import streamlit as st
import os
import base64
import google.generativeai as genai
from gtts import gTTS

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Whisper.AI V27 - Suite Terpadu",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- MASTER PASSWORD & API KEY ---
MASTER_PASSWORD = "yuldiana-secret-2026"

try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    GEMINI_API_KEY = ""

if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
    except Exception:
        pass

# --- FUNGSI SUARA INTERAKTIF ---
def speak(text):
    try:
        tts = gTTS(text=text, lang='id')
        tts.save("speech.mp3")
        with open("speech.mp3", "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f'<audio autoplay="true" src="data:audio/mp3;base64,{b64}">'
        st.markdown(md, unsafe_allow_html=True)
    except Exception:
        pass

# --- CSS NEON STYLE ---
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stButton>button {
        background: linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%);
        color: white; border: none; border-radius: 12px;
        font-weight: bold; padding: 0.6rem 1.2rem;
        box-shadow: 0 0 15px rgba(0, 210, 255, 0.4);
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #161b22; color: white; border-radius: 8px;
        border: 1px solid #30363d;
    }
    </style>
""", unsafe_allow_html=True)

# --- AUTENTIKASI AKSES ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

st.sidebar.title("🛡️ Whisper.AI V27")
st.sidebar.write("Aplikasi Terpadu Modul @yuldiana67")

if not st.session_state.authenticated:
    st.title("🔐 Akses Terkunci - Whisper.AI")
    input_pass = st.text_input("Masukkan Master Password:", type="password")
    if st.button("Masuk"):
        if input_pass.strip() == MASTER_PASSWORD:
            st.session_state.authenticated = True
            st.success("Akses Diberikan! Selamat datang, Bos.")
            st.rerun()
        else:
            st.error("Password salah!")
else:
    # --- SAPAAN SUARA KETIKA BERHASIL MASUK ---
    if 'greeted' not in st.session_state:
        speak("Syaloom Bos yuldiana cantik. Saya Whisper A I siap membantu kerajaan digital Anda.")
        st.session_state.greeted = True

    # --- NAVIGASI MODUL ---
    menu = st.sidebar.radio(
        "Pilih Modul Kreatif:",
        ["Clipper V27", "AnimaWhis Pro", "SEO Master"]
    )
    
    if st.sidebar.button("Keluar / Logout"):
        st.session_state.authenticated = False
        st.session_state.pop('greeted', None)
        st.rerun()

    # --- TAMPILAN UTAMA MODUL ---
    st.title(f"🚀 Modul Aktif: {menu}")
    
    if menu == "Clipper V27":
        st.subheader("✂️ Clipper V27 - Pemotong & Pemroses Video Viral")
        video_url = st.text_input("Tempel Link Video (YouTube / TikTok / IG):", placeholder="https://...")
        if st.button("Proses Klip Video"):
            if video_url:
                st.success("🔗 Link video berhasil diterima oleh Clipper V27!")
                st.info("Menyiapkan format rasio 9:16 vertical untuk TikTok & Reels...")
            else:
                st.warning("Mohon masukkan link video terlebih dahulu, Bos.")

    elif menu == "AnimaWhis Pro":
        st.subheader("🎨 AnimaWhis Pro - Generator Konten & Ide Kreatif")
        prompt = st.text_area("Masukkan Ide / Prompt Konten Animasi:")
        if st.button("Generate Ide Konten"):
            if GEMINI_API_KEY:
                try:
                    with st.spinner("Whisper sedang meracik ide kreatif untuk Bos..."):
                        model = genai.GenerativeModel("gemini-2.5-flash")
                        response = model.generate_content(f"Buatkan konsep konten dan naskah singkat berdasarkan: {prompt}")
                        st.markdown("### Hasil Kreasi AnimaWhis:")
                        st.write(response.text)
                except Exception as e:
                    st.error(f"Gagal memproses AI: {e}")
            else:
                st.warning("API Key Gemini belum terkonfigurasi di Secrets.")

    elif menu == "SEO Master":
        st.subheader("📈 SEO Master - Optimasi Judul & Algoritma")
        topic = st.text_input("Topik Konten / Keyword Utama:")
        if st.button("Analisis SEO & Judul Viral"):
            if GEMINI_API_KEY:
                try:
                    with st.spinner("Menganalisis tren algoritma..."):
                        model = genai.GenerativeModel("gemini-2.5-flash")
                        response = model.generate_content(f"Buatkan 5 pilihan judul video yang sangat menarik (clickbait elegan) dan 1 deskripsi SEO friendly untuk topik: {topic}")
                        st.markdown("### Rekomendasi SEO & Judul Viral:")
                        st.write(response.text)
                except Exception as e:
                    st.error(f"Gagal memproses AI: {e}")
            else:
                st.warning("API Key Gemini belum terkonfigurasi di Secrets.")
