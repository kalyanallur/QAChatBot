import streamlit as st
from get_text import FileReader
from src.Logging import logging 
from src.Exceptions import CustomExceptions
from Process import Splitter

st.title("🤖 ChatBot")
upload_Files = st.sidebar.file_uploader("Upload_Files", type=['txt', 'docx', 'pdf'], accept_multiple_files=True, label_visibility="visible")
filetype = st.sidebar.radio("Please select file Type",["PDF","DOCX","TXT"])
text_data = st.sidebar.text_input("Upload text", disabled=bool(upload_Files))
button = st.sidebar.button("Load Data")
if button:
    complete_data = ""
    for path in upload_Files:
        file_reader_obj = FileReader()
        complete_data += file_reader_obj.read_file(path, filetype)
        
    text_splitter_obj = Splitter()
    chunk_data = text_splitter_obj.split(complete_data)
    st.write(chunk_data)
