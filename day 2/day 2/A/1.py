import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')

pre_l = [1,2,3,3,'name',567,567,567,1,1,1,1,5,7,6,5,7,'hell','name','hell','njjk','hell']
def f(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

l = f(pre_l)
print(l)
l_new = l.copy()
del l_new[3]
del l_new[2]
del l_new[0]
print(l_new)
