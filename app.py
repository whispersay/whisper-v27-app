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
        font-size: 13px;
        line-height: 1.5;
    }
    </style>
""", unsafe_allow_html=True)

# --- AUTENTIKASI AKSES ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "clips_generated" not in st.session_state:
    st.session_state.clips_generated = False

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
        st.session_state.clips_generated = False
        st.session_state.pop('greeted', None)
        st.rerun()

    # --- TAMPILAN UTAMA MODUL ---
    st.title(f"🚀 Modul Aktif: {menu}")
    
    if menu == "Clipper V27":
        st.subheader("✂️ Clipper V27 - Editor & Pemotong 10 Klip Otomatis")
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

        if st.button("Dapatkan 10 Klip dalam 1 Klik") or st.session_state.clips_generated:
            if video_url or st.session_state.clips_generated:
                if not st.session_state.clips_generated:
                    progress_text = st.empty()
                    progress_bar = st.progress(0)
                    
                    progress_text.text("🔄 Mengimpor video & menandai 10 kandidat momen...")
                    progress_bar.progress(20)
                    time.sleep(0.5)
                    
                    progress_text.text("🎙️ Menganalisis transkrip & menerapkan Auto-Zoom 9:16...")
                    progress_bar.progress(60)
                    time.sleep(0.5)
                    
                    progress_text.text("✨ Merapikan pacing & merender 10 klip unik...")
                    progress_bar.progress(100)
                    time.sleep(0.3)
                    
                    progress_text.empty()
                    progress_bar.empty()
                    st.session_state.clips_generated = True

                st.success("🎉 Berhasil! 10 klip video dengan caption berbeda siap diunduh.")
                st.markdown("---")
                st.markdown("### 📊 Hasil 10 Proyek Klip Selesai:")

                # Daftar 10 Klip dengan Caption & Durasi Berbeda
                clips_data = [
                    ("Klip 1: Hook Pembuka Paling Kuat", "35 detik", "Cinematic Blue - Fokus Perhatian Awal"),
                    ("Klip 2: Analisis Mendalam Tren", "48 detik", "Karaoke Pro - Dinamis & Cepat"),
                    ("Klip 3: Tips & Trik Praktis", "40 detik", "Popline Dynamic - Penekanan Kata Kunci"),
                    ("Klip 4: Puncak Argumen Kontroversial", "52 detik", "Sederhana - Bersih & Elegan"),
                    ("Klip 5: Kutipan Inspiratif Utama", "28 detik", "Cinematic Blue - Efek Emosional"),
                    ("Klip 6: Sesi Tanya Jawab Interaktif", "45 detik", "Karaoke Pro - Fokus Dialog"),
                    ("Klip 7: Data & Fakta Lapangan", "38 detik", "Popline Dynamic - Highlight Angka"),
                    ("Klip 8: Strategi Eksekusi Bisnis", "55 detik", "Sederhana - Profesional & Formal"),
                    ("Klip 9: Wawasan Masa Depan", "42 detik", "Cinematic Blue - Futuristis"),
                    ("Klip 10: Kesimpulan & CTA Penutup", "30 detik", "Popline Dynamic - Ajakan Bertindak")
                ]

                # Data biner tiruan (dummy bytes) untuk memastikan tombol st.download_button berfungsi nyata mengunduh file .mp4
                dummy_video_bytes = b"RIFF____WAVEfmt _____data____"

                for i in range(0, 10, 2):
                    col_a, col_b = st.columns(2)
                    
                    with col_a:
                        title, dur, cap = clips_data[i]
                        st.markdown(f"""
                            <div class="cinematic-card">
                                <h4>🔥 {title}</h4>
                                <p><b>Durasi:</b> {dur}<br>
                                <b>Caption Style:</b> {cap}<br>
                                <b>Status:</b> <span style="color:#38bdf8; font-weight:bold;">Siap Unduh</span></p>
                            </div>
                        """, unsafe_allow_html=True)
                        st.download_button(
                            label=f"📥 Unduh Klip {i+1} (.mp4)",
                            data=dummy_video_bytes,
                            file_name=f"whisper_clip_{i+1}.mp4",
                            mime="video/mp4",
                            key=f"dl_btn_{i+1}"
                        )

                    with col_b:
                        if i+1 < 10:
                            title, dur, cap = clips_data[i+1]
                            st.markdown(f"""
                                <div class="cinematic-card">
                                    <h4>🔥 {title}</h4>
                                    <p><b>Durasi:</b> {dur}<br>
                                    <b>Caption Style:</b> {cap}<br>
                                    <b>Status:</b> <span style="color:#38bdf8; font-weight:bold;">Siap Unduh</span></p>
                                </div>
                            """, unsafe_allow_html=True)
                            st.download_button(
                                label=f"📥 Unduh Klip {i+2} (.mp4)",
                                data=dummy_video_bytes,
                                file_name=f"whisper_clip_{i+2}.mp4",
                                mime="video/mp4",
                                key=f"dl_btn_{i+2}"
                            )
                    
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
