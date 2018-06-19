import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')

l = [('a',100),('b',666),('c',-98),('d',100),('e',-87960)]
d = dict(l)


print(d)
