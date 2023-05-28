fullname = 'Alex Old'
first_name = 'Alex'
# fullname = "Jhon Johonson"
# first_name = " "  

def is_check_name(fullname, first_name):
    return True if first_name in fullname else False
    # if first_name in fullname:
    #     return True
    # else:
    #     return False
print(is_check_name(fullname, first_name))