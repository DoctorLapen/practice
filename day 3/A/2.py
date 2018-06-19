import datetime
from random import randint
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')

def random_phone_numbers():
    l = []
    number = '+38(0'
    c = 0
    i = 0
    while c < 3:
        while i < 9:
            x = randint(1, 9)

            number += str(x)
            if i  == 1:
                number += ')'
            elif i == 4 or i == 6:
                number += '-'
            i +=1

        l.append(number)
        number = '+38(0'
        i = 0
        c +=1
    return l
x = random_phone_numbers()

for j in x:
    print(j)