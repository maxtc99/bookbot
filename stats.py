def get_num_words(text):
    words = text.split()
    ''' counter = 0
    for word in words:
        counter += 1 
    print(f"Found {counter} total words") '''
    return len(words)

def get_num_char(text):
    words = text.split()
    dict = {}
    counter = 1
    for word in words:
        lword = word.lower()
        for char in lword:                       
            if char in dict:
                dict[char] += 1
            else:
                dict.update({char:counter})  
    return dict
            
            # if char exists in dictionary then dict value += 1
            # else 
            # dict add  key / value