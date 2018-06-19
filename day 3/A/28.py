import datetime
from sys import argv
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')
l = []
try:
   input_file = argv[1]
   f = open(input_file,'r')

   n = 1
   for i in f:
     l.append(i)
     if n == 10:
        break
     n += 1
   l = [line.rstrip() for line in l]

   for i in l:
      print(i)
   f.close()

except IndexError:
      print('параметр командного рядка пропущено.')
except FileNotFoundError:
         print('файл не існує')