print("Введите день недели: ")
day = int(input())

if day > 0 and day < 8:
    if day < 6:
        print("Будний день")
    else:
        print("Выходной день")
else:
    print("Не верное число")