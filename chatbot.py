import streamlit as st
from vector_store.searching import search_books, generate_llm_response

st.set_page_config("मेरी Book - Book Recommender Bot", layout='wide')
st.title('Welcome to, " मेरी Book! "')
st.caption("Powered by : Devansh Rajani")

with st.container():
    st.markdown("---")
    col1, col2 = st.columns([9, 1])
    with col1:
        user_input = st.text_input(
            label="", 
            placeholder="🔍 What type of book would you like to read today?", 
            label_visibility="collapsed"
        )
    with col2:
        send_button = st.button("➤", use_container_width=False)

# Initialize session history
if "history" not in st.session_state:
    st.session_state.history = []

# On send
if send_button and user_input:
    with st.spinner("Great! Let me think..."):
        matched_books = search_books(user_input)
        response = generate_llm_response(user_input, matched_books)

        st.session_state.history.append({"role": "user", "content": user_input})
        st.session_state.history.append({"role": "bot", "content": response})

# Display conversation
for msg in st.session_state.history:
    if msg["role"] == "user":
        st.markdown(
            f"""
            <div style="background-color:#cce5ff; padding: 15px; border-radius: 10px; margin:10px 0;">
                <span style="color:#003366; font-weight:bold;">🧑 You:</span><br>
                <span style="color:#003366;">{msg['content']}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="background-color:#f2f2f2; padding: 15px; border-radius: 10px; margin:10px 0; border-left: 5px solid #007acc;">
                <span style="color:#1a1a1a; font-weight:bold;">🤖 Book Bot:</span><br>
                <span style="color:#1a1a1a;">{msg['content']}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
