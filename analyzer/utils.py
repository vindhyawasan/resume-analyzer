from pypdf import PdfReader
from docx import Document

def extract_text_from_pdf(file):

    #pdf file
    if file.name.lower().endswith(".pdf"):
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

        return text


    #docx file
    elif file.name.lower().endswith(".docx"):

        document = Document(file)
        text=""

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

        return text

    return None