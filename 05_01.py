


def real_len(text):
    val = "\n", "\t", "\f", "\v", "\r"
    text = list(text)
    for v in val:
        try:
            text.remove(v)
        except ValueError:
            pass
    text = "".join(text)
    return len(text)


print(real_len('Alex\nKdfe23\t\f\v.\r'))
print(real_len('Al\nKdfe23\t\v.\r'))