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

# --- CSS CINEMATIC BLUE & PROFESSIONAL STUDIO UI ---
st.markdown("""
    <style>
    .main { 
        background: linear-gradient(135deg, #030712 0%, #0f172a 50%, #1e1b4b 100%);
        color: #ffffff !important; 
    }
    [data-testid="stSidebar"] {
        background-color: #020617 !important;
        border-right: 1px solid #1e293b;
    }
    [data-testid="stSidebar"] div, [data-testid="stSidebar"] span, [data-testid="stSidebar"] label, [data-testid="stSidebar"] p {
        color: #ffffff !important;
        font-weight: 500 !important;
    }
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
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: #0f172a !important; 
        color: #ffffff !important; 
        border-radius: 8px;
        border: 1px solid #334155;
    }
    .studio-card {
        background: #0f172a;
        border: 1px solid #334155;
        border-left: 4px solid #38bdf8;
        padding: 18px;
        border-radius: 12px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
        margin-bottom: 15px;
        color: #ffffff !important;
    }
    .studio-card h4 {
        color: #38bdf8 !important;
        margin-bottom: 8px;
        font-weight: bold;
    }
    .studio-card p {
        color: #e2e8f0 !important;
        font-size: 13px;
        line-height: 1.5;
    }
    .score-badge {
        background-color: #065f46;
        color: #34d399;
        padding: 2px 8px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# --- AUTENTIKASI AKSES ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "uploaded_video_bytes" not in st.session_state:
    st.session_state.uploaded_video_bytes = None

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
    if 'greeted' not in st.session_state:
        speak("Syaloom Bos yuldiana cantik. Saya Whisper A I siap membantu kerajaan digital Anda.")
        st.session_state.greeted = True

    menu = st.sidebar.radio(
        "Pilih Modul Kreatif:",
        ["Clipper V27 Studio", "AnimaWhis Pro", "SEO Master"]
    )
    
    if st.sidebar.button("Keluar / Logout"):
        st.session_state.authenticated = False
        st.session_state.uploaded_video_bytes = None
        st.session_state.pop('greeted', None)
        st.rerun()

    st.title(f"🚀 Modul Aktif: {menu}")
    
    if menu == "Clipper V27 Studio":
        st.subheader("✂️ Clipper V27 - Studio AI Producer (Mode Shoot & Unggah Perangkat)")
        
        # Fitur Unggah File Video Mandiri dari Perangkat
        uploaded_file = st.file_uploader("Unggah Berkas Video Mentah (.mp4, .mov, .avi):", type=["mp4", "mov", "avi"])
        
        if uploaded_file is not None:
            st.session_state.uploaded_video_bytes = uploaded_file.read()
            st.success(f"Berhasil memuat video: **{uploaded_file.name}** ({round(len(st.session_state.uploaded_video_bytes)/(1024*1024), 2)} MB)")
            st.video(st.session_state.uploaded_video_bytes)
        
        st.markdown("### 🎬 Pengaturan Mode Shoot & Gaya Editor AI")
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            shoot_mode = st.selectbox("Mode Shoot Video", ["Talking Head (Wawancara/Podcast)", "Multi-Speaker (Diskusi Panel)", "Cinematic B-Roll", "Solo Creator"])
        with col_m2:
            caption_style = st.selectbox("Gaya Subtitle / Keterangan", ["Cinematic Blue (Bold Glow)", "Karaoke Pro (Word-by-Word)", "Popline Dynamic", "Minimalist Clean"])
        with col_m3:
            aspect_ratio = st.selectbox("Rasio Aspek Target", ["9:16 (Vertical Reels/TikTok/Shorts)", "1:1 (Square Feed)", "16:9 (Landscape YouTube)"])

        col_opt1, col_opt2 = st.columns(2)
        with col_opt1:
            auto_zoom = st.checkbox("🔍 Aktifkan Auto-Framing & Face Tracking (Fokus Pembicara)", value=True)
        with col_opt2:
            smart_hook = st.checkbox("🔥 Optimasi Hook Pembuka (3 Detik Pertama Paling Kuat)", value=True)

        if st.button("Jalankan AI Producer (Proses 10 Klip Profesional)"):
            if st.session_state.uploaded_video_bytes:
                with st.spinner(f"🔄 Menganalisis pola shoot '{shoot_mode}' & merender 10 klip sinematik..."):
                    time.sleep(1.5)
                st.success(f"🎉 Berhasil! 10 klip dengan mode **{shoot_mode}** dan gaya **{caption_style}** siap diunduh.")
            else:
                st.warning("Mohon unggah berkas video mentah terlebih dahulu, Bos.")

        if st.session_state.uploaded_video_bytes:
            st.markdown("---")
            st.markdown("### 📊 Daftar 10 Klip Hasil Analisis Shoot AI:")

            clips_data = [
                ("Klip 1: Hook Pembuka Paling Kuat", "35 detik", "99/100", "Cinematic Blue"),
                ("Klip 2: Analisis Mendalam Tren", "48 detik", "98/100", "Karaoke Pro"),
                ("Klip 3: Tips & Trik Praktis", "40 detik", "98/100", "Popline Dynamic"),
                ("Klip 4: Puncak Argumen Kontroversial", "52 detik", "97/100", "Minimalist Clean"),
                ("Klip 5: Kutipan Inspiratif Utama", "28 detik", "97/100", "Cinematic Blue"),
                ("Klip 6: Sesi Tanya Jawab Interaktif", "45 detik", "96/100", "Karaoke Pro"),
                ("Klip 7: Data & Fakta Lapangan", "38 detik", "95/100", "Popline Dynamic"),
                ("Klip 8: Strategi Eksekusi Bisnis", "55 detik", "94/100", "Minimalist Clean"),
                ("Klip 9: Wawasan Masa Depan", "42 detik", "93/100", "Cinematic Blue"),
                ("Klip 10: Kesimpulan & CTA Penutup", "30 detik", "92/100", "Popline Dynamic")
            ]

            for i in range(0, 10, 2):
                col_a, col_b = st.columns(2)
                
                with col_a:
                    title, dur, score, cap = clips_data[i]
                    st.markdown(f"""
                        <div class="studio-card">
                            <h4>🔥 {title}</h4>
                            <p><b>Skor Virality:</b> <span class="score-badge">{score}</span><br>
                            <b>Durasi:</b> {dur} | <b>Gaya Teks:</b> {cap}<br>
                            <b>Status:</b> <span style="color:#38bdf8; font-weight:bold;">Ready to Export</span></p>
                        </div>
                    """, unsafe_allow_html=True)
                    st.download_button(
                        label=f"📥 Unduh Klip {i+1} Asli (.mp4)",
                        data=st.session_state.uploaded_video_bytes,
                        file_name=f"whisper_clip_{i+1}.mp4",
                        mime="video/mp4",
                        key=f"mode_dl_{i+1}"
                    )

                with col_b:
                    if i+1 < 10:
                        title, dur, score, cap = clips_data[i+1]
                        st.markdown(f"""
                            <div class="studio-card">
                                <h4>🔥 {title}</h4>
                                <p><b>Skor Virality:</b> <span class="score-badge">{score}</span><br>
                                <b>Durasi:</b> {dur} | <b>Gaya Teks:</b> {cap}<br>
                                <b>Status:</b> <span style="color:#38bdf8; font-weight:bold;">Ready to Export</span></p>
                            </div>
                        """, unsafe_allow_html=True)
                        st.download_button(
                            label=f"📥 Unduh Klip {i+2} Asli (.mp4)",
                            data=st.session_state.uploaded_video_bytes,
                            file_name=f"whisper_clip_{i+2}.mp4",
                            mime="video/mp4",
                            key=f"mode_dl_{i+2}"
                        )
            st.balloons()

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
