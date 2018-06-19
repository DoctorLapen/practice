import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Лапін Костянтин\n')
n = int(input('Введіть ціле число:'))
print('сума всіх цілих чисел від 1 до n = '+str(int(n*(n + 1)/2)))