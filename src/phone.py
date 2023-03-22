from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Employee и дочерние от них.')
        return self.quantity + other.quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim: int):
        try:
            if type(number_of_sim) != int:
                raise ValueError
            elif number_of_sim <= 0:
                raise ValueError
            else:
                self.__number_of_sim = number_of_sim
        except ValueError:
            print("Количество физических SIM-карт должно быть целым числом больше нуля.")
