# --- FUNGSI UNDUH VIDEO TANPA PERLU FFMPEG ---
def download_real_video(url):
    ydl_opts = {
        'format': 'best[ext=mp4]/best',  # Mengambil format tunggal siap pakai tanpa perlu ffmpeg
        'outtmpl': 'downloaded_video.mp4',
        'quiet': True,
        'no_warnings': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    with open('downloaded_video.mp4', 'rb') as f:
        data = f.read()
    return data
