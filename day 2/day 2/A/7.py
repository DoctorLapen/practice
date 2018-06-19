import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')


i = -1
pre_l = []
def f(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n


while i != '' :
    i = str(input())
    pre_l.append(i)
l = f(pre_l)
for i in l:
    print(i)