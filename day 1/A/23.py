import datetime
import math
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')

a  = float(input('введіть a: '))
b  = float(input('введіть b: '))
print('a + b = {:.2f}'.format(a + b))
      
print('b - a = {:.2f}'.format(b - a))

print('a * b = {:.2f}'.format(a * b))
if b == 0 :
    print('ділення на нуль')
else:
  print('частка від ділення a на b = {:.2f}'.format(a //b))
  print('остача від ділення a на b = {:.2f}'.format(a % b))
  
print('логарифм a з основою 10 = {:.2f}'.format(math.log10(a)))
print('a піднесенна до степеня b = {:.2f}'.format(a**b))



    
