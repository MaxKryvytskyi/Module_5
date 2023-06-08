'''
Повернемося до нашого завдання із телефонними номерами. Компанія розширюється та вийшла на ринок Азії. 
Тепер у списку можуть знаходитись телефони різних країн. Кожна країна має свій телефонний код .

Компанія працює з наступними країнами
 _____________________________
|Країна	   |Код ISO	|Префікс  |
|Japan	   |JP	    |+81      |
|Singapore |SG	    |+65      |
|Taiwan	   |TW	    |+886     |
|Ukraine   |UA	    |+380     |
|__________|________|_________|
Щоб ми могли коректно виконати рекламну SMS кампанію, необхідно створити для кожної країни свій список телефонних номерів.

Напишіть функцію get_phone_numbers_for_сountries, яка буде:

Приймати список телефонних номерів.
Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції sanitize_phone_number.
Сортувати телефонні номери за вказаними у таблиці країнами.
Повертати словник зі списками телефонних номерів для кожної країни у такому вигляді:
{
    "UA": [<тут список телефонів>],
    "JP": [<тут список телефонів>],
    "TW": [<тут список телефонів>],
    "SG": [<тут список телефонів>]
}
Якщо не вдалося порівняти код телефону з відомими, цей телефон повинен бути доданий до списку словника з ключем 'UA'.
'''

def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    normalized_list = [sanitize_phone_number(phone) for phone in list_phones]
    sorted_list = {
    "UA": [], # Ukraine	UA	+380
    "JP": [], # Japan	JP	+81
    "TW": [], # Taiwan	TW	+886
    "SG": []  # Singapore	SG	+65
}
    for phone in normalized_list:
        if phone == '':
            continue
        if phone[:2] in "81": 
            sorted_list["JP"].append(phone)  
        elif phone[:3] in "886":
            sorted_list["TW"].append(phone)  
        elif phone[:2] in "65":
            sorted_list["SG"].append(phone)  
        else:
            sorted_list["UA"].append(phone)  

    return sorted_list
print(get_phone_numbers_for_countries(['+380-(99)-875-94-05', '+81-876-53-47', '+886 765 89 76', '+65-765-89-76', '']))

    
    
        
    
        
        
            