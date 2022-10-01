print("Введите координаты х: ")
x = int(input())

print("Введите координаты y: ")
y = int(input())

if x != 0 or y != 0:
    if x > 0 and y > 0:
        print("1 четверть")
    elif x < 0 and y > 0:
        print("2 четверть")
    elif x < 0 and y < 0:
        print("3 четверть")
    elif x > 0 and y < 0:
        print("4 четверть")
else:
    print('Координаты точки имеют нулевые значения')