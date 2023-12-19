class Item:
    """Класс. реализующий представления товара в магазине."""
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """Рассчитывает общую стоимость конкретного товара в магазине."""
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """Применяет установленную скидку для конкретного товара."""
        self.price *= Item.pay_rate
