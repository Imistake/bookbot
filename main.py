import sys
from stats import character_count
from stats import chars_dict_to_sorted_list
from stats import word_count

if len(sys.argv) != 2:
   print("Usage: python3 main.py <path_to_book>")
   sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
  book_path = sys.argv[1]
  book_text = get_book_text(book_path)
  
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")

  print("----------- Word Count ----------")
  word_count_result = word_count(book_text)
  print(f"Found {word_count_result} total words")
  
  print("--------- Character Count -------")
  char_count = character_count(book_text)
  sorted_chars = chars_dict_to_sorted_list(char_count)

  for char_dict in sorted_chars:
     char = char_dict["char"]
     count = char_dict["count"]
     if char.isalpha():
        print(f"{char}: {count}")

  print("============= END ===============")




main()
