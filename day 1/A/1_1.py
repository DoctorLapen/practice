import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')


con_less_1 = int(input('введіть кількість контейнерів до 1 літра: '))
con_more_1 = int(input('введіть кількість контейнерів понад 1 літр: '))
result = con_less_1*0.1 + con_more_1*0.25
print('Доплата: {:.2f}$'.format(result))
