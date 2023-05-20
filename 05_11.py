import re

text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn"
word = "Python"

def find_all_words(text, word):
    return re.findall(word, text, flags=re.IGNORECASE)
find_all_words(text, word)
