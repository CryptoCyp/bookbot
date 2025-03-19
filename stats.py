def char_count(text):
    char_dict = {}
    lower = text.lower()
    
    for char in lower:
        if char not in char_dict and char.isalpha():
            char_dict[char] = 1
        elif char in char_dict and char.isalpha():
            char_dict[char] += 1
    return char_dict
    

def summary_function(char_dict,content):
    print("=========== BOOKBOT ============")
    print(f"Analyzing the book")
    print("----------- Word Count -----------")
    splitted = content.split()
    count = 0
    for word in splitted:
        count += 1
    print(f"Found {count} total words")
    print("-------- Character Count ----------")
    descending = sorted(char_dict.items(), key=lambda x:x[1], reverse=True)
    converted_descending = dict(descending)
    for key, value in converted_descending.items():
        print(f"{key}: {value}", " ")
    print("========== End ============")



