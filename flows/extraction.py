from langchain.chains import create_extraction_chain, create_extraction_chain_pydantic
from langchain.chains import create_tagging_chain, create_tagging_chain_pydantic
from services.llm import load_llm
from langchain.chat_models import ChatOpenAI
ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

test_schema = {
    "properties": {
        "name": {"type": "string"},
        "height": {"type": "integer"},
        "hair_color": {"type": "string"},
    },
    "required": ["name", "height"],
}


def extractflow(schema: dict, llm: str, text: str):    
    model = load_llm(llm)    
    chain =  create_extraction_chain(test_schema, model)
    chain.run(text)
    