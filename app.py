import streamlit as st

st.set_page_config(
    page_title="MogoHotel",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS для убирания всех отступов и белых полос
st.markdown("""
<style>
    /* Убираем ВСЕ отступы */
    .main, .block-container, .appview-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    
    /* Прячем Streamlit UI */
    #MainMenu, footer, header, .stDeployButton {
        visibility: hidden;
        display: none;
    }
    
    /* Убираем iframe padding */
    iframe {
        border: none !important;
    }
    
    /* Растягиваем на весь экран */
    section[data-testid="stVerticalBlock"] {
        gap: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# Загружаем HTML
with open('hotel_mockup_compact.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Показываем с правильной высотой (без белого пространства)
st.components.v1.html(html_content, height=1800, scrolling=False)