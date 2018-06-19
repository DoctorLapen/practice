import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

printTimeStamp('Лапін Костянтин\n')
while True:
    mouth= str(input('Enter mouth: '))
    day = int(input('Enter day: '))

       
    
    if 22 <= day <= 31 and mouth == 'December' or 1 <= day <= 19 and mouth == 'January' :
        print('Zodiac sign---Capricorn')
    elif 20 <= day <= 31 and mouth == 'January' or 1 <= day <= 18 and mouth == 'February':
        print('Zodiac sign---Aquarius')
    elif 19 <= day <= 29 and mouth == 'February' or 1 <= day <= 20 and mouth == 'March':
        print('Zodiac sign---Pisces')
    elif 21 <= day <= 31 and mouth == 'March' or 1 <= day <= 19 and mouth == 'April':
        print('Zodiac sign---Aries')
    elif 20 <= day <= 30 and mouth == 'April' or 1 <= day <= 20 and mouth == 'May':
        print('Zodiac sign---Taurus')
    elif 21 <= day <= 31 and mouth == 'May' or 1 <= day <= 20 and mouth == 'June':
        print('Zodiac sign---Gemini')
    elif 21 <= day <= 30 and mouth == 'June' or 1 <= day <= 22 and mouth == 'July':
        print('Zodiac sign---Cancer')
    elif 23 <= day <= 31 and mouth == 'July' or 1 <= day <= 22 and mouth == 'August':
        print('Zodiac sign---Leo')
    elif 23 <= day <= 31 and mouth == 'August' or 1 <= day <= 22 and mouth == 'September':
        print('Zodiac sign---Virgo')
    elif 23 <= day <= 30 and mouth == 'September' or 1 <= day <= 22 and mouth == 'October':
        print('Zodiac sign---Libra')
    elif 23 <= day <= 31 and mouth == 'October' or 1 <= day <= 21 and mouth == 'November':
        print('Zodiac sign---Scorpio')
    elif 22 <= day <= 30 and mouth == 'November' or 1 <= day <= 21 and mouth == 'December':
        print('Zodiac sign---Scorpio')    
    else:
        print('EntryError')
