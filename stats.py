def word_count(text):
    words = text.split()
    len(words)
    return len(words)

def char_count(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1
    return char_count

def get_sorted_chars(char_dict):


