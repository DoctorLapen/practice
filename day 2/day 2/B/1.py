import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')
D_prov = {'A' : 'Newfoundland','B':'Nova Scotia','C':'Prince Edward Island','E':'New Brunswick','G':'Quebec','H':'Quebec',
'J':'Quebec','K':'Ontario','L':'Ontario','M':'Ontario','N':'Ontario','P':'Ontario','R':'Manitoba','S':'Saskatchewan',
'T':'Alberta','V':'British Columbia','X': 'Nunavut або Northwest Territories', 'Y': 'Yukon' }
result =''
try:
  global post_index
  post_index = str(input('введіть поштоввий код: '))
except:
     print('введено не коректний тип даних')
if len(post_index)== 6:
 if  post_index[0] not in 'ABCDEGHJKLMNPRSTVXY':
    print('введено не коректний код')
 elif post_index[1] not in '0123456789':
    print('введено не коректний код')
 elif post_index[2] not in 'ABCDEGHJKLMNPRSTVXYDFIOQUWZ':
    print('введено не коректний код')
 elif post_index[3] not in '0123456789':
    print('введено не коректний код')
 elif post_index[4] not in 'ABCDEGHJKLMNPRSTVXYDFIOQUWZ':
    print('введено не коректний індекс')
 elif post_index[5] not in '0123456789':
    print('введено не коректний код')
 else:
    if post_index[0] in D_prov :
        prov = D_prov.get(post_index[0])
        if post_index[1] == '0':
             print('поштовий код вказує на село в ' + prov)
        else:
            print('поштовий код вказує на місто в ' + prov)
else:
    print('довжина  кода  не дорівнює 6')