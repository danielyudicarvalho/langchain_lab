from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain
from services.ingest import load_single_document, load_single_document_without_vectordb
from services.llm import load_llm

loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
docs = loader.load()

def summarizeflow(doc, llm, chain_type="stuff"):
    
    docs = load_single_document_without_vectordb(doc)
    llm = load_llm(llm)    
    chain = load_summarize_chain(llm, chain_type=chain_type)

    response = chain.run(docs)
    return response
    