from stats import get_num_words
from stats import count_letters
from stats import chars_dict_to_sort_list

def main():
    path = "/home/m4howie/bookbot/books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    book_dict = count_letters(text)
    chars_sorted_list = chars_dict_to_sort_list(book_dict)
    print_report(path, num_words, chars_sorted_list)



def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()


