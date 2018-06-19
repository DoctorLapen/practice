import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')
l = []
len_words = []
f = open('hell.txt','r')
for line in f:
    l += line.split(' ')
for i in l:
    len_words.append(len(i))
max_len = max(len_words)
print('max_word_len: ' + str(max_len ))
for i in l:
    if len(i)==max_len:
        print(i)
f.close()

