from stats import get_num_words, get_num_characters, list_sorting
import sys


def get_book_text(path_to_file):   
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    char_count = get_num_characters(text)
    new_list = list_sorting(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in new_list:
        ch = entry["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {entry['num']}")
    print("============= END ===============")   

main()

