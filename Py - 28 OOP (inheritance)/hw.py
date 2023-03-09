from math import pi

class Pair:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    # Вычисление произведение
    def calculation(self):
        calc = self.A * self.B
        print('Произведение:', calc)

    # Сумма
    def sum(self):
        calc = self.A + self.B
        print('Сумма:', calc)


# Производный класс
class RightTriangle(Pair):
    def hypot(self, A, B, C):
        super().__init__(A, B)
        self.C = C
        print('Прямоугольный треугольник: ', (A, B, C))

    # Вычисление гипотенузы
    def hypot_calculation(self):
        hyp = (self.A ** 2 + self.B ** 2) ** 0.5
        print('Гипотенуза ABC:', '%.2f' % hyp)

    # Площадь треугольника
    def triangle_area(self):
        tr_ar = (self.A * self.B) / 2
        print('Площадь Треугольника ABC:', tr_ar)


result = Pair(5, 8)

result.calculation()
result.sum()

result2 = RightTriangle(2.8, 9)
result2.hypot_calculation()
result2.hypot(5, 8, 9.43)

result3 = RightTriangle(5, 8)
result3.triangle_area()
