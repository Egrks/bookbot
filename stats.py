def get_book_text(flpth):
    with open(flpth) as f:
        file_text = f.read()
        return file_text
    
def wordcount(flpth):
    split_text = get_book_text(flpth).split()
    k = 0
    for i in split_text:
        k += 1
    return f"{k} words found in the document"

def charcount(flpth):
    char_dict = {}
    split_text = get_book_text(flpth).lower().split()
    
    for i in split_text:
        character_list = list(i)
        for character in character_list:
            if character in char_dict:
                char_dict[character] += 1
            else:
                char_dict[character] = 1
    return char_dict


        
    
    

    
