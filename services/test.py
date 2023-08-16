
import os
from pathlib import Path

from langchain.embeddings.openai import OpenAIEmbeddings
# import
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.document_loaders import WebBaseLoader
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import AzureOpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.tools import BaseTool
from langchain.llms import OpenAI
from langchain import LLMMathChain, SerpAPIWrapper
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

# 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

os.environ['OPENAI_API_KEY'] = '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'

print('1')
# Create instance of OpenAI LLM
llm = OpenAI(temperature=0.1, verbose=True)

loader = TextLoader("test.txt")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(documents)


print('2')
store = Chroma.from_documents(documents, collection_name='user_book')

# state_of_union = RetrievalQA.from_chain_type(
#     llm=llm, chain_type="stuff", retriever=store.as_retriever()
# )

# loader = WebBaseLoader("https://beta.ruff.rs/docs/faq/")

# docs = loader.load()
# ruff_texts = text_splitter.split_documents(docs)
# ruff_db = Chroma.from_documents(ruff_texts, collection_name="ruff")
# ruff = RetrievalQA.from_chain_type(
#     llm=llm, chain_type="stuff", retriever=ruff_db.as_retriever()
# )

print('3')
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
qa = ConversationalRetrievalChain.from_llm(llm=llm, chain_type='stuff', retriever=store.as_retriever(), memory=memory)   

# tools = [
#     Tool(
#         name="State of Union QA System",
#         func=state_of_union.run,
#         description="Util para perguntas sobre esploração espacial",
#     )
# ]

# # Construct the agent. We will use the default agent type here.
# # See documentation for a full list of options.
# agent = initialize_agent(
#     tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
# )

# response = agent.run(
#     "O que é esploração espacial?"
# )
# print(response)
