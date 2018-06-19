import datetime
import winsound

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')

melody_list =[(659,250), (659,250), (659,300), (523,250), (659,250), (784,300),
(392,300), (523,275), (392,275), (330,275), (440,250), (494,250),
(466,275), (440,275), (392,275), (659,250), (784,250), (880,275),
(698,275), (784,225), (659,250), (523,250), (587,225), (494,225)]
len_mel = len(melody_list) - 1
i = 0
while  i < len_mel:
 winsound.Beep(melody_list[i][0],melody_list[i][1])
 i += 1