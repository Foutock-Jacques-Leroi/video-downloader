import streamlit as st
import re
import yt_dlp






def download_video(link):
    ydl_opts = {
        'outtmpl':'%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=True)
        return info['title']
    

st.title("Hello You        ✨")
st.empty()


link = st.text_input("**ENTER YOUR VIDEO LINK**")





if link != "":
    pattern = re.compile(r'^https?://\S+$')
    if pattern.match(link):
        st.success("**Valid Link!**")
        st.write("I hope you coscent and agree you are responsible for the video link you put in the form!!!")


        st.write("copyrights Protected")
        st.checkbox("I Conscent ",value=True)
        if st.button("**DOWNLOAD   📩**"):
            try:
                title = download_video(link)
            except Exception as e:
                st.error(f"error {str(e)}")
    else:
        st.error("Please enter a valid link !")
