from stats import get_words, count_letters

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents
def main ():
    contents = get_book_text("books/frankenstein.txt")
    word_count = get_words(contents)
    print(f"{word_count} words found in the document")
    print(count_letters(contents))

main()
