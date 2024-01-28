"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


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


def test_repr():
    obj = Item('Ноутбук', 10, 5)
    expected_result = "Item('Ноутбук', 10, 5)"
    result = repr(obj)
    assert result == expected_result


def test_repr_invalid():
    obj = Item('Ноутбук', -5, -10)
    expected_result = "Item('Ноутбук', -5, -10)"
    result = repr(obj)
    assert result == expected_result


def test_repr_empty():
    obj = Item('', 0, 0)
    expected_result = "Item('', 0, 0)"
    result = repr(obj)
    assert result == expected_result


def test_str():
    obj = Item('Ноутбук', 10, 5)
    expected_result = "Ноутбук"
    result = str(obj)
    assert result == expected_result


def test_str_empty_name():
    obj = Item('', 10, 5)
    expected_result = ""
    result = str(obj)
    assert result == expected_result


def test_str_negative_price():
    obj = Item('Ноутбук', -10, 5)
    expected_result = "Ноутбук"
    result = str(obj)
    assert result == expected_result


def test_str_zero_quantity():
    obj = Item('Ноутбук', 10, 0)
    expected_result = "Ноутбук"
    result = str(obj)
    assert result == expected_result


def test_add_():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
