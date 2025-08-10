import pdfplumber

def extract_tables(file_path):
    """Extract tables from the PDF file using pdfplumber. Returns a list of tables per page."""
    tables = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_tables = page.extract_tables()
            for table in page_tables:
                # Clean each cell in the table
                cleaned_table = [[" ".join(str(cell).split()) if cell else "" for cell in row] for row in table]
                tables.append(cleaned_table)
    return tables

def extract_text_pdf(file_path: str) -> str:
    """Extract text from the PDF file using pdfplumber."""
    text = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                cleaned = " ".join(page_text.split())
                text.append(cleaned)
    return "\n".join(text)