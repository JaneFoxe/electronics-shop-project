import pytest

from src.keyboard import Keyboard

def test_keyboard_creation():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 9600
    assert kb.quantity == 5


def test_keyboard_change_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"

def test_setting_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    with pytest.raises(AttributeError):
        kb.language = "CH"