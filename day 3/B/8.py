import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')
morse_d = {'A':'.-','B':'-...','C':'-.-.','D':'   }-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..',
           'J': '.---', 'K': '.-.-','L': '.-..','M': '--' ,'N': '-.','O': '---','P': '.--.','Q': '--.-','R': '.-.',
           'S': '...','T': '-','U': '..-','V': '...-','W': '.--','X': '-..-','Y': '-.--','Z': '--..',
           '0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....',
           '7': '--...','8': '---..','9': '----.',' ':' '}
morse_code_string =''
input_string = str(input('enter string:')).upper()
for char in "?,.!/;:":
    input_string = input_string.replace(char,"")

print(input_string )
for p in input_string:
    morse_code_string += morse_d.get(p)
print('morse_code = ' +  morse_code_string)