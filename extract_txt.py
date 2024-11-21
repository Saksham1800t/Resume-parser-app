from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import TextConverter
from docx import Document
import os
import io

def extract_text_from_pdf(pdf_path):
    """
    This function returns a text from a PDF file.
    :param pdf_path: path for the PDF file
    :return: text
    """
    r_manager = PDFResourceManager()
    output = io.StringIO()
    converter = TextConverter(r_manager, output, laparams=LAParams())
    p_interpreter = PDFPageInterpreter(r_manager, converter)

    with open(pdf_path, 'rb') as file:
        for page in PDFPage.get_pages(file, caching=True, check_extractable=True):
            p_interpreter.process_page(page)
            text = output.getvalue()
        
    converter.close()
    output.close()

    return text


def extract_text_from_docx(docx_path):
    """
    This function returns a text from a DOCX file.
    :param docx_path: path for the DOCX file
    :return: text
    """
    doc = Document(docx_path)
    text = "\n".join(paragraph.text for paragraph in doc.paragraphs)
    return text


def extract_text_from_doc(doc_path):
    """
    This function extracts text from a DOC file (older Word format).
    :param doc_path: path for the DOC file
    :return: text
    """
    try:
        import win32com.client
        word = win32com.client.Dispatch("Word.Application")
        doc = word.Documents.Open(doc_path)
        text = doc.Content.Text
        doc.Close()
        word.Quit()
        return text
    except Exception as e:
        print(f"Error reading .doc file: {doc_path}. Error: {e}")
        return ""


def read_files(file_path):
    """
    This function returns a list of texts from multiple files.
    :param file_path: path for the directory that contains multiple PDF, DOCX, and DOC files
    :return: list of texts
    """
    fileTXT = []

    for filename in os.listdir(file_path):
        if filename.endswith(".pdf"):
            try:
                fileTXT.append(extract_text_from_pdf(os.path.join(file_path, filename)))
            except Exception:
                print("Error reading PDF file: " + filename)
        
        elif filename.endswith(".docx"):
            try:
                fileTXT.append(extract_text_from_docx(os.path.join(file_path, filename)))
            except Exception:
                print("Error reading DOCX file: " + filename)

        elif filename.endswith(".doc"):
            try:
                fileTXT.append(extract_text_from_doc(os.path.join(file_path, filename)))
            except Exception:
                print("Error reading DOC file: " + filename)
    
    return fileTXT


if __name__ == "__main__":
    txt = read_files("/home/ayoub/DS/Parser-Shortlisting-Project/files/resumes")
    print(txt)
