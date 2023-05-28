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

    
    
        
    
        
        
            