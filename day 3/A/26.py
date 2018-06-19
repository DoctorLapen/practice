import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')
l = []
while True:
 try:
    global num
    num_str = str(input('enter num: '))
    if num_str == '':
        break
    num = float(num_str)
    print(num_str)
    l.append(num)
    print('Сума: ' + str(sum(l)))
 except:
    print('введено нечислові дані!!!')

