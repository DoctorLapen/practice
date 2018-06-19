import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')

input_file = str(input('enter input file:'))

l = []
l_new = []
d = {}
l_count = []
f = open(input_file,'r')
for line in f:
    l += line.upper().split(' ')

l = [line.rstrip() for line in l]
for i in l:
    for p in i:
     if p in " ?,.!/;:":
       i =  i.replace(p,'')
    l_new.append(i)
key = set(l_new)
for i in key:
   # print(i)

    d[l_new.count(i)]= i
    l_count.append(l_new.count(i))
max_w = max(l_count)
print(max_w )
print(d[max_w])
f.close()