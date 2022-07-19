import random


def password_gerator():
    length = random.randint(5, 10)
    d = ""

    for b in range(length):
        letters = random.choice(list("qwertyuiopasdfghjklzxcvbnmZXCVBNMLKJHGFDSAQWERTYUIOP"))
        number = random.choice(list("1234567890"))
        characters = random.choice(list("~!@#$%&*/?"))
        if b < 1:
            d += letters + number + characters
        elif b < 2:
            d += letters + number
        else:
            d += letters
    d = list(d)
    password = ""
    while len(d) > 0:
        random.shuffle(d)
        password += d[0]
        d.remove(d[0])

    return password

def pw_validator(password):
    if len(password) < 8:
        print("Password length has to be greater than or equal to 8")
        return False
    letters_lower = "qwertyuiopasdfghjklzxcvbnm"
    letters_upper = "ZXCVBNMLKJHGFDSAQWERTYUIOP"
    characters = "`~!@#$%^&*()_-+=[]{}:;'\"<>,./?|\\"

    letter_l, letter_u, charact, num = 0, 0, 0, 0
    for i in password:
        if i.isdigit():
            num += 1
        elif i in letters_lower:
            letter_l += 1
        elif i in letters_upper:
            letter_u += 1
        elif i in characters:
            charact += 1
    
    if 0 in [letter_l, letter_u, charact, num]:
        return False
    
    return True

def triangle(lines):
    space = 0
    triangle_contents = []
    
    if lines < 0:
        symbol_number = -2 *  lines - 1 
    else:
         symbol_number = 2*lines -1 

    for i in range(0, symbol_number, 2):
        triangle = " " * space + "#" * (symbol_number - i)
        triangle_contents.append(triangle)
        space += 1
            
    if lines < 0:
        for k in triangle_contents:
            print(k)
    else:
        for j in range(len(triangle_contents)):
            print(triangle_contents[len(triangle_contents)- j - 1])


