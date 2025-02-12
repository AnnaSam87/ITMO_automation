def function(a,b):
    if a < b:
        print(b)
    else:
        print(a)

function(10,8)



def function1(a,b):
    if a +-135==b or b+-135==a:
        print('Yes')
    else:
        print('No')

function1(143,8)



def function2(a):
    if a ==1 or a==2 or a==12:
        print('Зима')
    elif a in range (3,6):
        print('Весна')
    elif a in range(6, 9):
        print('Лето')
    elif a in range(9, 12):
        print('Осень')
    else:
        print('Такого месяца не существует')

function2(18)



def function3(a,b,c):
    if a >10 and b>10 and c>10:
        print('Yes')
    else:
        print('No')

function3(143,8, 5)



def function5(years:int, months:int) ->int :
   return years*12*29+months*29

print(function5(2,1))