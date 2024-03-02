import pdfplumber

def extract_text(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    return text

pdf_path = 'Texts/D19640296Lj.pdf'
extracted_text = extract_text(pdf_path)

# Zapisz tekst do pliku z obsługą kodowania UTF-8
with open('Texts/kodeks.txt', 'w', encoding='utf-8') as file:
    file.write(extracted_text)
