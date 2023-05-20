import re

text = 'Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777 +380(67)777-77-787'

def find_all_emails(text):
    return [m.group() for m in re.finditer(r"((\+?[0-9]{3}?\(?[0-9]{2}\)?[0-9]{3}\-)([0-9]{2}\-[0-9]{2}|[0-9]{1}\-[0-9]{3}))", text)] 
print(find_all_emails(text))
