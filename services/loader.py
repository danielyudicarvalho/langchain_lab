import sys
import os

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import (
    UnstructuredHTMLLoader, 
    WikipediaLoader,
    TwitterTweetLoader,
    TrelloLoader,
    UnstructuredPowerPointLoader,
    JSONLoader, 
    UnstructuredMarkdownLoader, 
    PyPDFLoader, 
    TextLoader, 
    Docx2txtLoader,
    CSVLoader, 
    WebBaseLoader)



def loader(filename, *args):
    
    _, extension = os.path.splitext(filename)
    
    tool  =  args[0]

    loaders = {
        ".html": UnstructuredHTMLLoader,
        ".pdf": PyPDFLoader,
        ".txt": TextLoader,
        ".csv": CSVLoader,
        ".json": JSONLoader,
        ".md": UnstructuredMarkdownLoader,
        ".docx": Docx2txtLoader,
        ".com": WebBaseLoader,
        ".pptx": UnstructuredPowerPointLoader
     }

    try:
        loader = loaders[extension](filename)
        return loader.load()
    except KeyError:
        raise IOError(f"File extension {extension} is not supported")
    


if __name__ == "__main__":
    
    input_file = sys.argv[1]
        
    print(loader(input_file))