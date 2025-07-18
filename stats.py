def word_count(book_string):
    word_count_list = book_string.split()
    return len(word_count_list)

def character_count(book_string):
    book_string = book_string.lower()
    character_dict = {}
    for char in book_string:
        if char in character_dict:
            character_dict[char] +=1
        elif char not in character_dict:
            character_dict[char] = 1
    sorted_dict = dict(sorted(character_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict

