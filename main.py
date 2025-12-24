from stats import count_words, count_chars, sort_nbr, sort_on

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return (file_contents)

def main():
    char_count = []
    new_sorted_list = []
    txt = get_book_text("books/frankenstein.txt")
    total_words = count_words(txt)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found", total_words, "total words")
    print("--------- Character Count -------")

    char_count = count_chars(txt)
    new_sorted_list = sort_nbr(char_count)
    new_sorted_list.sort(reverse=True, key=sort_on)

    for i in new_sorted_list:
        print(f"{i["char"]}: {i["num"]}")


if __name__=="__main__":
    main()
