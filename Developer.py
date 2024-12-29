class House:
    def __init__(self, name, number):
        self.name = name
        self.number_of_floors = number

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor+1):
                print(floor)
        else:
            print('Такого этажа не существует')

h1 = House('ЖК Фридланд', 6)
h2 = House('русская Европа', 7)

h1.go_to(7)
h2.go_to(4)