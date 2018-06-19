import datetime
from random import randint
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')
myaccount = 12
mynums = []

myaccount_points = {3:20,4:50,5:500,6:5000,0:0,1:0,2:0}
win_list = []
win= 0

while True:
     start = str(input('бажаєте випробувати вдачу?: ')).upper()
     if start =='ТАК' :
        if 20<=  myaccount:
            myaccount -= 20
            c = 0
            while c < 6:
              num = int(input('введіть число №{} від 1 до 49(числа не повинні повторюватися): '.format(c+1)))
              if num in range(1,49) and num not in mynums:
                  mynums.append(num)
                  c +=1
              else:
                print('помилка вводу !!!')
            c = 0
            while c < 6:
              x = randint(1,48)
              if x not in win_list:
                  win_list.append(x)
                  c += 1
            for i in win_list:
              win += mynums.count(i)

            myaccount += myaccount_points.get(win)

            print('ваші числа: {}\nвиграшна комбінація: {}\nзбігів числ: {}\nрахунок до гри: {} у.о\nвиграш: {} у.о\nрахунок: {} у.о'
                  .format(mynums,win_list,win,myaccount+20-myaccount_points.get(win),myaccount_points.get(win),myaccount))
            mynums.clear()
            win_list.clear()
            win = 0
        else:
            print('недостатньо у.о для гри ')
            break



     elif start =='НІ':
          break
     else:
          print('помилка вводу !!!')