import sys
import nltk
import morfeusz2
from nltk.tokenize import word_tokenize
from nltk.text import Text
# nltk.download('punkt')


def adjust_tokens(tokens):
    adjusted_tokens = []
    for token in tokens:
        if token in ",.!?;:" and adjusted_tokens:
            adjusted_tokens[-1] += token
        else:
            adjusted_tokens.append(token)
    return adjusted_tokens


def symmetric_kwic(keyword, filepath, param, total_width=33):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    tokens = word_tokenize(text)
    adjusted_tokens = adjust_tokens(tokens)

    flag = True if param == 'odmien' else False

    if flag:
        keywords = get_inflected_forms(keyword)
    else:
        keywords = {keyword}

    center_length = max(len(kw) for kw in keywords)

    for i, token in enumerate(adjusted_tokens):
        for kw in keywords:
            if kw.lower() == token.lower():
                # Adjust start and end indices to limit the context to max_context_width
                left_index = max(0, i - total_width)
                right_index = min(len(adjusted_tokens), i + total_width + 1)

                left_context_tokens = adjusted_tokens[left_index:i]
                right_context_tokens = adjusted_tokens[i + 1:right_index]

                # Join the tokens to form the left and right context strings
                left_context = ' '.join(left_context_tokens)
                right_context = ' '.join(right_context_tokens)

                # Ensure the left context is trimmed to fit the max_context_width
                if len(left_context) > total_width:
                    left_context = left_context[-total_width:]

                # Ensure the right context is trimmed to fit the max_context_width
                if len(right_context) > total_width:
                    right_context = right_context[:total_width]

                line = f'{left_context} {token + " " * (center_length - len(token))} {right_context}'
                print(line.center(total_width))
                break


def get_inflected_forms(word):
    m = morfeusz2.Morfeusz()
    return [var for var, *_ in m.generate(word)]


if __name__ == "__main__":
    keyword = sys.argv[1]
    multiple_forms = sys.argv[2]
    files = sys.argv[3:]
    for file in files:
        print(file)
        symmetric_kwic(keyword, file, multiple_forms)
