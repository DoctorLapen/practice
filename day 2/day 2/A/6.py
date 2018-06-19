import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')

l = [89,1,2,3,-2,4,5,6,7]
l.sort()
print(l)
n = int(input('введіть ціле додатнє число: '))
if n*2 >= len(l):
    print('нє вистачає  елементів для видалення')
else:
  c = 0
  while c < n:
    del l[0]

    del l[-1]
    c +=1
  print(l)