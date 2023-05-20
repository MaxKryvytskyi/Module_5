

def formatted_numbers():
    list_num = list()
    list_num.append("|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary")) 
    for i in range(16):
        dec1 = '{:d}'.format(i)
        hex1 = '{:x}'.format(i)
        bin1 = '{:b}'.format(i)
        list_num.append("|{:<10}|{:^10}|{:>10}|".format(dec1, hex1, bin1)) 
    return list_num

for el in formatted_numbers():
    print(el)
    
    
