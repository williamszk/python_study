class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def discount(self, percent):
        self.price = self.price * (1 - percent / 100)

    # Getter
    # def get_price():
    @property
    def price(self):
        print(f"message from the getter: {self._price=}")
        return self._price

    # Setter
    @price.setter
    def price(self, value):
        print(f"message from the setter: {value=}")
        self._price = value


p1 = Product("T-shirt", 50)
p1.discount(10)
# print(p1.price)


# p2 = Product("Mug", "R$15")
# p2.discount(10)
# print(p2.price)
