import datetime
from random import randrange
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')



def sattoloCycle(items):
    i = len(items)
    while i > 1:
        i = i - 1
        j = randrange(i)  # 0 <= j <= i-1
        items[j], items[i] = items[i], items[j]
    return


Suit_of_cards = ['s','h','c','d']

Ranks_of_cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

card_deck = []
for i in Suit_of_cards:
    for rank in Ranks_of_cards:
        card = rank + i
        card_deck.append(card)

sattoloCycle(card_deck)


number_of_cards = int(input('введіть кількість карт на одного гравця:'))
players = int(input('введіть кількість гравців:'))
cards_for_this_games = number_of_cards*players
if cards_for_this_games > 52:
    print('немає стільки карт для цієї партії')
else:

  card_deck_x =card_deck.copy()
  print(card_deck)
# if cards_for_this_games <= 52:
#  new_lis =  card_deck[0,cards_for_this_games,1]
  c1 = 0
  c2 = 0
  while c1 < players:
      print('гравець' + str(c1 + 1))
      while c2 < number_of_cards:

       print(card_deck_x[0])
       del card_deck_x[0]
       c2 += 1
      c2 = 0
      print('\n')
      c1 += 1
  c1 = 0


  while c1 < players:
    print('гравець'+str(c1+1))
    for i  in range(c1,cards_for_this_games,players):
        print(card_deck[i])
        # c2 += 1
    # c2
    print('\n')
    c1 += 1
  c1 = 0

  i = 0
  while i < cards_for_this_games :
      while c1 < players:
          print('гравець' + str(c1 + 1))
          print(card_deck[i])
          c1 += 1
          i += 1
      c1 = 0
