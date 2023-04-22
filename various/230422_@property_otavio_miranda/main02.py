from dataclasses import dataclass


@dataclass
class Product:
    # def __init__(self, name, price) -> None:
    #     self.name = name
    #     self.price = price
    name: str
    price: float

    def discount(self, percent):
        self.price = self.price * (1 - percent / 100)

    # Getter
    # def get_price():
    @property  # type: ignore
    def price(self):
        # print(f"message from the getter: {self._price=}")
        return self._price

    # Setter
    @price.setter
    def price(self, value: float):
        # print(f"message from the setter: {value=}")

        new_value = value
        # if type(value) is str:
        if isinstance(value, str):
            new_value = new_value.replace("R$", "")
            new_value = new_value.replace("RS", "")
            new_value = float(new_value)

        self._price = new_value

    @property  # type: ignore
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        # print(f"Calling setter for name: {value=}")
        # new_value = value.capitalize()
        new_value = value.title()
        self._name = new_value


p1 = Product("T-SHIRT", 50)
p1.discount(10)
print(f"{p1.name=}, {p1.price=}")


p2 = Product("MUG", "R$15")  # type: ignore
p2.discount(10)
print(f"{p2.name=}, {p2.price=}")
