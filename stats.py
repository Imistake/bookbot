# Counts total number of words in the provided text.
# Args = book_text (str): The text content to analyse.
# Returns = an integer which is the total number of words in a text.
def word_count(book_text):
   num_words = len(book_text.split()) # Split text by whitespace and count the elements (spaces, tabs, newlines, etc.)
   return num_words


# Counts the frequency of each character in the text.
# Args = book_text(str): The text content to analyse.
# Returns = dict: A dictionary where keys are characters and values are their frequencies.
def character_count(book_text):
    chars_dict = {} # Initialising empty dictionary to store character counts.

    for char in book_text:
        char = char.lower() # Converting to lowercase for case-insensitive counting.
        if char in chars_dict:
            chars_dict[char] += 1 # Increment existing character count.
        else:
            chars_dict[char] = 1 # Add new character to dictionary with count 1.
    return chars_dict


# This is a helper function that returns the value to sort by when sorting character dictionaries.
# Used as the key function for sorting in chars_dict_to_sorted_list.
# Args = dict (dictionary): A dictionary containing character and count.
# Returns = int: The count value to sort by.
def sort_on(dict):
    
    return dict["count"]

# Converts a character count dictionary to a list of dictionaries sorted by character frequency in descending order.
# Args = char_count (dict): Dictionary mapping characters to their frequencies.
# Returns = list: List of dictionaries, each with 'char' and 'count' keys, sorted by count.
def chars_dict_to_sorted_list(char_count):
    chars_list = [] # Initialize empty list to store character dictionaries.
    for char, count in char_count.items(): # Convert dictionary to list of dictionaries.
        chars_list.append({"char": char, "count": count})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list