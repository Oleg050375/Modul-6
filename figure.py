import math  # импорт математической библиотеки
class Figure:  # родительский класс фигур
    filled = False  # атрибут закрашенности (bool)
    color = [255, 255, 255]  # фиксированный список цветов RGB (int)

    def __fullnamecolor__(self):  # формирование полного имени для обращения к атрибуту __color
        return '_' + self.__class__.__name__ + '__color'

    def __get_color__(self):  # получение списка цветов RGB
        return getattr(self, self.__fullnamecolor__(), 'нет такого')

    def __is_valid_color__(self, R, G, B):  # проверка корректности задания RGB значений
        return 1 <= R <= 255 and 1 <= G <= 255 and 1 <= B <= 255

    def __set_color__(self, R, G, B):  # задание цвета RGB
        if self.__is_valid_color__(R, G, B):  # проверка на корректность значений RGB
            setattr(self, self.__fullnamecolor__(), [R,G,B])
            print('Установлены новые значения RGB:', self.__get_color__())
        else:
            print('Неверные цветовые значения')

    def __fullname__(self):  # формирование полного имени для обращения к атрибуту __sides
        return '_' + self.__class__.__name__ + '__sides'

    def __is_valid_sides__(self, sides):  # проверка корректности задания сторон
        a = True
        if len(sides) == self.sides_count:  # проверка количенства сторон в общем случае
            for i in sides:
                if isinstance(i, int) and i > 0:  # проверка формата задания длин сторон в общем случае
                    continue
                else:
                    a = False
        elif isinstance(self, Cube) and len(sides) == 1 and isinstance(sides[0], int):  # проверка в случае куба
            pass
        else:
            a = False
        return a

    def __get_sides__(self):  # получение значения атрибута __sides
        return getattr(self, self.__fullname__(), 'нет такого')

    def __len__(self):  # определение периметра фигуры
        return sum(self.__get_sides__())

    def __set_sides__(self, new_sides):  # задание новых сторон
        if self.__is_valid_sides__(new_sides):  # проверка на корректность задания длин сторон
            if isinstance(self, Cube):  # проверка на кубизм )))
                b = new_sides
                for i in range(11):  # формирование нового значения в случае куба
                    b = b + new_sides
                setattr(self, self.__fullname__(), b)
                print('Установлены новые значения длин сторон:', self.__get_sides__())
            else:
                setattr(self, self.__fullname__(), new_sides)  # формировние нового значения в общем случае
                print('Установлены новые значения длин сторон:', self.__get_sides__())
        else:
            print('Неверные значения длин сторон')

class Circle(Figure):  # дочерний класс окружности
    sides_count = 1  # перезадание количества сторон
    radius = 0
    __sides = []
    __color = Figure.color
    def __init__(self, sides, filled):
        self.__sides = sides
        self.filled = filled
        self.radius = self.__sides[0] / 2 / math.pi  # вычисляется из длины окружности, как единственной стороны

    def __get_square__(self):  # вычисление площади круга
        return math.pi * self.radius**2


class Triangle(Figure):  # дочерний класс треугольника
    sides_count = 3  # перезадание количества сторон
    __sides = []
    __color = Figure.color
    def __init__(self, sides, filled):
        self.__sides = sides
        self.filled = filled
    def __get_square__(self):  # вычисление площади треугольника
        p = self.__len__()/2
        s = math.sqrt(p*(p-self.__sides[0])*(p-self.__sides[1])*(p-self.__sides[2]))
        return (s)

class Cube(Figure):  #  дочерний класс куба
    sides_count = 12  # перезадание количества сторон
    __sides = []
    __color = Figure.color
    def __init__(self, sides, filled):
        self.__sides = sides
        self.filled = filled
        for i in range(11):
            self.__sides = self.__sides + sides
    def __get_volume__(self):  # вычисление объёма куба
        return self.__sides[0]**3


# ТЕСТ ----------------------------------------------------------------------------------------------------------------

tri = Triangle([1,2,3], True)
cir = Circle([5], True)
cub = Cube([3], True)

# print(tri.sides_count)
# print(tri.filled)

tri.__set_color__(1, 1, 1)
print(tri.__get_color__())
print(tri.__get_sides__())
tri.__set_sides__([4,5,6])
print(tri.__get_sides__())
print(tri.__len__())
print(tri.__get_square__())

print(cir.radius)
print(cir.__get_square__())
cir.__set_color__(2,2,2)
print(cir.__get_color__())
print(cir.__get_sides__())
cir.__set_sides__([7])
print(cir.__get_sides__())
print(cir.__len__())

print(cub.__get_volume__())
cub.__set_color__(3,3,3)
print(cub.__get_color__())
print(cub.__get_sides__())
cub.__set_sides__([4])
print(cub.__get_sides__())
