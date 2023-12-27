from src.Logging import logging
from src.Exceptions import CustomExceptions
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import faiss

class Splitter:
    def __init__(self):
        pass


    def split(self,text_data):
        try: 
            splitter = RecursiveCharacterTextSplitter(chunk_size = 800, chunk_overlap  = 50, length_function = len)
            data_chunks = splitter.split_text(text_data)
            logging.info("Text splitted successfully")
            return data_chunks
        
        except Exception as e :
            raise CustomExceptions(e)
    


class Embeddings:
    def __init__(self) :
        pass


    def create_embeddings(self, data_chunks):
        try:
            embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})
            vector_db =faiss.FAISS.from_texts(data_chunks,embeddings)
            return vector_db
        
        except Exception as e :
            raise CustomExceptions(e)
    
a = Splitter()
b = a.split_text("""hfsfjfnfnjscnjnjn cnshncfhsjjjjjjjjjjjjjjjjjjjjjjjjjjjj sjds
                 

         ejjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjllllllllllllllllllllllllllllllll skkkkkkkkkk
             sssssssssssssssssssssssssssssssss
             tttttttttttttttttttttttttttttttttttt
             tttttttttttttttttttttttttttttttttttttttttttt
             ttttttttttttttttttttttttttttttttttttttt    """)
print(b)