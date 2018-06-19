import datetime
from sys import argv
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')
l = []
l_output = []
try:
   input_file = argv[1]
   f = open(input_file,'r')


   for i in f:
     l.append(i)

   l = [line.rstrip() for line in l]
   l_output = l[-10:len(l)]


   for i in l_output:
      print(i)
   f.close()

except IndexError:
      print('параметр командного рядка пропущено.')
except FileNotFoundError:
         print('файл не існує')