import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')


def Exponentiation(x,n):
    if n == 0:
           return 1
    elif n > 0:

     return   x * Exponentiation(x,n-1)


print(Exponentiation(2,3))