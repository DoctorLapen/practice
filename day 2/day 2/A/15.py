import datetime
from random import randrange
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')



def Durstenfeld(items):
    n = len(items)
    for i in range(n-1,2,-1):
        print(i)
        j = randrange(i)  
        items[j], items[i] = items[i], items[j]
    return

def Fisher_Yates(items):
    items_new = []
    n = len(items)
    for i in range(n,2,-1):
        j = randrange(i)  
        items_new.append(items[j])
        del items[j]
        
    return  items_new

Suit_of_cards = ['s','h','c','d']

Ranks_of_cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

card_deck = []

for i in Suit_of_cards:
    for rank in Ranks_of_cards:
        card = rank + i
        card_deck.append(card)
card_deck_2 = card_deck.copy()       
print(card_deck)
Durstenfeld(card_deck)
print('відсортована колода')
print(card_deck)
print('Fisher_Yates')
print(card_deck_2)
deck = Fisher_Yates(card_deck_2)
print('відсортована колода')
print(deck)


