import streamlit as st

st.set_page_config(page_title="MogoHotel", layout="wide")

# Загрузи HTML
with open('hotel_mockup.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

st.components.v1.html(html_content, height=2000, scrolling=True)