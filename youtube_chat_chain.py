from langchain_openai import ChatOpenAI
from youtube_transcript_api import YouTubeTranscriptApi , TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel , RunnablePassthrough , RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


def get_transcript_text(video_id):
    ytt_api = YouTubeTranscriptApi()
    try:
        transcripts_list=ytt_api.list(video_id=video_id)
        transcript = transcripts_list.find_transcript(['en'])
        fetched = transcript.fetch()
        return " ".join([s.text for s in fetched.snippets])
    except TranscriptsDisabled:
        return ""
    

def build_chain(video_id):
    transcript_text= get_transcript_text(video_id=video_id)
    if not transcript_text:
        raise ValueError("Transcription not available for this Video")
    
    #split
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000 , chunk_overlap = 100)
    chunks = splitter.create_documents([transcript_text])
    
    #embeddig and store
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(chunks , embedding=embeddings)
    retriever = vector_store.as_retriever(search_type = "similarity" , search_kwargs = {'k' : 4})
    
    #Prompt
    prompt = PromptTemplate(
        template='''You are a helpful assistant.
        Use only the Provided transcript context to answer.
        If the context is insufficient , reply: "i don't know".
        Context:
        {context}
        
        Question 
        {query}
        ''',
        input_variables=["context" , "query"]
    )
    
    def format_doc(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    parallel_chain = RunnableParallel(
       {
           "context" : retriever | RunnableLambda(format_doc),
           "query" : RunnablePassthrough()
           
       }
    )
    
    load_dotenv()
    llm = ChatOpenAI(
        model="gpt-oss-120b",
        base_url="https://api.cerebras.ai/v1",
    )
    
    parser = StrOutputParser()
    main_chain = parallel_chain | prompt | llm | parser
    return main_chain
    
        