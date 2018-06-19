import datetime
import random
from itertools import permutations
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')
l = [1,-2.33,3.89,-8,9008]
print(l)
random.shuffle(l)
print(l)


l_new = []
for p in permutations(l):
    l_new.append(p)
c = 0
random_numbers = []
while c <  8:
    random_numbers.append(random.randint(-1000,1001))
    c += 1


print(len(l_new))
print(l_new+ random_numbers )