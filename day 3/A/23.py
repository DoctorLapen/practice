import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')

input_file = str(input('enter input file:'))
output_file = str(input('enter output file:'))
l = []
f = open(input_file,'r')
for line in f:
    l.append(line)

f.close()

h = open(output_file, 'w')
n = 1
for i in l:
    h.write(str(n)+'. '+ i)
    n +=1
h.close()
print('The END!!!')
