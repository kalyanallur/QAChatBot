from src.Logging import logging
from src.Exceptions import CustomExceptions
import docx
import PyPDF2

class FileReader:
    def __init__(self):
        pass
        

    def read_file(self,file_path, file_type):
        try:
            if file_type=="TXT":
                file_content = file_path.read()
                text = file_content.decode("utf-8")
                logging.info("Text extracted successfully")
                return text
            
            elif file_type=="DOCX":
                doc = docx.Document(file_path)
                text = ""
                for para in doc.paragraphs:
                    text+=para.text +"\n"
                logging.info("Text extracted successfully")
                return text
            
            else:
                doc = PyPDF2.PdfReader(file_path)
                text = ""
                for page in doc.pages:
                    data = page.extract_text().encode('utf-8')   
                    text += data.decode("utf-8")
                logging.info("Text extracted successfully")
                return text
            
        except Exception as e:
            raise CustomExceptions(e)