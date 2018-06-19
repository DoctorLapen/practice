import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')

cost = float(input('введіть віртість їжі: '))
print('Чайові: {:.2f}\nПодаток: {:.2f}\nЗагальна сума для оплати: {:.2f}'.format(cost*0.14,cost*0.18,cost +cost*0.18 + cost*0.14))