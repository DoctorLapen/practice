import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')
l_f2 = []
l = []
l_output = []


f = open('6_start.txt','r')


for i in f:
    l += i.split(' ')

c = 0
n =  0

num = 0
while c  < len(l):

       if l[c] != l[n] :
           l_output.append(l[n])
           l_output.append(num)

           n = c
           num = 0

       c +=1
       num += 1
f2  = open('6_compressed.txt','w')

for i in l_output:
    f2.write(str(i)+ ' ')
f2.close()
f3  = open('6_compressed.txt','r')
for i in f3:
    l_f2 += i.split(' ')
    del l_f2[-1]
f3.close()
f4  = open('6_decompressed.txt','w')
i = 0
w = 0
nu = 1

while i < len(l_f2)/2:

   p_word =(' '+ l_f2[w])*int(l_f2[nu])
   f4.write(p_word)


   w += 2
   nu += 2
   i += 1
print(len((l)))
print(len(l_output))


print('стиснено на: {:.2f}%'.format(100-(len(l_output)/(len(l)*0.01))))

f4.close()
f.close()

