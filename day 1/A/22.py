import datetime
import math
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')

r  = float(input('введіть радіус: '))
print('Площа кругу:{:.2f}\nОб`єм кулі:{:.2f}'.format(math.pi*r**2,4/3*math.pi*r**3))
