import os
from dotenv import load_dotenv

from langchain.embeddings import (
    AlephAlphaAsymmetricSemanticEmbedding,
    OpenAIEmbeddings,
    BedrockEmbeddings,
    CohereEmbeddings,
    DeepInfraEmbeddings,
    ElasticsearchEmbeddings,
    FakeEmbeddings,
    VertexAIEmbeddings,
    HuggingFaceEmbeddings,
    SentenceTransformerEmbeddings,
    HuggingFaceInstructEmbeddings,
    JinaEmbeddings,
    LlamaCppEmbeddings,
    MiniMaxEmbeddings,
    ModelScopeEmbeddings,
    MosaicMLInstructorEmbeddings,
    OpenAIEmbeddings,
    SagemakerEndpointEmbeddings,
    TensorflowHubEmbeddings
       )

load_dotenv()

KEY1 = os.getenv('KEY1')
def load_embeddings(name):
    embedders = {
        "aleph": AlephAlphaAsymmetricSemanticEmbedding(normalize=True, compress_to_size=128),
        "openai": OpenAIEmbeddings(),
        "hugginface": HuggingFaceEmbeddings(model_name="krlvi/sentence-t5-base-nlpl-code-x-glue"),
        "tensorflow": TensorflowHubEmbeddings(),
        "befrock": BedrockEmbeddings(),
        "cohere": CohereEmbeddings(),
        "deepinfra": DeepInfraEmbeddings(),
        "elasticsearch": ElasticsearchEmbeddings(),
        "llamacpp": LlamaCppEmbeddings(),
        "minimax": MiniMaxEmbeddings(),
        "modescope": ModelScopeEmbeddings(),
        "mosaic": MosaicMLInstructorEmbeddings(),
        "sagemaker": SagemakerEndpointEmbeddings(),
        "default": FakeEmbeddings(size=1352)
    }

    return embedders.get(name, embedders["default"])