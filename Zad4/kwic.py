import nltk
from nltk.text import Text
# nltk.download('punkt')


def read_txt_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print('File not found')
        return None


def search_with_context(word, width):
    concordance_list = text_obj.concordance_list(word, width=width, lines=5)
    for concordance in concordance_list:
        left = ' '.join(concordance.left)
        right = ' '.join(concordance.right)
        print(f"{left} {concordance.query} {right}")


text = read_txt_from_file('Texts/kodeks.txt')
words = nltk.word_tokenize(text)
text_obj = Text(words)

search_word = "uczestnik"
num_chars = 15
search_with_context(search_word, num_chars)