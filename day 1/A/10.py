import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')


x = int(input('введіть кількість штучох: '))
x2 = int(input('введіть кількість штукенцій: '))
print('загальна маса замовлення: '+str(x*0.075+x2*0.112)+'кг')
