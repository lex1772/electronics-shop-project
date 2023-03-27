import pytest
from src.keyboard import Keyboard

@pytest.fixture
def kb():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard_init(kb):
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 9600
    assert kb.quantity == 5
    assert kb.language == "EN"

def test_change_lang(kb):
    assert kb.change_lang() == "RU"
    assert kb.change_lang().change_lang() == "RU"
    with pytest.raises(AttributeError):
        kb.language = "UZ"