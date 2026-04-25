import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="YouTube Downloader HD", page_icon="🎥")

st.title("🎥 YouTube MP4 Downloader")
st.write("Masukkan link video YouTube untuk mendownload dalam resolusi 1080p.")

url = st.text_input("Paste link YouTube di sini:", placeholder="https://www.youtube.com/watch?v=...")

if st.button("Generate Download Link"):
    if url:
        with st.spinner("Sedang memproses video... Mohon tunggu."):
            try:
                # Setup opsi yt-dlp
                ydl_opts = {
                    'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080]',
                    'merge_output_format': 'mp4',
                    'outtmpl': 'downloaded_video.mp4', # Nama file sementara
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                # Sediakan tombol download di UI
                with open("downloaded_video.mp4", "rb") as file:
                    st.video("downloaded_video.mp4") # Preview video
                    st.download_button(
                        label="Klik di sini untuk Simpan MP4",
                        data=file,
                        file_name="video_youtube_1080p.mp4",
                        mime="video/mp4"
                    )
                
                # Hapus file sementara setelah diproses agar tidak memenuhi storage server
                os.remove("downloaded_video.mp4")

            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
    else:
        st.warning("Silakan masukkan URL terlebih dahulu!")