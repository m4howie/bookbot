from stats import get_words, count_letters,sort_on, sorted_count_letters

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents




def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path} ...")
    print("........... Word Count ...........")
    print(f"Found {get_words(text)} total words")
    print("......... Character Count .........")
    letters = count_letters(text)
    sorted_letters = sorted_count_letters(letters)
    for d_letter in sorted_letters:
        print(f"{d_letter["char"]}: {d_letter["num"]}")
    print("========== END ==========")


main()
