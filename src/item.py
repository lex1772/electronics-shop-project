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
    def instantiate_from_csv(cls, dir="src", file="items.csv"):
        try:
            cls.all = []
            work_dir = os.getcwd()
            dir_correct = work_dir.split("\\")
            if dir_correct[-1] != "electronics-shop-project":
                os.chdir('..')
                work_dir = os.getcwd()
            items = os.path.join(work_dir, dir, file)
            with open(items, 'r', encoding='utf-8') as f:
                csvreader_object = csv.DictReader(f)
                for row in csvreader_object:
                    if len(row) != 3 or None in row:
                        raise InstantiateCSVError
                    else:
                        cls(row.get('name'), int(row.get('price')), int(row.get('quantity')))
        except FileNotFoundError:
            print(f"Отсутствует файл {file}")
            raise
        except InstantiateCSVError:
            print(f"Файл {file} поврежден")
            raise

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

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Employee и дочерние от них.')
        return self.quantity + other.quantity


class InstantiateCSVError(Exception):
    pass
