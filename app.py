import streamlit as st
import os
import google.generativeai as genai

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Whisper.AI V27 - Suite Terpadu",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- MASTER PASSWORD (DIKUNCI DI KODE) & API KEY (DARI SECRETS) ---
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

# --- CSS CUSTOM STYLING ---
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stButton>button {
        background: linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%);
        color: white; border: none; border-radius: 8px;
        font-weight: bold; padding: 0.5rem 1rem;
    }
    .stTextInput>div>div>input {
        background-color: #161b22; color: white; border-radius: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# --- AUTENTIKASI AKSES ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

st.sidebar.title("🛡️ Whisper.AI V27")
st.sidebar.write("Aplikasi Terpadu Modul @yuldiana67")

if not st.session_state.authenticated:
    st.title("🔐 Akses Terkunci")
    input_pass = st.text_input("Masukkan Master Password:", type="password")
    if st.button("Masuk"):
        if input_pass.strip() == MASTER_PASSWORD:
            st.session_state.authenticated = True
            st.success("Akses Diberikan! Selamat datang, Bos.")
            st.rerun()
        else:
            st.error("Password salah!")
else:
    # --- NAVIGASI MODUL ---
    menu = st.sidebar.radio(
        "Pilih Modul:",
        ["Clipper V27", "AnimaWhis Pro", "SEO Master"]
    )
    
    if st.sidebar.button("Keluar / Logout"):
        st.session_state.authenticated = False
        st.rerun()

    # --- TAMPILAN MODUL ---
    st.title(f"🚀 Modul: {menu}")
    
    if menu == "Clipper V27":
        st.subheader("✂️ Clipper V27 - Pemotong & Pemroses Video")
        video_url = st.text_input("Masukkan Link Video (YouTube / TikTok):")
        if st.button("Proses Video"):
            st.info("Memproses klip... Fitur pemrosesan siap dijalankan!")

    elif menu == "AnimaWhis Pro":
        st.subheader("🎨 AnimaWhis Pro - Generator Animasi & Konten")
        prompt = st.text_area("Masukkan Ide / Prompt Animasi:")
        if st.button("Generate Animasi"):
            if GEMINI_API_KEY:
                try:
                    model = genai.GenerativeModel("gemini-2.5-flash")
                    response = model.generate_content(f"Buatkan ide animasi berdasarkan: {prompt}")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Gagal memproses AI: {e}")
            else:
                st.warning("API Key Gemini belum diatur di Secrets Streamlit Cloud.")

    elif menu == "SEO Master":
        st.subheader("📈 SEO Master - Optimasi Judul & Deskripsi")
        topic = st.text_input("Topik Konten / Keyword Utama:")
        if st.button("Analisis SEO"):
            if GEMINI_API_KEY:
                try:
                    model = genai.GenerativeModel("gemini-2.5-flash")
                    response = model.generate_content(f"Buatkan 5 pilihan judul viral dan 1 deskripsi SEO friendly untuk topik: {topic}")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Gagal memproses AI: {e}")
            else:
                st.warning("API Key Gemini belum diatur di Secrets Streamlit Cloud.")
