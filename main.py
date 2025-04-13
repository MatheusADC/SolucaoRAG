from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.chat_models.openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains.question_answering.chain import load_qa_chain
import os
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

embeddings_model = OpenAIEmbeddings()
llm = ChatOpenAI(model="gpt-3.5-turbo", max_tokens=200)
