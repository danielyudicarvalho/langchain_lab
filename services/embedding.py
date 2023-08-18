import os
from dotenv import load_dotenv
from ..utils.keys import load_embeddings_keys 

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
    VertexAIEmbeddings,
    TensorflowHubEmbeddings
       )

load_dotenv()

KEY1 = os.getenv('KEY1')

def load_embeddings(name):
    def aleph():
        return AlephAlphaAsymmetricSemanticEmbedding(normalize=True, compress_to_size=128)
    
    def openai():
        return OpenAIEmbeddings()
    
    def hugginface():
        return HuggingFaceEmbeddings(model_name="krlvi/sentence-t5-base-nlpl-code-x-glue")
    
    def tensorflow():
        return TensorflowHubEmbeddings()
    
    def befrock():
        return BedrockEmbeddings()
    
    def cohere():
        return CohereEmbeddings()
    
    def deepinfra():
        return DeepInfraEmbeddings()
    
    def elasticsearch():
        return ElasticsearchEmbeddings()
    
    def llamaccp():
        return LlamaCppEmbeddings()
    
    def minimax():
        return MiniMaxEmbeddings()
    
    def modescope():
        model_id = "damo/nlp_corom_sentence-embedding_english-base"
        return ModelScopeEmbeddings(model_id=model_id)
    
    def mosaic():
        return MosaicMLInstructorEmbeddings()
    
    def sagemaker():
        return SagemakerEndpointEmbeddings()
    
    def default():
        return FakeEmbeddings(size=1352)
    
    embedders = {
        'aleph': aleph,
        'openai': openai,
        'hugginface': hugginface,
        'tensorflow': tensorflow,
        'befrock': befrock,
        'cohere': cohere,
        'deepinfra': deepinfra,
        'elasticsearch': elasticsearch,
        'llamaccp': llamaccp,
        'minimax': minimax,
        'modescope': modescope,
        'mosaic': mosaic,
        'sagemaker': sagemaker,
        'default': default,
    }
    
    return embedders.get(name, default)()
