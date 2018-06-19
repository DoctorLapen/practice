import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')

d = {'a':678,'b':1,'c':-1.78,'d':5}
d_up = sorted(d.items(), key=lambda x: x[1])
d_down = sorted(d.items(), key=lambda x: x[1],reverse = True)
print(d_up)
print(d_down)
print(d_up + d_down)