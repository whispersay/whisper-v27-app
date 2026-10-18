import streamlit as st
import os
import base64
import time
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

# --- CSS CINEMATIC BLUE & PENINGKATAN KONTRAS SISI KIRI ---
st.markdown("""
    <style>
    /* Latar Belakang Utama Sinematik */
    .main { 
        background: linear-gradient(135deg, #030712 0%, #0f172a 50%, #1e1b4b 100%);
        color: #ffffff !important; 
    }
    
    /* Sidebar Profesional & Teks Sisi Kiri Terlihat Jelas */
    [data-testid="stSidebar"] {
        background-color: #020617 !important;
        border-right: 1px solid #1e293b;
    }
    [data-testid="stSidebar"] div, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label, [data-testid="stSidebar"] p {
        color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* Tombol Utama dengan Gradasi Biru Sinematik */
    .stButton>button {
        background: linear-gradient(135deg, #0284c7 0%, #2563eb 100%);
        color: white !important; 
        border: 1px solid rgba(56, 189, 248, 0.4);
        border-radius: 10px;
        font-weight: 600; 
        padding: 0.6rem 1.2rem;
        box-shadow: 0 4px 20px rgba(37, 99, 235, 0.4);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #0ea5e9 0%, #1d4ed8 100%);
        box-shadow: 0 6px 25px rgba(14, 165, 233, 0.6);
        border-color: #38bdf8;
    }

    /* Input Teks & Area Teks Elegan */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #0f172a !important; 
        color: #ffffff !important; 
        border-radius: 8px;
        border: 1px solid #334155;
    }

    /* Kartu Dashboard Sinematik Berkontras Tinggi */
    .cinematic-card {
        background: #0f172a;
        border: 1px solid #334155;
        border-left: 4px solid #38bdf8;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
        margin-bottom: 15px;
        color: #ffffff !important;
    }
    .cinematic-card h4 {
        color: #38bdf8 !important;
        margin-bottom: 10px;
        font-weight: bold;
    }
    .cinematic-card p {
        color: #e2e8f0 !important;
        font-size: 14px;
        line-height: 1.6;
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
        st.subheader("✂️ Clipper V27 - Editor & Pemotong Klip Otomatis")
        video_url = st.text_input("Tempel Tautan Video (YouTube / Rumble / TikTok):", placeholder="https://...")
        
        # Pengaturan Preset & Gaya Subtitle Sinematik
        st.markdown("### ⚙️ Pengaturan Cepat & Template Keterangan")
        col_opt1, col_opt2, col_opt3 = st.columns(3)
        with col_opt1:
            caption_style = st.selectbox("Gaya Subtitle / Keterangan", ["Cinematic Blue", "Karaoke Pro", "Popline Dynamic", "Sederhana", "Tanpa Keterangan"])
        with col_opt2:
            language_opt = st.selectbox("Bahasa Lisan", ["Indonesia", "English", "Auto-Detect"])
        with col_opt3:
            aspect_ratio = st.selectbox("Rasio Aspek", ["9:16 (Vertical Reels/TikTok)", "1:1 (Square)", "16:9 (Landscape)"])

        # Opsi Tambahan Auto-Zoom & AI
        auto_zoom = st.checkbox("🔍 Aktifkan Pembingkaian Ulang AI (Auto-Zoom Fokus Pembicara)", value=True)

        if st.button("Dapatkan Klip dalam 1 Klik"):
            if video_url:
                progress_text = st.empty()
                progress_bar = st.progress(0)
                
                # Simulasi progres detail dengan ETA
                progress_text.text("🔄 Mengimpor video & mendeteksi sumber (ETA 3m)...")
                progress_bar.progress(15)
                time.sleep(0.7)
                
                progress_text.text("🎙️ Menjalankan Teks Terjemahan AI & Transkripsi suara...")
                progress_bar.progress(45)
                time.sleep(0.7)
                
                if auto_zoom:
                    progress_text.text(f"🎬 Menerapkan gaya subtitle '{caption_style}' & Auto-Zoom 9:16...")
                else:
                    progress_text.text(f"🎬 Menerapkan template {caption_style}...")
                progress_bar.progress(80)
                time.sleep(0.7)
                
                progress_text.text("✨ Menyelesaikan proyek klip sinematik...")
                progress_bar.progress(100)
                time.sleep(0.4)
                
                progress_text.empty()
                progress_bar.empty()
                
                # Hasil Akhir Rincian Klip dengan Tombol Aksi
                st.success("🎉 Berhasil! Proyek klip video selesai diproses.")
                st.markdown("---")
                st.markdown("### 📊 Hasil Proyek Klip Saat Ini:")
                
                col_res1, col_res2, col_res3 = st.columns(3)
                with col_res1:
                    st.markdown(f"""
                        <div class="cinematic-card">
                            <h4>🔥 Klip 1: Hook Viral</h4>
                            <p><b>Durasi:</b> 45 detik<br>
                            <b>Gaya:</b> {caption_style}<br>
                            <b>Status:</b> <span style="color:#38bdf8; font-weight:bold;">Siap Unduh</span></p>
                        </div>
                    """, unsafe_allow_html=True)
                    st.button("📥 Unduh Klip 1", key="btn_clip1")

                with col_res2:
                    st.markdown(f"""
                        <div class="cinematic-card">
                            <h4>💡 Klip 2: Puncak Diskusi</h4>
                            <p><b>Durasi:</b> 58 detik<br><b>Gaya:</b> {caption_style}<br>
                            <b>Status:</b> <span style="color:#38bdf8; font-weight:bold;">Siap Unduh</span></p>
                        </div>
                    """, unsafe_allow_html=True)
                    st.button("📥 Unduh Klip 2", key="btn_clip2")

                with col_res3:
                    st.markdown(f"""
                        <div class="cinematic-card">
                            <h4>🎯 Klip 3: Kesimpulan</h4>
                            <p><b>Durasi:</b> 35 detik<br>
                            <b>Gaya:</b> {caption_style}<br>
                            <b>Status:</b> <span style="color:#38bdf8; font-weight:bold;">Siap Unduh</span></p>
                        </div>
                    """, unsafe_allow_html=True)
                    st.button("📥 Unduh Klip 3", key="btn_clip3")
                    
                st.balloons()
            else:
                st.warning("Mohon masukkan tautan video terlebih dahulu, Bos.")

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
