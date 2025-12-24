letter_dict = {
    'a': 0, 
    'b': 0, 
    'c': 0, 
    'd': 0, 
    'e': 0, 
    'f': 0, 
    'g': 0, 
    'h': 0, 
    'i': 0, 
    'j': 0, 
    'k': 0, 
    'l': 0, 
    'm': 0, 
    'n': 0, 
    'o': 0, 
    'p': 0, 
    'q': 0, 
    'r': 0, 
    's': 0, 
    't': 0, 
    'u': 0, 
    'v': 0, 
    'w': 0, 
    'x': 0, 
    'y': 0, 
    'z': 0,
    'æ': 0,
    'â': 0,
    'ê': 0,
    'ë': 0,
    'ô': 0,
}

def sort_on(items):
    return items["num"]

def sort_nbr(char_dict):
    new_sorted_list = []

    for i in char_dict:
        c = i
        num = char_dict[i]
        new_sorted_list.append({'char': c, "num": num})
    return (new_sorted_list)

def count_chars(txt):
    for i in txt:
        if i.isupper():
            i = i.lower()
        if i in letter_dict:
            letter_dict[i] += 1
    return(letter_dict)

def count_words(txt):
    words_split = txt.split()
    return (len(words_split))