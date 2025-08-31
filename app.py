import streamlit as st
from urllib.parse import urlparse, parse_qs
from youtube_chat_chain import build_chain

st.set_page_config(page_title="YouTube Chatbot with RAG", layout="wide")
st.title("🎬 YouTube RAG Chatbot")

# Input video URL
yt_url = st.text_input("Enter YouTube URL", placeholder="https://www.youtube.com/watch?v=T-D1OfcDW1M")

if yt_url:
    # Extract video ID
    video_id = parse_qs(urlparse(yt_url).query).get("v", [None])[0]

    if video_id:
        st.success(f"Loaded video ID: {video_id}")

        # Reset chain when new video is loaded
        if "last_video_id" not in st.session_state or st.session_state.last_video_id != video_id:
            with st.spinner("Building RAG pipeline..."):
                try:
                    st.session_state.chain = build_chain(video_id)
                    st.session_state.last_video_id = video_id   # store current video
                except Exception as e:
                    st.error(f"Error: {e}")

        if "chain" in st.session_state:
            query = st.text_input("Ask a question about this video:")
            if query:
                with st.spinner("Thinking..."):
                    response = st.session_state.chain.invoke(query)
                st.markdown(f"**Answer:** {response}")
    else:
        st.error("Invalid YouTube URL")
