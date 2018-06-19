import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')
keys_symb = [['A','E','I','L','N','O','R','S','T','U'],['D','G'],['B','C','M','P'],['f','H','V','W','Y'],['K'],['J','X'],['Q','Z']]

d = {}
c = 0
i = 0
n = 8
while c < 7:
    if c > 4:
       while i < len(keys_symb[c]):
            d[keys_symb[c][i]] = n
            i += 1
       n += 2

    else:
        while i < len(keys_symb[c]):
         d[keys_symb[c][i]] = c+1
         i += 1
    c += 1
    i = 0

string = str(input('введіть слово: ')).upper()

#
mark = 0
cont = True
for j in string:
    if j not in  'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
         print('введений не підтримуваний символ --- ' + j)
         cont = False
         break

if cont is True:
    for f in string:
        mark += d.get(f)

    print('оцінка --- ' + str(mark)+ ' балів')
