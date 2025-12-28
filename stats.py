def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    char_count = {}
    for c in text:
        key = c.lower()
        char_count[key] = char_count.get(key, 0) + 1
    return char_count

def sort_on(item):
    return item["num"]

def sort_dict(dict):
    list = []
    for d in dict:
        list.append({"char": d, "num": dict[d]})
    list.sort(reverse=True, key=sort_on)
    return list