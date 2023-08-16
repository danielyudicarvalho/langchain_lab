import os
import glob
from dotenv import load_dotenv

from langchain.vectorstores import (
    AnalyticDB,
    Annoy,
    AtlasDB,
    AwaDB,
    Chroma,
    Clickhouse,
    ClickhouseSettings,
    DeepLake,
    DocArrayHnswSearch,
    DocArrayInMemorySearch,
    ElasticVectorSearch,
    FAISS,
    LanceDB,
    MatchingEngine,
    Milvus,
    MongoDBAtlasVectorSearch,
    MyScale,
    OpenSearchVectorSearch,
    SingleStoreDB,
    SKLearnVectorStore,
    Pinecone,
    Qdrant,
    SupabaseVectorStore,
    Tair,
    Tigris,
    Typesense,
    Vectara,
    Weaviate
)


load_dotenv()

from langchain.vectorstores.redis import Redis

        
def load_vector_store(vector_store_name, docs, embedder=None):
    vector_stores = {
        "analyticdb": lambda : AnalyticDB.from_documents(docs, embedding=embedder).as_retriever(),
        "annoy": lambda: Annoy.from_documents(docs, embedding=embedder).as_retriever(),
        "atlasdb": lambda : AtlasDB.from_documents(docs, embedding=embedder).as_retriever(),
        "awadb": lambda : AwaDB.from_documents(docs, embedding=embedder).as_retriever(),
        "chroma": lambda: Chroma.from_documents(docs, embedding=embedder).as_retriever(),
        "clickhouse": lambda: Clickhouse.from_documents(docs, embedding=embedder).as_retriever(),
        "deeplake": lambda: DeepLake.from_documents(docs, embedding=embedder).as_retriever(),
        "docarrayhnswsearch": lambda : DocArrayHnswSearch.from_documents(docs, embedding=embedder).as_retriever(),
        "docarrayinmemorysearch": lambda: DocArrayInMemorySearch.from_documents(docs, embedding=embedder).as_retriever(),
        "elasticvectorsearch": lambda: ElasticVectorSearch.from_documents(docs, embedding=embedder).as_retriever(),
        "faiss": lambda: FAISS.from_documents(docs, embedding=embedder).as_retriever(),
        "lancedb": lambda: LanceDB.from_documents(docs, embedding=embedder).as_retriever(),
        "matchingengine": lambda: MatchingEngine.from_documents(docs, embedding=embedder).as_retriever(),
        "milvus": lambda: Milvus.from_documents(docs, embedding=embedder).as_retriever()
    }

    return vector_stores.get(vector_store_name, lambda: Chroma.from_documents(docs, embedding=embedder).as_retriever())()        