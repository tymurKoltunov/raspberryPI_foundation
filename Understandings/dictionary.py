

def func_1(x):

    if x % 2 == 0:
        y = True
    else:
        y = False
    print('func1')
    return  y

def func_2(x):
    if x % 3 == 0:
        y = True
    else:
        y = False
    print('func2')
    return y

def func_3(x):
    if x % 5 == 0:
        y = True
    else:
        y = False
    print('func3')
    return y

def switcher( number):

    switch = {
        1: func_1,
        2: func_2,
        3: func_3
    }
    func = switch.get(number, lambda number :'Invalid')
    return func

#print(switcher(5)(5))
#print(switcher(5, 3))
#print(switcher(6, 2))

dic = {"Cheese" : 123}
print("Cheese" in dic)
print(dic["Cheese"])