import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')

centimeters= int(input('Введіть свій зріст у сантиметрах: '))
ft = centimeters // 30.48
jj = centimeters % 30.48
d = jj /2.54
print(ft)
print(jj)
print(d)
#print('Зріст у дюймах: {:.2f}\nЗріст у футах: {:.2f}'.format(centimeters/2.54,centimeters/30.48))
print(1.54 + 0.276098)

