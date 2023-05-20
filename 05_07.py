CYRILLIC = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
LATIN = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
name = "Максим кривицький"
def translate(name):
    for c, l in zip(CYRILLIC, LATIN):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    return (name.translate(TRANS)) 

print(translate(name))

