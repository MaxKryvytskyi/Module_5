phone = "   +38(050)123-32-34   "
print(phone)
def sanitize_phone_number(phone):
    phones = ""
    phone.strip()
    for p in phone:
        if p in "0123456789":
            phones += p
        else:
            pass
    return phones

print(sanitize_phone_number(phone))