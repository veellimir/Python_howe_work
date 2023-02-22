class Rectangle:
    # long = 0
    # width = 0
    # Длинна и ширина квадрата
    def __init__(self, long, width):
        self.long = long
        self.width = width
    # Поиск площади квадрата
    def rectangle_square(self):
        return f'{self.long * self.width}'

    # функц. периметр прямоугольника
    def rectanlge_perimeter(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        return f'{self.a * self.b + self.c * self.d}'

    # Функц. Гипотенуза прямоугольника
    def rectanlge_hypotenuse(self, long_h, width_h):
        self.long_h = long_h
        self.width_h = width_h
        result = (self.long_h ** 2 + self.width_h ** 2) ** 0.5
        return result

    # Метод рисующий прямоугольник
    def rectanlge_paint(self, long_paint, width_paint):
        self.long_paint = long_paint
        self.width_paint = width_paint

        for i in range(long_paint):
            for j in range(width_paint):
                print('*', end='')
            print()


res = Rectangle(3, 9)
print('Площадь прямоугольника :', res.rectangle_square())

print('Периметр прямоугольника :', res.rectanlge_perimeter(3, 9, 3, 9))
print('Гипотенуза прямоугольника :', res.rectanlge_hypotenuse(3, 9))

print(res.rectanlge_paint(3, 9))