def word_count(book_text):
   num_words = len(book_text.split())
   return num_words

def character_count(book_text):
    chars_dict = {}

    for char in book_text:
        char = char.lower()
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def sort_on(dict):
    
    return dict["count"]

def chars_dict_to_sorted_list(char_count):
    chars_list = []
    for char, count in char_count.items():
        chars_list.append({"char": char, "count": count})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list