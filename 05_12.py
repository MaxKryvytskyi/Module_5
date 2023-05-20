import re

text = 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn '

spam_words = ['began', 'Python']

def replace_spam_words(text, spam_words):
    for sw in spam_words:
        if sw in text:
            text = re.sub(sw, '*' * len(sw), text, flags=re.IGNORECASE)
        else:
            pass
    return text
    
print(replace_spam_words(text, spam_words))
    