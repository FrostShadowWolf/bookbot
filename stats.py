def get_num_words(words):
    #with open(path) as f:
    c = 0
    data = words
    lines = data.split()
    c += len(lines)
    return c
    
def get_chars_dict(words):
    count = {}
    #with open(path) as f:
    data = words.lower()
    for line in data:
        for c in line:
            count[c]=count.setdefault(c, 0)+1
    return count
    
def sort_on(item):
    return item["num"]
    
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
