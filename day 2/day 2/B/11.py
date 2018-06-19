import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')
phone_book = {1:{'name':'Пожежна безпека','phone_number':'101'},2:{'name':'Поліція','phone_number':'102'},3:{'name':'Швидка допомога','phone_number':'103'}}
print('{}---{}'.format(phone_book[1]['name'],phone_book[1]['phone_number']))
print('{}---{}'.format(phone_book[2]['name'], phone_book[2]['phone_number']))
print('{}---{}'.format(phone_book[3]['name'], phone_book[3]['phone_number']))
while True:
    choice_act = int(input('1-add contact ,2-del contact,3-edit contact, 4-show phone book,5- exit: '))
    if choice_act == 1 :
        name = str(input('enter  name: '))
        phone_number  = str(input('enter phone_number : '))
        phone_book[len(phone_book)+1] = {'name': name,'phone_number': phone_number }
    elif choice_act == 2:
        key = int(input('enter contact key: '))
        phone_book.pop(key)
    elif choice_act == 3:
        key = int(input('enter contact key: '))
        print('{}---{}'.format(phone_book[key]['name'], phone_book[key]['phone_number']))
        choice_edit = str(input('choice_edit_field ')).upper()
        if choice_edit == 'ALL':
            name = str(input('enter new name: '))
            phone_number = str(input('enter new phone number : '))
            phone_book[key] = {'name': name, 'phone_number': phone_number}
        elif   choice_edit =='NAME':
            name = str(input('enter new name: '))
            phone_book[key] = {'name': name, 'phone_number':phone_book[key]['phone_number'] }
        elif choice_edit == 'NUMBER':
            phone_number = str(input('enter new phone number : '))
            phone_book[key] = {'name':phone_book[key]['name'] , 'phone_number':phone_number }

    elif choice_act == 4:
        for i in phone_book:
            print('{}---{}'.format(phone_book[i]['name'], phone_book[i]['phone_number']))
    elif choice_act == 5:
        print('The End!!!')
        break
