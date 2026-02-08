import streamlit as st
import re
import yt_dlp
import os

def download_video(link):
    # On définit des options pour récupérer le nom du fichier proprement
    ydl_opts = {
    'format': 'mp4/best', # Force le MP4 combiné direct
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # Force l'IPv4, souvent moins surveillé que l'IPv6
}
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # 1. On récupère les infos sans télécharger pour avoir le nom du fichier
        info = ydl.extract_info(link, download=False)
        filename = ydl.prepare_filename(info)
        
        # 2. On effectue le téléchargement réel
        ydl.download([link])
        
        return filename # TRÈS IMPORTANT : on renvoie le nom du fichier

st.title("Hello You ✨")

link = st.text_input("**ENTER YOUR VIDEO LINK**")

if link:
    pattern = re.compile(r'^https?://\S+$')
    if pattern.match(link):
        st.success("**Valid Link!**")
        st.write("I hope you consent and agree you are responsible...")

        consent = st.checkbox("I Consent", value=False)
        
        if consent:
            if st.button("**PREPARE DOWNLOAD 📩**"):
                try:
                    with st.spinner('Downloading from YouTube to server...'):
                        filename = download_video(link)
                    
                    # On vérifie si le fichier existe bien avant de proposer le bouton
                    if os.path.exists(filename):
                        with open(filename, 'rb') as f:
                            st.download_button(
                                label="CLICK HERE TO SAVE ON YOUR DEVICE",
                                data=f,
                                file_name=filename,
                                mime="video/mp4"
                            )
                        # Optionnel: supprimer le fichier du serveur après pour ne pas saturer l'espace
                        # os.remove(filename)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    else:
        st.error("Please enter a valid link !")