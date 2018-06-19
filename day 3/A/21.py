import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')
l = []
f = open('text_21.txt','r')
for line in f:
    l.append(line)

f.close()
l.append('Лапін Костянтин Едуардович')
h = open('text_21.txt','w')
for i in l:
    h.write(i)
h.close()
