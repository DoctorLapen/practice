import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')

def fib(n):
    if n<3:
        return 1
    return fib(n-1) + fib(n-2)