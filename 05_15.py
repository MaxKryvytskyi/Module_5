import re

text =  'The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com '

def find_all_links(text):
    result = []
    iterator = re.finditer(r"https?://(?![\w]*\.\.)[\w\.]+", text) 
    for match in iterator:
        result.append(match.group())
    return result

print(find_all_links(text))


