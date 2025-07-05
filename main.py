from stats import get_num_words
from stats import count_letters
def main():
    path = "/home/m4howie/bookbot/books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    book_dict = count_letters(text)
    print(f"{num_words} words found in the document", book_dict)



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()


