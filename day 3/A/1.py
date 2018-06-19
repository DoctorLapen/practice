import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')
def payment(path,price_140):
    payment = 25 + (path/140)*price_140
    return payment
path = int(input('enter your path: '))
price = int(input('enter price per 140 meters: '))
print(payment(path,price))
