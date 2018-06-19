import datetime
from random import randint
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')
def gener_passwords():
    l = []
    password = ''
    c = 0
    i = 0
    while i <10:
       end = randint(8, 17)
       while c < end:
           ascii_num = chr(randint(33,127))
           password += str(ascii_num)
           c += 1
       l.append(password)
       c = 0
       password = ''
       i += 1
    return l

x = gener_passwords()
for j in x:
    print(j)
