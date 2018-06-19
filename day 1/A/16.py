import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин\n')

length_field = int(input('введіть довжину поля:'))
width_field = int(input('введіть ширину поля :'))
area_m = length_field*width_field
print('Площа у арах: {:.0f}\nПлоща у гектарах:{:.0f}'.format(area_m/100,area_m/10000))
