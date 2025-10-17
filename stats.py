#def get_word_count(file_path):
#    num_words = 0
#    with open(file_path) as f:
#        data = f.read()
#        words = data.split()
#        num_words += len(words)
#    print(f"Found {num_words} total words")
#get_word_count("books/frankenstein.txt")

#def get_word_count(file_path):
#    num_characters = {}
#    with open(file_path) as f:
#        file_path = ("books/frankenstein.txt")
#        data = f.read()
#        words = data.lower()
#        for characters in words:
#            if characters in num_characters:
#                num_characters[characters] += 1
#            else:
#                num_characters[characters] = 1
#    return num_characters

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if  lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list