from .utils import process_pdf, process_docx

def summarize_file(file_path):
    extension = file_path.split('.')[-1]
    if extension == 'pdf':
        return process_pdf(file_path)
    elif extension in ['docx', 'txt', 'csv']:
        return process_docx(file_path)
    else:
        return "Tipo de archivo no soportado"