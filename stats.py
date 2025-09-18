def get_num_words(text):
    words = str.split(text)
    return len(words)

def get_num_characters(text):
    dictionary_characters = {}

    for char in text:
        lowercase = char.lower()
        if lowercase not in dictionary_characters:
            dictionary_characters[lowercase] = 1
        else:
            dictionary_characters[lowercase] += 1
    return dictionary_characters

def sort_on(item):
    return item["num"]


def list_sorting(dictionary_characters):
    result = []
    
    for char, num in dictionary_characters.items():
        smol = {"char": char, "num": num}
        result.append(smol)
    result.sort(reverse=True, key=sort_on)
    return result
