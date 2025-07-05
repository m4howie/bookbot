def get_num_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    book_dict = {}
    text = text.lower()
    for letters in text:
        if letters in book_dict:
            book_dict[letters] += 1
        else:
            book_dict[letters] = 1

    return book_dict
