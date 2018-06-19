import datetime
from random import choice
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')
article = ["the", "a", "one", "some", "any"]
noun = ["boy", "girl", "dog", "town" ,"car"]
verb = ["drove", "jumped", "ran", "walked" ,"skipped"]
preposition = ["to", "from", "over", "under" ,"on"]
c = 0
while c < 10:
 print('{} {} {} {} {} {}.'.format(choice(article).capitalize(),choice(noun),choice(verb),choice(preposition),choice(article),choice(noun )))
 c += 1