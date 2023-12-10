# !pip install PyPDF2
# importing required modules
from PyPDF2 import PdfReader
import os
from .cleantxt import cleantext
import time

def pdf2txt(file_path, output_path, file_name):
    file_path = file_path + file_name
    # creating a pdf reader object
    reader = PdfReader(file_path)
    text = ''
    for page in reader.pages:
        txt = page.extract_text()
        text = text + txt
    
    # clean the text
    text = cleantext(text)
    
    today = time.strftime("%Y%m%d")
    output_path = output_path + today + '/'
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    # save text to file
    # remove the ".pdf" suffix
    with open(output_path+file_name[:-4] + '.txt', 'w') as f:
        f.write(text)
        f.close()

    return text

def pdfs2txt(file_path, output_path):
    # get all the pdf files in the folder if their filenames end with ".pdf"
    files = [f for f in os.listdir(file_path) if f.endswith('.pdf')]

    for file in files:
        pdf2txt(file_path, output_path, file)
    
    print('All pdf files have been converted to txt files.')
    return None

if __name__ == '__main__':
    file_path = 'data/'
    output_path = 'output/'
    pdf2txt(file_path, output_path, 'sed_wos_12')
