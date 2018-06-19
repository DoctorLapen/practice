import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')
i = -1
l = []

while i != 0 :
    i = int(input('введіть ціле число: '))
    l.append(i)




del l[-1]

l.sort()


for el in l:
    print(el)