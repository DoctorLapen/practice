import datetime
from math import sqrt
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')
n = int(input('enter integer: '))
l = [i for i in range (2,n,1)]

p = 2
i = 0
while p <sqrt(n) :
    for i in l :
        if i%p == 0 and i != p:
            l.remove(i)
    p += 1

print(l)