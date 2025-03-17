import PyPDF2
import docx

def summarize_file(file):
    """Lee el archivo y devuelve un resumen simulado."""
    text = ""
    
    if file.filename.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    elif file.filename.endswith(".docx"):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    elif file.filename.endswith(".txt"):
        text = file.read().decode("utf-8")
    elif file.filename.endswith(".csv"):
        text = file.read().decode("utf-8")
    else:
        return "Formato de archivo no soportado."
    
    summary = f"Resumen del documento ({len(text.split())} palabras): {text[:500]}..."
    return summary
