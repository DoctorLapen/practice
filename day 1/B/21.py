import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Лапін Костянтин\n')
while True:
    mark = str(input('введіть буквенну оцінку: '))
    if mark == 'A+':
        print('Бальна оцінка = >4.0')
    elif mark == 'A':
        print('Бальна оцінка = 4.0')
    elif mark == 'A-':
        print('Бальна оцінка = 3.7')
    elif mark == 'B+':
        print('Бальна оцінка = 3.3')
    elif mark == 'B':
        print('Бальна оцінка = 3.0')
    elif mark == 'B-':
        print('Бальна оцінка = 2.7')
    elif mark == 'C+':
        print('Бальна оцінка = 2.3')
    elif mark == 'C':
        print('Бальна оцінка = 2.0')
    elif mark == 'C-':
        print('Бальна оцінка = 1.7')
    elif mark == 'D+':
        print('Бальна оцінка = 1.3')
    elif mark == 'D':
        print('Бальна оцінка = 1.0')
    elif mark == 'F':
        print('Бальна оцінка = 0')
    else:
       print('введена буквенна оцінка не іcнyє')
