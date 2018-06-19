import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')
thousands = [' тисяча',' дві тисячі',' три тисячі',' чотири тисячі',' п`ять тисяч',' шість тисяч',' сім тисяч',' вісім тисяч',' дев`ять тисяч']
hundreds = [' сто',' двісті',' триста',' чотириста',' п`ятсот',' шістсот',' сімсот',' вісімсот',' дев`ятсот']
decades = [' десять',' двадцять',' тридцять',' сорок',' п`ятдесят',' шістдесят',' сімдесят',' вісімдесят',' девяносто']
decades_11_19 = [' одинадцять',' дванадцять',' тринадцять',' чотирнадцять', ' п`ятнадцять',' шістнадцять',' сімнадцять',' вісімнадцять',' дев`ятнадцять']
ones = [' одна гривня',' дві гривні',' три гривні',' чотири гривні',' п`ять гривень',' шість гривень',' сім гривень',' вісім гривень',' дев`ять гривень']
b = ''
thousands_output = ''
hundreds_output = ''
decades_output = ''
decades_11_19_output = ''
ones_output =' гривень'

num =str(input('введіть  число: '))
if num.isdigit() is False:
        print('введено не число ')
else:
   int_num = int(num)

   if  int_num not in range(1,10001):
    print('введено число поза діапазоном')

   else:
     if len(num) == 5:
       print('десять тисяч гривень')


     else:
             a = 4 - len(num)
             num_op = '0' * a + num

             if int(num_op[0]) != 0:
                thousands_output = thousands[int(num_op[0])-1]
             if int(num_op[1]) !=0 :
                 hundreds_output = hundreds[int(num_op[1]) - 1]
             if  int(num_op[2]) == 1 and int(num_op[3]) != 0 :
                    decades_11_19_output = decades_11_19[int(num_op[3]) - 1]
             else:

                 if int(num_op[2]) != 0:
                   decades_output = decades[int(num_op[2]) - 1]
                 ones_output = ones[int(num_op[3]) - 1]
             output_string = thousands_output + hundreds_output + decades_11_19_output + decades_output + ones_output
             print('{} ---{}'.format(num, output_string))







