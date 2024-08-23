class Horse:  # родительский класс лошадей
    x_distance = 0  # параметр дистанции
    sound = 'Frrr'  # фырканье лошади
    def __run__(self, dx): # метод побежали
        self.x_distance += dx

class Eagle:  # родительский класс орлов
    y_distance = 0  # параметр высоты
    sound = 'Chirik-chik-chik'  # чириканье орла )))
    def __fly__(self, dy):  # метод полетели
        self.y_distance += dy

class Pegasus(Eagle, Horse):  # дочерний класс пегасов
    def __init__(self):
        pass
    def __move__(self, dx, dy):  # метод перемещения в пространстве
        self.__run__(dx)
        self.__fly__(dy)
    def __get_pos__(self):  # метод определения текущей позиции
        return (self.x_distance, self.y_distance)
    def __voice__(self):  # метод покричим
        print(self.sound)

# ТЕСТ ----------------------------------------------------------------------------------------------------------------

p1 = Pegasus()  # объект класса пегас

print(p1.__get_pos__())  # посмотрим стартовую позицию

p1.__move__(10, 15)  # переместимся

print(p1.__get_pos__())  #  посмотрим позицию после перемещения

p1.__move__(-5, 20)  # ещё переместимся

print(p1.__get_pos__())  #  посмотрим новую позицию

p1.__voice__()  #  спой, птичка, спой

print(Pegasus.mro())