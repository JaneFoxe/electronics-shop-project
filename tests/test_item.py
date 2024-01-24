"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def position():
    return Item("Смартфон", 100, 1)


def test_item_init(position):
    assert position.name == "Смартфон"
    assert position.price == 100
    assert position.quantity == 1


def test_calculate_total_price(position):
    assert position.calculate_total_price() == 100


def test_apply_discount(position):
    Item.pay_rate = 0.8
    position.apply_discount()
    assert position.price == 80


def test_apply_discount2(position):
    Item.pay_rate = 1.5
    position.apply_discount()
    assert position.price == 150


def test_instantiate_from_csv():
    Item.all.clear()  # Очищаем объекты перед каждым тестом
    file_path = 'test_items.csv'  # Путь к тестовому CSV-файлу
    Item.instantiate_from_csv(file_path)

    # Проверяем, что список объектов класса не пустой
    assert len(Item.all) > 0

    # Проверяем, что объекты корректно инициализированы из CSV-файла
    for item in Item.all:
        assert isinstance(item, Item)
        assert isinstance(item.name, str)
        assert isinstance(item.price, float)
        assert isinstance(item.quantity, int)
        assert item.name != ''
        assert item.price > 0
        assert item.quantity >= 0


def test_string_to_number_with_integer():
    string = "10"
    expected_result = 10
    result = Item.string_to_number(string)
    assert result == expected_result


def test_string_to_number_with_float():
    string = "3.14"
    expected_result = 3
    result = Item.string_to_number(string)
    assert result == expected_result


def test_string_to_number_with_negative_number():
    string = "-5.7"
    expected_result = -6
    result = Item.string_to_number(string)
    assert result == expected_result


def test_string_to_number_with_invalid_string():
    string = "abc"
    with pytest.raises(ValueError):
        Item.string_to_number(string)
