import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Лапін Костянтин')

def hotel_cost(night,price):
     return  night*price
def transport_cost(city):
    d = {'КИЇВ':10,'ПАРИЖ':80,'НЬЮ-ЙОРК':800,'САН-ФРАНЦИЗКО':1000,'МІНЬСК':30}
    return d.get(city.upper())*2
def  rent_a_car(day):
    cost = day*20
    if day < 7:
        cost -= 25
    if 3 <= day < 7:
        cost -= 10
    return cost
def all_travel_cost(day,price,city,own_exp):
    return hotel_cost(day,price) +transport_cost(city)+rent_a_car(day)+ own_exp
print(all_travel_cost(13,25,'ПАРИЖ',200))

