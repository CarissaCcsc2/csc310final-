import final
import comp_two
import streamlit as st 
from PIL import Image


PAGES = {
    "Main Page": final,
    "Two Comparisons": comp_two
}

img = Image.open('AC_icon.png')

st.set_page_config(
    page_title='Animal Crossing Ro.',
    page_icon = img,
    initial_sidebar_state="expanded",
)

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
