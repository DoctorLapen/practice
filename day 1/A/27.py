import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Лапін Костянтин\n')

while True:
    talk_status= str(input('папуга говорить? : '))
    if talk_status == 'так' or talk_status == 'Так' :
      time_cor = float(input('котра година?(формат гг.хх): '))
      if 22.00 <= time_cor <= 24.00 or 00.00 <= time_cor < 8.00:
         print('Рекомендація--- накрити клітку')
      else:
         print('Рекомендація--- не треба накривати клітку')
    elif talk_status == 'ні' or talk_status == 'Ні' :
        print('Рекомендація--- не треба накривати клітку') 
    else:
        print('Не правельні дані!!!') 
    
