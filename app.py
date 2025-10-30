import streamlit as st

st.set_page_config(page_title="MogoHotel", layout="wide", initial_sidebar_state="collapsed")

# Hide streamlit ui
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Загрузи HTML
with open('hotel_mockup.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Показай HTML на весь экран
st.components.v1.html(html_content, height=3000, scrolling=True)