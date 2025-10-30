import streamlit as st

# Конфиг страницы - убирает белые полосы и прячет интерфейс Streamlit
st.set_page_config(
    page_title="MogoHotel",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS чтобы убрать белые полосы и максимизировать контент
st.markdown("""
<style>
    /* Убираем отступы */
    .appview-container {
        padding: 0 !important;
    }
    
    .main {
        padding: 0 !important;
        margin: 0 !important;
    }
    
    .st-emotion-cache-1wbqy5l {
        padding: 0 !important;
    }
    
    /* Прячем Streamlit UI */
    #MainMenu {
        visibility: hidden;
    }
    
    footer {
        visibility: hidden;
    }
    
    header {
        visibility: hidden;
    }
    
    .stDeployButton {
        display: none;
    }
    
    /* Убираем мин-высоту */
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

# Загрузи HTML
with open('hotel_mockup.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Показывай HTML на весь экран
st.components.v1.html(html_content, height=4000, scrolling=True)
