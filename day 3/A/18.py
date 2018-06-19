import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')


def sum_g(n):
    if n == 0:
        return 0
    else:

        return 1/n + sum_g(n - 1)

print(sum_g(4))