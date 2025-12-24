from stats import count_words, count_chars

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return (file_contents)

def main():
    char_count = []
    txt = get_book_text("books/frankenstein.txt")
    total_words = count_words(txt)
    print("Found", total_words, "total_words")
    char_count = count_chars(txt)
    for i in char_count:
        print(f"'{i}': {char_count[i]}")


if __name__=="__main__":
    main()
