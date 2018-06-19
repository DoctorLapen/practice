import datetime
import math
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Лапін Костянтин\n')

d = float(input('введіть висоту у метрах: '))

speed = math.sqrt(2*9.8*d)
print('Швидкість = {:.2f} м/с '.format(speed))