
from langchain.llms import (
    Cohere,
    GPT4All, 
    LlamaCpp,
    OpenAI,
    AzureOpenAI,
    CTransformers,
    Bedrock,
    VertexAI
)

from langchain import HuggingFacePipeline
from langchain import HuggingFaceHub

# def load_llm(name, **kwargs):
#     match name:
#         case "ctransformers":
#             llm_cls = CTransformers(model="marella/gpt-2-ggml")
#         case "openai":
#             llm_cls = OpenAI(openai_api_key="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")
#         case "gpt4all":
#             llm_cls = GPT4All(model="marella/gpt-2-ggml")
#         case "llama":
#             llm_cls = LlamaCpp(**kwargs)
#         case "azure":
#             llm_cls = AzureOpenAI(**kwargs)
#         case "cohere":
#             llm_cls = Cohere(**kwargs)
#         case "bedrock":
#             llm_cls = Bedrock(**kwargs)
#         case "vertexai":
#             llm_cls = VertexAI(**kwargs)
#         case _:
#             llm_cls = CTransformers(model="marella/gpt-2-ggml")
    
#     llm = llm_cls
#     return llm


def load_llm(name, **kwargs):
    class_map = {
        "ctransformers": lambda: CTransformers(model="marella/gpt-2-ggml"),
        "openai": lambda: OpenAI(openai_api_key="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"),
        "gpt4all": lambda: GPT4All(model="marella/gpt-2-ggml"),
        "llama": lambda: LlamaCpp(**kwargs),
        "azure": lambda: AzureOpenAI(**kwargs),
        "cohere": lambda: Cohere(**kwargs),
        "bedrock": lambda: Bedrock(**kwargs),
        "vertexai": lambda: VertexAI(**kwargs)
    }

    llm_cls = class_map.get(name, lambda: CTransformers(model="marella/gpt-2-ggml"))
    llm = llm_cls()
    return llm

