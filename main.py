import final
import comp_two
import streamlit as st 

PAGES = {
    "Main Page": final,
    "Two Comparisons": comp_two
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()