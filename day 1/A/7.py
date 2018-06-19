import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')

Celsius = float(input('введіть температуру по шкалі Цельсія: '))
print('по Кельвіну: ',Celsius + 273.15,'\nпо Фаренгейту: ',9/5*Celsius+32)