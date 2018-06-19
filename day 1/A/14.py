import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')

while True:
    mouth = str(input('введіть місяць:'))
    if mouth == 'січень' or mouth == 'Cічень':
        print('Кількість днів = 31')
    elif mouth == 'Лютий' or mouth == 'лютий':
        print('Кількість днів = 28 або 29')
    elif mouth == 'Березень' or mouth == 'березень':
        print('Кількість днів = 31')
    elif mouth == 'Квітень' or mouth == 'квітень':
        print('Кількість днів = 30')
    elif mouth == 'Травень' or mouth == 'травень':
        print('Кількість днів = 31')
    elif mouth == 'Червень' or mouth == 'червень':
        print('Кількість днів = 30')     
    elif mouth == 'Липень' or mouth == 'липень':
        print('Кількість днів = 31')
    elif mouth == 'Серпень' or mouth == 'серпень':
        print('Кількість днів = 31')
    elif mouth == 'Вересень' or mouth == 'вересень':
        print('Кількість днів = 30')
    elif mouth == 'Жовтень' or mouth == 'жовтень':
        print('Кількість днів = 31')
    elif mouth == 'Листопад' or mouth == 'листопад':
        print('Кількість днів = 30')    
    elif mouth == 'Грудень' or mouth == 'грудень':
        print('Кількість днів = 31')
    else:
        print('введіть правильні дані')
