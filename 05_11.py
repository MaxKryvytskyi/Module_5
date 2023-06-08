'''
Для закріплення матеріалу напишіть функцію find_all_words, яка шукає збіг слова в тексті. 
Функція повертає список всіх знаходжень слова в параметрі word в тексті у вигляді будь-якого написання, тобто, 
наприклад, можливі варіанти написання слова "Python" як pYthoN, pythOn, PYTHOn і т.і. головне, 
щоб зберігався порядок слів, регістр не має значення.

Підказка: функції модуля re приймають ще ключовий параметр flags і ми можемо визначити нечутливість до регістру, 
надавши йому значення re.IGNORECASE
'''



import re

text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn"
word = "Python"

def find_all_words(text, word):
    return re.findall(word, text, flags=re.IGNORECASE)
find_all_words(text, word)
