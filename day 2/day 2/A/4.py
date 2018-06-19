import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')

def f(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n


l = [-2,3,4,4,5,6,6,6,6,7,8,0,3.5,2.1,3.1,3.1,4,3.1,1,2.1,1,1,2.1]


freq_lis = f(l)
# print(freq_lis)
# частоти зустрічі елементів у списку
number_of_items = 0
for el in freq_lis:
        print('частота елемента {} = {}'.format(el,l.count(el)))
#обчислення кількості елементів у діапазоні від 1 до 5
freq_in_range_list = []
for el in freq_lis:
    if 1 <= el <5:
        freq_in_range_list.append(el)
#print(freq_in_range_list)
number_of_items_1_5 = 0
for freq in freq_in_range_list:
    number_of_items_1_5 += l.count(freq)


print('кількість елементів у діапазоні від 1 до 5 = '+ str(number_of_items_1_5))


