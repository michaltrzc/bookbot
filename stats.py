def count_words(saved_text):
    split_words = saved_text.split()
    num_words = len(split_words)
    return num_words

def count_characters(saved_text):
    dictionary = {}
    for character in saved_text:
        character_low = character.lower()
        if character_low in dictionary:
            dictionary[character_low] = dictionary[character_low] + 1
        else:
            dictionary.update({character_low: 1})
    return dictionary

def sort_on(dict_item):
    # Assuming each dict has a 'count' key
    return dict_item["count"]

def return_sorted_list_dictionaries(dictionary):
    # Convert dictionary to list of dictionaries
    dictlist = []
    for char, count in dictionary.items():  #tu dictionary przerabiam na listę
        dictlist.append({"char": char, "count": count})
    # Sort the list by count (high to low)
    dictlist.sort(reverse=True, key=sort_on)
    return dictlist
