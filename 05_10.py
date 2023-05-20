import re
text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
word = "Python"

def find_word(text, word):
    dict_list = { "result" : False,
                  "first_index" : None,
                  "last_index" : None,
                  "search_string" : word,
                  "string" : text
                }
    
    search_name = re.search(word, text)
    if search_name == None:
        return dict_list
    if search_name.group() in word:
        dict_list["result"] = True
        first_index, last_index = search_name.span()
        dict_list["first_index"] = first_index 
        dict_list["last_index"] = last_index
        return dict_list
    
print(find_word(text, word))           
            
            