import streamlit as st

st.set_page_config(page_title="MogoHotel", layout="wide", initial_sidebar_state="collapsed")

# Hide streamlit ui
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Загрузи HTML
with open('hotel_mockup.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Основной контент в контейнере
col1, col2 = st.columns([1, 0], gap="small")

with col1:
    st.components.v1.html(html_content, height=2000, scrolling=True)

#Fixed чат на боку (будет всегда видно)
with st.sidebar:
    st.markdown("### 💬 Chat Assistant")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hi! How can I help?"}]
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if user_input := st.chat_input("Type your message..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Здесь подключаешь свой n8n агент
        # response = call_n8n_agent(user_input)
        response = "Спасибо за вопрос! Это демо. Подключи свой n8n агент."
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)