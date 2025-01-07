# объявление функции
def get_middle_point(x_1, y_1, x_2, y_2):
    x_mid = (x_1+x_2)/2
    y_mid = (y_1+y_2)/2
    return x_mid, y_mid


# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())


# вызываем функцию
x_mid, y_mid = get_middle_point(x_1, y_1, x_2, y_2)
print(x_mid, y_mid)