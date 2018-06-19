import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')
i = 0
places = []
while i < 12:
    places.append(True)
    i += 1

print(len(places))
print(places)
n1 = 0
n2 = 6
while places.count(False) != 12:
    place = int(input('Натисніть 1 для першого класу (місця 1-6)'
'Натисніть 2 для економного класу (місця 7-12): '))
    if place == 1:
        while n1 < 6:
            if places[n1] == False:
                pass
            else:
                places[n1] = False
                print('забраньовано місце № ' + str(n1+1)+ ' у першому класі')
                break
            n1 += 1

        if n1 > 5 :
            print('Наступний виліт через 3 години')


    elif place == 2:
        while n2 < 12:
            if places[n2] == False:
                pass
            else:
                places[n2] = False
                print('забраньовано місце № ' + str(n2 + 1) + ' у економ класі ')
                break
        n2 += 1
        if n2 > 12:
            agr = str(input('вільних місць у економ класі немає,бажаєтє забронювати місце у першому класі?'))
            if agr == 'так' and n1 != 5:
                while n1 < 6:
                    if places[n1] == False:
                        pass
                    else:
                        places[n1] = False
                        print('забраньовано місце № ' + str(n1 + 1) + ' у першому класі')
                        break
                n1 += 1
            else:
                print('Наступний виліт через 3 години')



    elif place == 0:
        break
    else:
      print('введення не коректнє')

print(places)