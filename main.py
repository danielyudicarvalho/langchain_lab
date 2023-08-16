import os
from dotenv import load_dotenv
from services.ingest import load_single_document, load_single_document_without_vectordb
from services.retriever import create_agent
from services.llm import load_llm
from flows.summarazation import summarizeflow
from flows.extraction import extractflow  
from fastapi import FastAPI, HTTPException, UploadFile, File
from langchain.llms import OpenAI


UPLOAD_DIRECTORY = "uploads"

# Create the directory if it doesn't exist
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

app = FastAPI()
app.chat_ids = {}
app.chats = {}
app.retrievers = {}
app.schema = {
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "address": {"type": "string"},
        "cpf": {"type": "string"},
        "status": {"type": "string"},
        "email": {"type": "string"},
        "phone": {"type": "integer"},
        "gender": {"type": "string"},
    },
    "required": ["name", "age", "cpf", "email", "phone", "address", "gender"],
}

  
@app.post("/upload/{embedding_type}")
async def upload_file(file: UploadFile = File(...), embedding_type: str="glove", vectordb: str="glove"):
    try:
        file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)

        # Save the file to the server
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        # Process the file
        app.retrievers[file.filename] = load_single_document(file_path, embedding_type, vectordb)

        return {"filename": file.filename}
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    
    
@app.post("/create_agent/")
async def create_agents(document: str, chain_type: str="stuff", llm="openai"):    
    
    llm = load_llm(llm)
    retriever = app.retrievers[document]
    agent, id = create_agent(llm,retriever, chain_type, document)    
    app.chats[id] = agent
    app.chat_ids[document] = id
    return {"agent_id": id}
     

    
@app.post("/chat/{agent_id}")
async def chat(agent_id: str="glove", user_message: str="Hello World", embedding_type: str="glove"):
    agent = app.chats.get(agent_id, None)
    if agent is None:
        return {"message": "Agent not found"}
    
    response = agent.run(user_message)
    print(response)
    
    return response

@app.post("/summarize/")
async def summarize(file: UploadFile = File(...), llm: str="openai", chain_type: str="stuff"):
    try:
        file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)

        # Save the file to the server
        with open(file_path, "wb") as f:
            f.write(file.file.read())

        # Process the file
        response = summarizeflow(file_path, llm, chain_type)
        
        return {"filename": response}
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/extract/")
def extract(llm: str="openai", text: str=""):
    result = extractflow(app.schema, text, llm)
    return result


    
@app.post("/create_schema/")
def create_schema(name: str, type:str):    
    
    app.schema['properties'][name] = {"type":type}   
   
   

@app.get('/schema/') 
def get_schema():
    
    return app.schema 

@app.get('/chats/') 
def get_chats():
    
    return app.chat_ids 

@app.get('/retrievers/') 
def get_retrievers():
    keys =  app.retrievers.keys()
    print(keys)
    
    return keys


