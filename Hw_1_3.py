print("Введите номер четверти: ")
x = int(input())

if x in [1, 2, 3, 4]:
    if x == 1:
        print("x > 0 & y > 0")
    elif x == 2:
        print("x < 0 & y > 0")
    elif x == 3:
        print("x < 0 & y < 0")
    elif x == 4:
        print("x > 0 & y < 0")
else:
    print('Не в промежутке')