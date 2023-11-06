# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 14:10:05 2023

@author: nevish
"""

import PyPDF2


def read_pdf(read_path,read_mode):
    
    file_obj=open(read_path,read_mode)

    pdfReader = PyPDF2.PdfReader(file_obj)

    pageObj = pdfReader.pages[0]

    text=pageObj.extract_text()
    
    file_obj.close()
    
    return text

def write_to_txt_file(write_path,write_mode,text):
    
    file1=open(write_path,write_mode)

    file1.writelines(text)

    file1.close()
    
if __name__=="__main__":
    
    try:
        read_path=r'C:\Users\nevis\OneDrive\Documents\python_projects\content\sample_file.pdf'
        read_mode='rb'
        write_path=r'C:\Users\nevis\OneDrive\Documents\python_projects\content\output.txt'
        write_mode="a"
        text=read_pdf(read_path,read_mode)
        write_to_txt_file(write_path,write_mode,text)
    except:
        print("exception")
    
    