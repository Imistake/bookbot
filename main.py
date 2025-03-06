# Importing sys module to access command-line arguments.
import sys
# Importing functions from the stats module for text analysis.
from stats import character_count
from stats import chars_dict_to_sorted_list
from stats import word_count

# Checking if exactly one command-line argument (the book path) was provided.
# If not, then displaying the usage instructions and exiting the program.
if len(sys.argv) != 2:
   print("Usage: python3 main.py <path_to_book>")
   sys.exit(1)

# This function opens a file at the given path and returns its contents as a string
# Uses a context manager (with) to ensure the file is properly closed.
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
  # Gets the book path from the command-line argument [1] because binary stuff.
  book_path = sys.argv[1]
  # Read the book content into a string.
  book_text = get_book_text(book_path)
  
  # Prints the header for the report.
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")

  # Calculates and displays the total word count.
  print("----------- Word Count ----------")
  word_count_result = word_count(book_text)
  print(f"Found {word_count_result} total words")
  
  # Calculates character frequency and sort results.
  print("--------- Character Count -------")
  char_count = character_count(book_text) # Gets dictionary of character counts.
  sorted_chars = chars_dict_to_sorted_list(char_count) # Converts to sorted list of dictionaries.

  # Iterates through sorted character list and prints counts for alphabetic characters only.
  for char_dict in sorted_chars:
     char = char_dict["char"]
     count = char_dict["count"]
     if char.isalpha(): # Only display letters, not other characters.
        print(f"{char}: {count}")

  print("============= END ===============")




main()
