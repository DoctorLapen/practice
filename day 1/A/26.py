import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')


while True:
  a  = float(input('введіть довжину сторони a: '))
  b  = float(input('введіть довжину сторони b: '))
  c  =  float(input('введіть довжину сторони с: '))  
  if a == b == c:
    print('Трикутник ABC --- рівносторонній')
  elif a == b or a == c or c == b:
    print('Трикутник ABC --- рівнобедрений')
  else:
    print('Трикутник ABC --- нерівносторонній')
