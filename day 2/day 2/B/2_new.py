import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')
keys_symb = [['.',',','?','!',':'],['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],
 ['T','U','V'],['W','X','Y','Z']]
d = {' ':'0'}
c = 0
i = 0
n = 2
while c < 9:
    while i < len(keys_symb[c]):
        if i == 0:
          d[keys_symb[c][i]] = str(c+1)
        else:
            d[keys_symb[c][i]] = str(c+1)*n
            n +=1
        i += 1
    c += 1
    i = 0
    n = 2
string = str(input('введіть строку: ')).upper()


output_string = ''
cont = True
for j in string:
    if j not in  ' .,?!:ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print('введений не підтримуваний символ --- ' + j)
        cont = False
        break

if cont is True:
    for f in string:
        output_string += d.get(f)
    print(len(output_string))
    print(output_string)
