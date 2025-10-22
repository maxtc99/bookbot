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
            
def sort_on(items):
    return items["num"]
         
def get_sorted_list(dict):
    dline = {}
    list = []
    for k in dict:
        dline = {"char":k, "num":dict[k]}

        list.append(dline)
    list.sort(reverse=True, key=sort_on)    
    return list


