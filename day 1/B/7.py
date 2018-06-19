import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Лапін Костянтин\n')
while True:
    home = str(input('Місце проживання: '))
    time_at_home = float(input('Час вдома: '))
    if time_at_home <= 0 :
        print('некоректно введено час вдома ')
    else:
        if  home  == 'Будинок' or home  == 'будинок' :
            if time_at_home > 18:
                print('Рекомендація---В’єтнамське порося')
            elif  10 <=  time_at_home <= 17:
                print('Рекомендація---Собака')
            else:
                print('Рекомендація---Змія')
        elif  home  == 'Квартира' or home  == 'квартира' :
             if time_at_home >= 10:
                print('Рекомендація---Кішка')
             else:
                 print('Рекомендація---Хом’як')
        elif  home  == 'Гуртожиток' or home  == 'гуртожиток' :
             if time_at_home >= 6:
                print('Рекомендація---Рибки')
             else:
                 print('Рекомендація---Мурашник')
        else:
            print('некоректно введено місце проживання')
            
                 
                 
             
                
                
            
