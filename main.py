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

pdf_link = "path_to_your_pdf.pdf"
loader = PyPDFLoader(pdf_link, extract_images=False)
pages = loader.load_and_split()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=4000,
    chunk_overlap=20,
    length_function=len,
    add_start_index=True
)

chunks = text_splitter.split_documents(pages
db = Chroma.from_documents(chunks, embedding=embeddings_model, persist_directory="text_index")
db.persist()
                                       
vectordb = Chroma(persist_directory="text_index", embedding_function=embeddings_model)

retiever = vectordb.as_retriever(search_kwargs={"k": 3})

chain = load_qa_chain(llm, chain_type="stuff")

def ask(question):
    context = retiever.get_relevant_documents(question)
    answer = (chain({"input_documents": context, "question": question}, return_only_outputs=True))['output_text']
    return answer, context

user_question = input("User: ")
answer = ask(user_question)
print("Answer:", answer)
print(context[0])
