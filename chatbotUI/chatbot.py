import streamlit as st

st.set_page_config("मेरी Book - Book Recommender Bot",layout='wide')
st.title('Welcome to, " मेरी Book! "')
st.caption("Powered by : Devansh Rajani")

with st.container():
    st.markdown("---")
    col1, col2 = st.columns([9,1])
    with col1:
        user_input = st.text_input(label="",placeholder="🔍 Please enter what type of book you want to read today?",label_visibility="collapsed")
    with col2:
        send_button = st.button("➤",use_container_width=True)
