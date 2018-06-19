import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')

def enter():
   global s_new
   s_new = []
   global x
   x = (input('введіть 4-значне число: '))
   s = list(x)
   try:
       for i in s:
           i_new = int(i)
           s_new.append(i_new)
   except:
        enter()
   if len(s_new) == 4:
       print('сума цифр числа ' + str(x) + ' = ' + str(sum(s_new)))

   else:
       enter()


enter()



