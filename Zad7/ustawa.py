#!/usr/bin/python3
import pdfplumber
import re

content_area = (0, 0, 450, 842)


def get_main_content_text(page):
    words = page.extract_words()

    filtered_words = [
        word for word in words
        if content_area[0] <= word['x0'] <= content_area[2] and content_area[1] <= word['top'] <= content_area[3]
    ]

    # Combine the text of the filtered words
    text = ' '.join(word['text'] for word in filtered_words)
    return text


def print_chapters(filename):
    """
    Print chapters in a PDF file (in Polish).
    :param filename: PDF file name
    :return: nothing
    Processing is simplified. The file may contain no chapters.
    """
    found = False
    with pdfplumber.open(filename) as pdf:

        page_number = 1
        t = pdf.pages[0].extract_text() if found else get_main_content_text(pdf.pages[0])
        if not found:
            pattern = r"(USTAWA.*?)TYTUŁ WSTĘPNY"
            match = re.search(pattern, t, re.DOTALL)
            if match:
                print(match[1])
                found = True

        for p in pdf.pages:
            t = p.extract_text()
            for r in re.findall(r'^(Rozdział|Tytuł|Część|Księga|Dział|Oddział)\W(\w*)', t,
                                re.IGNORECASE | re.MULTILINE):
                if r[0][0].isupper():
                    print(r[0], r[1], 'strona', page_number)
            page_number = page_number + 1


if (__name__ == "__main__"):
    import sys

    for filename in sys.argv[1:]:
        print(filename)
        print_chapters(filename)