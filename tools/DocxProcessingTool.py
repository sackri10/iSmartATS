from docx import Document

def extract_text_docx(file_path: str) -> str:
    """Extract and clean text from a DOCX file using python-docx."""
    doc = Document(file_path)
    text = []
    for para in doc.paragraphs:
        para_text = para.text
        if para_text:
            cleaned = " ".join(para_text.split())
            if cleaned:
                text.append(cleaned)
    return "\n".join(text)
