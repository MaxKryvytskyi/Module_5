articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    # global articles_dict
    search = []
    if letter_case == True:
        for i in articles_dict:
            for keys, val in i.items():
                try:
                    if key in val:
                        search.append(i) 
                        break
                except TypeError: 
                    pass
        return search
                
    else:
        for i in articles_dict:
            for keys, val in i.items():
                try:
                    if key.lower() in val or key in val:
                        search.append(i) 
                        break
                except TypeError: 
                    pass
        return search
            
    
# find_articles("Ocean", False)
find_articles("Ark", False)