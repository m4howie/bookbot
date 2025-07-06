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

def sort_on(d):
    return d["num"]

def chars_dict_to_sort_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
