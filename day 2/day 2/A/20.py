import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')


pre_i = -1
l = []

def middle(lis):
    return sum(lis)/len(lis)

while pre_i != '' :
   pre_i = input()
   if pre_i =='':
    break
   else:
    i = float( pre_i)
    l.append(i)
mid = middle(l)
less_mid_list = []
more_mid_list = []
print('середнє значення = {:.2f}' .format(mid))

for i in l:
    if i < mid:
        less_mid_list.append(i)
    elif i >= mid:
        more_mid_list.append(i)
print('числа  що не перевищують середнє значення: {}\nчисла  що більше або рівні за середнє значення:{}'.format(less_mid_list,more_mid_list))        

