import base64
import streamlit as st

from about import about
from publications import publications


def load_custom_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_custom_css("style.css")

st.set_page_config(page_title="Brahmani Nutakki", initial_sidebar_state="expanded")

page_names_to_funcs = {
    "About": about,
    "Publications": publications,
}

with open("assets/cartoon.jpeg", "rb") as f:
    image_data = f.read()
encoded = base64.b64encode(image_data).decode()

st.sidebar.markdown(f"""
    <img src="data:image/jpeg;base64,{encoded}" class="rounded-image" />
""", unsafe_allow_html=True)


st.sidebar.markdown("---")


st.sidebar.markdown("""
<div style="text-align: center;">
    Mail: bnutakki[at]cs[dot]uni-saarland[dot]de
</div>
""", unsafe_allow_html=True)
st.sidebar.markdown("\n")
st.sidebar.markdown("""
<div style="display: flex; justify-content: space-around; align-items: center;">
    <a href="http://linkedin.com/in/brahmani-nutakki" target="_blank">
        <img src="https://img.icons8.com/ios-filled/30/ffffff/linkedin.png"/>
    </a>
    <a href="https://bsky.app/profile/brahmaninutakki.bsky.social" target="_blank">
        <img src="https://logowik.com/content/uploads/images/bluesky-butterfly-icon9071.logowik.com.webp" width="30"/>
    </a>
    <a href="http://github.com/nbrahmani" target="_blank">
        <img src="https://img.icons8.com/ios-glyphs/30/ffffff/github.png"/>
    </a>
</div>
""", unsafe_allow_html=True)



st.sidebar.markdown("---")


if "page" not in st.session_state:
    st.session_state.page = "About"


if st.sidebar.button("About"):
    st.session_state.page = "About"
if st.sidebar.button("Publications"):
    st.session_state.page = "Publications"

page_names_to_funcs[st.session_state.page]()