# YouTube RAG Chatbot

An interactive AI-powered chatbot built with LLMs and LangChain.
This project allows users to input a YouTube video link, automatically extract its transcript, and then chat with the content.
The chatbot provides context-aware answers based on the video, making it easy to query long videos without watching everything manually.

# Features

🔗 YouTube Integration – Paste a YouTube video link to extract its transcript.

🧠 LLM + LangChain – Uses a Retrieval-Augmented Generation (RAG) pipeline for accurate, grounded answers.

💬 Chat Interface – Ask natural language questions about the video.

⚡ Efficient Context Handling – Splits transcripts into chunks and retrieves only the most relevant parts.

🎨 Streamlit Frontend – Simple and interactive UI for chatting with your video.

🛠️ Tech Stack

Language: Python

Frameworks: LangChain, Streamlit

LLM Models: OpenAI GPT / Hugging Face Models

Other Tools: YouTube Transcript API, FAISS Vector DB

📂 Project Structure
youtube-rag-chatbot/
│
├── app.py                # Main Streamlit app
├── youtube_chat_chain.py # RAG pipeline with LangChain
├── requirements.txt      # Dependencies
├── README.md             # Project documentation


⚙️ Installation & Setup

Clone the repo:

git clone [https://github.com/zyrogX/Youtube_chatbot.git](https://github.com/zyrogX/Youtube_chatbot.git)
cd youtube-rag-chatbot


Create a virtual environment & install dependencies:

pip install -r requirements.txt


Set your OpenAI API Key (or Hugging Face key):

export OPENAI_API_KEY="your_api_key_here"


Run the Streamlit app:

streamlit run app.py

📸 Demo

(Add screenshots of your app UI or a short GIF here)

Example workflow:

Paste YouTube video link

Ask: “Summarize this video in 3 bullet points.”

Ask: “What does the speaker say about AI automation?”

🔮 Future Improvements

Support for multi-video conversations

Adding speech-to-text for videos without transcripts

Fine-tuned LLMs for domain-specific video Q&A

🧑‍💻 Author

Muhammad Iftikhar

GitHub: zyrogX

LinkedIn: zyrog
