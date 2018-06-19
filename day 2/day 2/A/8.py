import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')
string = str(input('введіть рядок: '))
num_of_uniq_symb = len(set(string))

print('Кількість унікальних символів = '+ str(num_of_uniq_symb))