import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')

name = str(input("введіть своє ім'я: "))
print('Привіт' ,name)

