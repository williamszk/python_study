from dataclasses import dataclass, field
from datetime import date
from enum import Enum, auto


class OrderStatus(Enum):
    OPEN = auto()
    CLOSED = auto()


@dataclass
class Product:
    name: str = field(compare=True)
    category: str = field(compare=True)
    shipping_weight: float = field(compare=True)
    unit_price: int = field(compare=True)
    tax_percent: float = field(compare=True)

    def __post_init__(self) -> None:
        if self.unit_price < 0:
            raise ValueError("unit_price must be greater than 0.")
        elif self.shipping_weight < 0:
            raise ValueError("shipping_weight must be greater than 0.")
        if not 0 <= self.tax_percent <= 1:
            raise ValueError("tax_percent must be between 0 and 1.")


@dataclass
class Order:
    status: OrderStatus
    creation_date: date = date.today()
    products: list[Product] = field(default_factory=list)

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    @property
    def sub_total(self) -> int:
        return sum((p.unit_price for p in self.products))

    @property
    def tax(self) -> float:
        return sum((p.unit_price * p.tax_percent for p in self.products))

    @property
    def total_price(self) -> float:
        return self.sub_total + self.tax

    @property
    def total_shipping_weight(self) -> float:
        return sum((p.shipping_weight for p in self.products))


def main() -> None:
    products = {
        "banana": Product(
            name="banana",
            category="fruit",
            shipping_weight=0.5,
            unit_price=215,
            tax_percent=0.07,
        ),
        "mango": Product(
            name="mango",
            category="fruit",
            shipping_weight=2,
            unit_price=319,
            tax_percent=0.11,
        ),
        "expensive_mango": Product(
            name="Mango",
            category="fruit",
            shipping_weight=4.0,
            unit_price=800,
            tax_percent=0.20,
        ),
    }

    order = Order(status=OrderStatus.OPEN)
    for product in products.values():
        order.add_product(product)

    print(f"Comparison between mango and expensive mango: {products['mango'] == products['expensive_mango']}")
    print(f"Total order price: {order.total_price/100:.2f}")
    print(f"Subtotal order price: {order.sub_total/100:.2f}")
    print(f"Value paid in taxes: {order.tax/100:.2f}")
    print(f"Total weight order: {order.total_shipping_weight} kg")
    print(f"Comparison between banana and banana: {products['banana'] == products['banana']}")


if __name__ == "__main__":
    main()
