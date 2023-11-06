# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 00:04:25 2023

@author: nevis
"""

import PyPDF2
import os


def read_pdf_with_page(read_path,read_mode,page):
    
    file_obj=open(read_path,read_mode)
    
    pdfReader = PyPDF2.PdfReader(file_obj)

    pageObj = pdfReader.getPage(page)
   # pageObj = pdfReader.pages[page]

    text=pageObj.extract_text()
    file_obj.close()
    
    return text

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
        read_path=r'C:\Users\nevis\OneDrive\Documents\python_projects\content\sample_multi_pages.pdf'
        read_mode='rb'
        write_path=r'C:\Users\nevis\OneDrive\Documents\python_projects\content\output.txt'
        write_mode="w"
        page=int(input("Enter the page number:"))
        text=read_pdf_with_page(read_path,read_mode,page)
        write_to_txt_file(write_path,write_mode,text)
    except:
        print("exception")