from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, n_sim):
        """
        Сеттер для переменной number_of_sim с проверкой на целое и положительное число
        """
        # проверяем на целое число
        if not isinstance(n_sim, int):
            raise ValueError('Количество физических SIM-карт должно быть целым числом')
        # проверяем на положительное число
        if n_sim < 1:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        self.__number_of_sim = n_sim

    # магические методы
    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity
