import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')


def GCD(x,y):
    if y == x:
         return x
    elif x > y:
        return  GCD(x-y,y)

    elif x < y:
        return  GCD(y,y-x)

print(GCD(28,124))