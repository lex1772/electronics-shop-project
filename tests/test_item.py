"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


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


def test_instantiate_from_csv(item1):
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number(item1):
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('a') == None
