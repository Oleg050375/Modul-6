class Vehicle:  # родительский класс транспортных средств
    __COLOR_VARIANTS = ['Blue', 'Red', 'Yellow']  # список разрешённых цветов

    def __get_model__(self):  # метод получения модели
        return self._Sedan__model

    def __get_horsepower__(self):  # метод получения мощности
        return self._Sedan__engine_power

    def __get_color__(self):  # метод получения цвета
        return self._Sedan__color

    def __print_info__(self):  # метод вывода статуса объекта
        print('Владелец:', self.owner)
        print('Модель:', self.__get_model__())
        print('Мощность:',self.__get_horsepower__())
        print('Цвет', self.__get_color__())

    def __set_color__(self, new_color):  # метод изменения цвета
        a = 0
        for i in self.__COLOR_VARIANTS:  # сверка со списком допустимых цветов
            if i.lower() == new_color.lower():
                self._Sedan__color = new_color  # смена цвета на разрешённый
                a = 1
                break
        if a == 0:
            print('Нельзя изменить цвет на', new_color)

class Sedan(Vehicle):  # дочерний класс
    def __init__(self, owner, model, engine_power, color):
        self.owner = owner  # изменяемый параметр (str)
        self.__model = model  # не изменяемый вручную параметр (str)
        self.__engine_power = engine_power  # не изменяемый вручную параметр (int)
        self.__color = color  # не изменяемый вручную параметр (str)

# ТЕСТ ----------------------------------------------------------------------------------------------------------------

v1 = Sedan('Oleg', 'ZEEKR', 428, 'White')  # объект дочернего класса Sedan

v1.__print_info__()  # смотрим статус объекта

v1.__set_color__('Red')  # смена цвета на цвет из списка разрешённых
v1.__set_color__('Green')  # смена цвета на цвет не из  списка разрешённых

v1.owner = 'Sasha'  # смена собственника
v1.model = 'Avatr'  # попытка смены модели
v1.engine_power = 500  # попытка смены мощности

v1.__print_info__()  # проверка статуса