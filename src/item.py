import csv
from pathlib import Path


class Item:
    """Класс. реализующий представления товара в магазине."""
    pay_rate = 1.0
    all_product = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """Метод, который инициализирует экземпляры класса."""
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all_product.append(self)

    def calculate_total_price(self) -> float:
        """Рассчитывает общую стоимость конкретного товара в магазине."""
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """Применяет установленную скидку для конкретного товара."""
        self.price *= Item.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            name = name[:10]
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Инициализирует экземпляры класса Item данными из CSV - файла.
        """
        current_file_path = Path(__file__)
        file_path = current_file_path.parent.parent / 'src/items.csv'

        with open(file_path, 'r', encoding='utf-8') as file:
            cls.all_product.clear()
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        number = round(float(string))
        return number

    # магические методы
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        return self.quantity + other.quantity
