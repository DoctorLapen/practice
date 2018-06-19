import datetime
from sys import argv
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')
l = []

l2 = []

try:
   input_file_1 = argv[1]
   input_file_2 = argv[2]

   f1 = open(input_file_1,'r')
   f2 = open(input_file_2,'r')


   for i in f1:
     l.append(i)
   for i in f2:
     l.append(i)
   l = [line.rstrip() for line in l]



   for i in l:
      print(i)
   f1.close()
   f2.close()

except IndexError:
      print('параметри командного рядка пропущено.')
except FileNotFoundError:
         print('файл не існує')