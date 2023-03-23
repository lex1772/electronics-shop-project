import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_phone_init(phone1):
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120_000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2
    phone1.number_of_sim = 0
    assert phone1.number_of_sim == 2
    phone1.number_of_sim = 0.1
    assert phone1.number_of_sim == 2
    phone1.number_of_sim = 3
    assert phone1.number_of_sim == 3


def test_add(phone1, item1):
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    with pytest.raises(ValueError):
        phone1 + 5
