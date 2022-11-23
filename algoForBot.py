import random

def gen_nickname():
    
    list_1 = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 
            'l', 'm', 'n', 'p', 'q', 'r', 's', 
            't', 'w', 'x', 'z']
    
    list_2 = ['a', 'e', 'i', 'u', 'y']

    lenght = [1, 2, 3] # Длина никнейма
    n = random.choice(lenght)
    
    nickname = []
    count = 0
    
    join = list_1 + list_2
    first = random.choice(join)
    last = random.choice(join)
    
    # Пока не закончится случайная длина
    while count != n:
        
        # Случайная буква из первого списка 
        i = random.choice(list_1)
        nickname.append(i)
        
        #Случайная буква из второго списка
        i = random.choice(list_2)
        nickname.append(i)
        
        count += 1
    
    # Со списка в строку
    first_letter = ''.join(first)        
    nick = ''.join(nickname)
    last_letter = ''.join(last)
    # Объединить слово
    full = first_letter + nick + last_letter
    # Возврощаем строку
    return full.title()
    
    
def gen_password():

    list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k',
            'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'w',
            'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
            'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S',
            'T', 'U', 'W', 'X', 'Y', 'Z']

    password = []
    count = 0

    for i in list:
        while count != 16:
            count += 1
            i = random.choice(list)
            password.append(i)

    str_pass = ''.join(password)
    return str_pass