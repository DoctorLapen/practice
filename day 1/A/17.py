import datetime
import math
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')

a  = float(input('введіть суму: '))
year_1 =  a* 1.14
year_2 =  year_1*1.14
year_3 =  year_2*1.14
print("Сума на рахунку через 1 рік: {:.2f}\nСума на рахунку через 2 роки: {:.2f}\nСума на рахунку через 3 роки: {:.2f}".format(year_1,year_2,year_3))
