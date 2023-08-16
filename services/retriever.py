import hashlib

from langchain.memory import ConversationBufferMemory
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain

# from langchain.retrievers import (
#     ContextualCompressionRetriever, 
#     TimeWeightedVectorStoreRetriever,
#     ArxivRetriever,
#     AzureCognitiveSearchRetriever,
#     ChatGPTPluginRetriever,
#     ElasticSearchBM25Retriever,
#     KNNRetriever,
#     MetalRetriever,
#     PineconeHybridSearchRetriever,
#     PubMedRetriever,
#     SVMRetriever,
#     TFIDFRetriever,
#     WikipediaRetriever,
#     ZepRetriever      
    
# )


def create_agent(llm, retriever, chain_type='stuff', document: str = None):
    
    
    try:

        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        
        
        print(f'llm: {llm}')
        print(f'retriever: {retriever}')
        print(f'chain_type: {chain_type}')
        
        
        qa = ConversationalRetrievalChain.from_llm(llm=llm, chain_type=chain_type, retriever=retriever, memory=memory)    

        id = hashlib.md5(document.encode()).hexdigest()
        return qa, id
    except Exception as e:
        print(e)
        return None, None