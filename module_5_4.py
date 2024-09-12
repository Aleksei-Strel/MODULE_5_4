class HOUSE:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = object.__new__(cls)
        args = args[0]
        cls.houses_history.append(args)
        return instance

    def __init__(self, name, numb_f):
        self.name = name
        self.number_of_floor = numb_f
        if isinstance(numb_f, HOUSE):
            self.houses_history = numb_f.append()

    def go_to(self, new_floor):
        if int(new_floor) > int(self.number_of_floor) or int(new_floor) < 1:
            print(f'Этажа № {new_floor} не существует')
        else:
            for floor in range(1, new_floor + 1):
                print(int(floor))

    def __del__(self):
        return print(f'{self.name} снесён, но он останется в истории')

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floor}.'

    def __eq__(self, other):
        if isinstance(other, HOUSE):
            return self.number_of_floor == other.number_of_floor
        return False

    def __lt__(self, other):
        if isinstance(other, HOUSE):
            return self.number_of_floor < other.number_of_floor
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, HOUSE):
            return self.number_of_floor <= other.number_of_floor
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, HOUSE):
            return self.number_of_floor > other.number_of_floor
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, HOUSE):
            return self.number_of_floor >= other.number_of_floor
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, HOUSE):
            return self.number_of_floor != other.number_of_floor
        return True

    def __add__(self, value):
        if isinstance(value, int):
            return HOUSE(self.name, self.number_of_floor + value)
        return NotImplemented

    def __radd__(self, value):
        return self.__add__(value)


# Вывод результата по условию задачи

h1 = HOUSE('Скала', 28)
print(HOUSE.houses_history)
h2 = HOUSE('Хрущ', 5)
print(HOUSE.houses_history)
h3 = HOUSE('ЖК Волгарь', 12)
print(HOUSE.houses_history)

# Удаление объектов
del h2
del h3

print(HOUSE.houses_history)
