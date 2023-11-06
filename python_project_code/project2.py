# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 23:12:47 2023

@author: nevis
"""

import PyPDF2
import os


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
            for a,b,c in os.walk(r'C:\Users\nevis\OneDrive\Documents\python_projects\content'):
                 print(c)
             
                 for i in c:
                     
                     if '.pdf' in i:
                         path=os.path.join(a, i)
                         write_path=(os.path.dirname(path)+'\output.txt')
                         text=read_pdf(path,'rb')
                         write_to_txt_file(write_path,'a',text)
   except:
           print("exception")
    
    