import streamlit as st
import re








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
        st.button("**DOWNLOAD   📩**")
    else:
        st.error("Please enter a valid link !")
