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
            if len(self.__name) < 10:
                self.__name = name
            if len(self.__name) >= 10:
                raise Exception
        except Exception:
            print("Длина наименования товара превышает 10 символов.")

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
                cls(row.get('name'), int(row.get('price')), int(row.get('quantity')))

    @staticmethod
    def string_to_number(string):
        try:
            int_to_str = int(string)
            return int_to_str
        except ValueError:
            list_for_count = list(string)
            count = list_for_count.count('.')
            if count == 1:
                list_for_count.pop(list_for_count.index('.'))
                counter = 0
                for i in list_for_count:
                    if i.isdigit():
                        counter += 1
                if counter == len(list_for_count):
                    int_to_str = float(string)
                    int_to_str = int(int_to_str)
                    return int_to_str
                else:
                    print('Переданная строка не является числом')
            else:
                print('Переданная строка не является числом')
