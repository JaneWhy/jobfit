from docx import Document
from pypdf import PdfReader


def extract_text_from_pdf(file) -> str:
    reader = PdfReader(file)
    texts = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            texts.append(text)
    return "\n".join(texts)


def extract_text_from_docx(file) -> str:
    doc = Document(file)
    texts = []
    for para in doc.paragraphs:
        texts.append(para.text)
    return "\n".join(texts)


def extract_resume_text(file) -> str:
    filename = file.name.lower()

    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file)
    if filename.endswith(".docx"):
        return extract_text_from_docx(file)
    raise ValueError("暂不支持该文件格式，请上传 PDF 或 DOCX 文件。")
