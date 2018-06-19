import datetime
from random import choice
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')
l = []
password = ''
f = open('words for passwors_27.txt','r')
for i in f:
    l += i.split(',')
f.close()
print(l)
c = 0
while c< 2:
    w = choice(l)

    if   3 <= len(w)and w not in password:
        if c == 0:
            password += w
            c += 1
        elif c == 1 and 8 <= len(password + w) <= 16 :


            password += w
            c += 1

print(len(password))


print(password.capitalize())
