import os
from langchain.docstore.document import Document
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain import HuggingFacePipeline
import transformers
from langchain.chains import ConversationalRetrievalChain

folder_name = "sample_code"
# os.system(f"git clone https://github.com/hwchase17/langchain {folder_name}")

documents = []
for root, dirs, files in os.walk(folder_name):
    for file in files:
        try:
            with open(os.path.join(root, file), "r", encoding="utf-8") as o:
                code = o.readlines()
                d = Document(page_content="\n".join(code), metadata={"source": os.path.join(root, file)})
                documents.append(d)
        except UnicodeDecodeError:
            pass
            # some files are not utf-8 encoded; let's ignore them for now.

hfemb = HuggingFaceEmbeddings(model_name="krlvi/sentence-t5-base-nlpl-code-x-glue")
persist_directory = "db"
db = Chroma.from_documents(documents, hfemb, persist_directory=persist_directory)
db.persist()

db = Chroma(persist_directory=persist_directory, embedding_function=hfemb)

retriever = db.as_retriever()

model_id = "mosaicml/mpt-7b-instruct"
config = transformers.AutoConfig.from_pretrained(model_id, trust_remote_code=True)
tokenizer = transformers.AutoTokenizer.from_pretrained(model_id)
model = transformers.AutoModelForCausalLM.from_pretrained(model_id, config=config, trust_remote_code=True)
pipe = transformers.pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=100)
llm = HuggingFacePipeline(pipeline=pipe)

qa_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, return_source_documents=True)

result = qa_chain({"question": "What is the return type of the create_index function in the KNNRetriever?", "chat_history": []})
print(f"Answer: {result['answer']}")
print(f"Sources: {[x.metadata['source'] for x in result['source_documents']]}")

# #////////////////////////////////////

# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationBufferMemory

# conversation = ConversationChain(
#     llm=llm, 
#     verbose=True, 
#     memory=ConversationBufferMemory()
# )

# conversation.predict(input="Hi there!")
# import os
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "xxxxxxxxxxxxxxxxxxx"
# from langchain import PromptTemplate, HuggingFaceHub, LLMChain
# template = """Question: {question}

# Answer: Let's think step by step."""
# prompt = PromptTemplate(template=template, input_variables=["question"])
# llm=HuggingFaceHub(repo_id="google/flan-t5-xl", model_kwargs={"temperature":1e-10})

# question = "When was Google founded?"

# print(llm_chain.run(question))
