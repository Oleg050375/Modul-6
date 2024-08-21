class Animal:  # родительский класс животных
    fed = False  # параметр накормленности по умолчанию
    alive = True  # параметр жизни по умолчанию
    def __eat__(self, food):  # метод употребления пищи
        if food.edible == True:  # проверка на съедобность
            print(self.name, 'cъел', food.name)  # сожрал
            self.fed = True # выжил
        elif food.edible == False:  # проверка на не съедобность
            print(self.name, 'не стал есть', food.name)  # морду воротит
            self.alive = False  # сдох
class Plant:  # родительский класс растений
    edible = False  # параметр съедобности по умолчанию

class Mummal(Animal):  # дочерний класс класса животных
    def __init__(self, name):
        self.name = name
        self.fed = Animal.fed  # стартовое значение параметра накормленности из родительского класса
        self.alive = Animal.alive  # стартовое значение параметра жизни из родительского класса

class Predator(Animal):  # дочерний класс класса животных
    def __init__(self, name):
        self.name = name
        self.fed = Animal.fed  # стартовое значение параметра накормленности из родительского класса
        self.alive = Animal.alive  # стартовое значение параметра жизни из родительского класса

class Flower(Plant):  # дочерний класс цветов
    def __init__(self, name):
        self.name = name

class Fruit(Plant):  # дочерний класс фруктов
    edible = True  # переопределение параметра съедобности
    def __init__(self, name):
        self.name = name

# ТЕСТ ----------------------------------------------------------------------------------------------------------------

a1 = Predator('Ge') # объект дочернего класса Predator
a2 = Mummal('Che') # объект дочернего класса Mummal

p1 = Flower('Romashka') # объект дочернего класса цветов
p2 = Fruit('Apelsin') # объект дочернего класса фруктов

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.__eat__(p1)  # хищник поедает цветок
a2.__eat__(p2)  # травоядное поедает фрукт

print(a1.alive)
print(a2.fed)