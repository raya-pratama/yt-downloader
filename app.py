import streamlit as st
from pytube import YouTube
import os

st.title("🎥 YouTube Downloader (v2)")

url = st.text_input("Masukkan link YouTube:")

if st.button("Proses Video"):
    try:
        yt = YouTube(url)
        # Mengambil resolusi 720p karena biasanya video & audio sudah jadi satu (Progressive)
        # Ini menghindari error merging di server cloud
        video = yt.streams.filter(progressive=True, file_extension='mp4', res="720p").first()
        
        if video:
            with st.spinner("Downloading..."):
                out_file = video.download()
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp4'
                os.rename(out_file, new_file)
                
                with open(new_file, "rb") as f:
                    st.download_button("Download Sekarang", f, file_name="video.mp4")
                
                os.remove(new_file)
        else:
            st.error("Resolusi 720p tidak tersedia untuk video ini.")
    except Exception as e:
        st.error(f"Error: {e}")
