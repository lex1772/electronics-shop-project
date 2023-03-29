"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def direction_correct():
    return "C:\\Users\\lexa1\\PycharmProjects\\electronics-shop-project\\tests\\test_corect_items.csv"


@pytest.fixture
def direction_empty():
    return "C:\\Users\\lexa1\\PycharmProjects\\electronics-shop-project\\tests\\file_empty.csv"


@pytest.fixture
def direction_damaged():
    return "C:\\Users\\lexa1\\PycharmProjects\\electronics-shop-project\\tests\\test_file_damaged.csv"


def test_item_init(item1):
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


def test_apply_discount(item1):
    item1.apply_discount()
    assert item1.price == 10000


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_name_setter(item1):
    assert item1.name == 'Смартфон'


def test_instantiate_from_csv(item1, direction_correct, direction_empty, direction_damaged):
    Item.instantiate_from_csv(dir=direction_correct)
    assert len(Item.all) == 5
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(dir=direction_empty)
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(dir=direction_damaged)


def test_string_to_number(item1):
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('a') == None


def test_repr(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str(item1):
    assert str(item1) == 'Смартфон'
