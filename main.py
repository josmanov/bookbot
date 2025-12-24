from stats import count_words

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return (file_contents)


def main():
    txt = get_book_text("books/frankenstein.txt")
    total_words = count_words(txt)
    print("Found", total_words, "total words")

if __name__=="__main__":
    main()
