import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')

bread = int(input('введіть кількість буханок хлібу: '))
print('Звичайна вартість товару:\n {:>10.2f} грн.\nСкидка:\n {:>10.2f} грн.\nЗагальна вартість покупки:\n {:>10.2f} грн.'.format(bread*8.5,bread*8.5*0.6,bread*8.5*0.4))

