  
def get_num_words(text):
    return len(text.split())
    
    
def get_char_count(text):
    lower_text = text.lower()
    char_count = {}
    for char in lower_text:
        if char in char_count:
            char_count[char] += 1
        else:    
            char_count[char] = 1
    return char_count

def sort_char_count_dict(char_count_dict):
    char_list = []
    for char, count in char_count_dict.items():
        char_list.append({'char': char, 'num': count})
        
    def get_count(items):
        return items['num']

    char_list.sort(reverse=True, key=get_count)
    return char_list
