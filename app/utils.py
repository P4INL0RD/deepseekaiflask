import PyPDF2
from docx import Document

def process_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''.join([page.extract_text() for page in reader.pages])
    return text[:500]  # Retorna un resumen de los primeros 500 caracteres

def process_docx(file_path):
    doc = Document(file_path)
    text = '\n'.join([para.text for para in doc.paragraphs])
    return text[:500]  # Retorna un resumen de los primeros 500 caracteres