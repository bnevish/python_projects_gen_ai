# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:21:53 2023

@author: nevis
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 00:04:25 2023

@author: nevis
"""

import PyPDF2
import os
import configparser
import re

config = configparser.ConfigParser()
config.read(r'C:\Users\nevis\OneDrive\Documents\python_projects\config.txt')   

reg_exp=config.get('global', 'regex_exp') 

def extract_content_after_heading(pdf_path, heading_pattern):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.numPages

        heading_content = []
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            page_text = page.extractText()

           
            matches = re.findall(heading_pattern + r'(.*?)((?=\n\n)|(?=\n[^\n]))', page_text, re.DOTALL)
            if matches:
                for match in matches:
                    heading_content.append(match[0].strip())

    return heading_content

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
    
   # try:
        
        pdf_path=r'C:\Users\nevis\OneDrive\Documents\python_projects\content\four\regex_file.pdf'
        heading_pattern = r'Section 1: Formatting Requirements for Headings and Chapters/Sections'
        text=extract_content_after_heading(pdf_path, heading_pattern)
        print(text)
        write_path=r'C:\Users\nevis\OneDrive\Documents\python_projects\content\four\output.txt'
        write_mode="w"
        write_to_txt_file(write_path,write_mode,text)
   # except:
        #print("exception")
