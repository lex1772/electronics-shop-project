from src.item import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv(dir="C:\\Users\\lexa1\\PycharmProjects\\electronics-shop-project\\tests\\file_empty.csv")
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(dir="C:\\Users\\lexa1\\PycharmProjects\\electronics-shop-project\\tests\\test_file_damaged.csv")
    # InstantiateCSVError: Файл item.csv поврежден
