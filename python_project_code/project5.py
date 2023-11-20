import mysql.connector
import PyPDF2
import re


conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='testdb'
)
cursor = conn.cursor()




pdf_file = r'C:\Users\nevis\OneDrive\Documents\python_projects\content\Five\QandA.pdf' 
pdf_text = ''
with open(pdf_file, 'rb') as file:
    pdf_reader = PyPDF2.PdfFileReader(file)
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        pdf_text += page.extractText()
print(pdf_text)

#question_pattern = r'Chapter (\d+): (.+?)\n(\d+)\. (.+?)\n((?: [a-d]\) .+?\n)+)Answer: ([a-d])\) (.+?)\n'
#question_pattern = r'Chapter (\d+): (.*?)((?:\d+\. Question .*?Answer: [a-d]\) .*?(?=\d+\. Question|$)))'
question_pattern = r'Chapter (\d+): (.*?)((?:\d+\. Question .*?Answer: [a-d]\) .*?(?=\d+\. Question|$)))'

questions = re.findall(question_pattern, pdf_text, re.DOTALL)
print(questions)

for question in questions:
    Subject_Name='Social'
    Chapter_name = question[1].strip()
    question_number = question[2]
    Question_Text = question[3].strip()
    Answer_options = question[4].strip()
    correct_answer = f"{question[6]}) {question[7]}"

    insert_query = '''
        INSERT INTO pdf ((Subject_Name, Question_Text, Answer_options, Chapter_name)
        VALUES (%s, %s, %s, %s)
    '''
    data = (chapter_name, question_text, answer_options, correct_answer)
    cursor.execute(insert_query, data)


conn.commit()
conn.close()