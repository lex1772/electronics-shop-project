import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        try:
            if len(name) < 10:
                self.__name = name
        except len(name) >= 10:
            print(f'Длина наименования товара превышает 10 символов')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        os.chdir('..')
        work_dir = os.getcwd()
        items = os.path.join(work_dir, 'src', 'items.csv')
        with open(items, 'r', encoding='utf-8') as file:
            csvreader_object = csv.DictReader(file)
            for row in csvreader_object:
                cls.all.append(row)


    @staticmethod
    def string_to_number(string):
        return int(string)

