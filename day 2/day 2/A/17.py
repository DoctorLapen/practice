import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')

for i in range(2,10000):
    s = 0
    for c in range(1,i):
        if i%c == 0:
            s += c
    if s == i:
        print(i)