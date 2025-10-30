import streamlit as st

st.set_page_config(
    page_title="MogoHotel",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .main, .block-container, .appview-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    
    #MainMenu, footer, header, .stDeployButton {
        visibility: hidden;
        display: none;
    }
    
    iframe {
        border: none !important;
    }
    
    section[data-testid="stVerticalBlock"] {
        gap: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

with open('hotel_mockup.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

st.components.v1.html(html_content, height=1800, scrolling=False)
