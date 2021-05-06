import _final
import _comp_two
import streamlit as st 

PAGES = {
    "Main Page": _final,
    "Two Comparisons": _comp_two
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
