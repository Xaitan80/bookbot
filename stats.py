    
def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    found_so_far = {}
    words_lower = file_contents.lower()
    for c in words_lower:
        if c in found_so_far:
            found_so_far[c] += 1
        else:
            found_so_far[c] = 1

    return found_so_far

def sort(ccd):
    list_of_char_dicts = []
    for char, count in ccd.items():
        if char.isalpha() == False:
            continue
        dicti = {"char": char, "num": count}
        list_of_char_dicts.append(dicti)
    def sort_on(item_dict):
        return item_dict["num"]
    
    list_of_char_dicts.sort(reverse=True, key=sort_on)

    return list_of_char_dicts

    








