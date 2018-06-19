import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')
Suit_of_cards = ['s','h','c','d']

Ranks_of_cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

card_deck = []
for i in Suit_of_cards:
    for rank in Ranks_of_cards:
        card = rank + i
        card_deck.append(card)


print(card_deck)