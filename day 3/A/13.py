import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)