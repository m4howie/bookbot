def get_words(contents):
    return len(contents.split())

def count_letters(contents):
    result = {}

    for l in contents:
        l = l.lower()
        if l not in result:
            result[l] = 0
        result[l] += 1
    return result

def sort_on(d):
    return d["num"]


def sorted_count_letters(letters):
    result = []
    for letter in letters:
        if letter.isalpha():
            d = {}
            d["char"] = letter
            d["num"] = letters[letter]
            result.append(d)
    result.sort(reverse=True, key=sort_on)
    return result
