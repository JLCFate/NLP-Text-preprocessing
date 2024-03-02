import pdfplumber


def extract_text(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    return text


pdf_path = 'D19640296Lj.pdf'
extracted_text = extract_text(pdf_path)
with open('kodeks.txt', 'w') as file:
    file.write(extracted_text)