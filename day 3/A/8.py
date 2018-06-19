import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')
def magic_date(day,month,year):
   g_2 = str(year)
   y_2 =int( g_2[-2:len(g_2)])

   if day*month == int(y_2):
       m = ('{}-{}-{}-магічна дата'.format(day,month,year))
       return  m
   else:
       m = ('{}-{}-{}-звичайна дата'.format(day, month, year))
       return m

print(magic_date(28, 2, 2020))
print(magic_date(24, 2, 1948))