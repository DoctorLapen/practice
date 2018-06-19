import datetime
import winsound

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')

melody_list =[(440,500), (440,500), (440,500), (349,350), (523,150), (440,500), (349,350),
(523,150), (440,1000), (659,500), (659,500), (659,500), (698,350), (523,150),
(415,500), (349,350), (523,150), (440,1000)]
len_mel = len(melody_list) - 1
i = 0
while  i < len_mel:
 winsound.Beep(melody_list[i][0],melody_list[i][1])
 i += 1