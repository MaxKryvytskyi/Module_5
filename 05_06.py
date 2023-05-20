# лох
# молох бог ужасен.
# лох
# сполох ходит далеко.
# лох
# ты хорош, но выглядишь как лох.
# лох
# молох бог ужасен.
spam_words = ['лох']
text = 'ты хорош, но выглядишь как лох.'
def is_spam_words(text, spam_words, space_around = False):
    words = (
        text.strip()
        .removeprefix("-")
        .replace("?", "")
        .replace("!", "")
        .replace(",", "")
        .replace(".", "")
    )
    words = words.lower()
    word = words.split(" ") 
    
    if space_around == True:
        for wor in word:
            for sw in spam_words:
                sw.lower()
                if sw in wor:
                    if len(sw) == len(wor):
                        return True
                    else:
                        return False
    else:
        for wor in word:
            for sw in spam_words:
                sw.lower()
                if sw in wor:
                    if len(sw) <= len(wor):
                        return True
                    else:
                        return False
print(is_spam_words(text, spam_words, space_around = True))