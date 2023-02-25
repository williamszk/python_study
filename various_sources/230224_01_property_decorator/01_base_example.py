
# Basic way of setting and getting attributes in Python 
class Celsius:
    def __init__(self, temperature=0) -> None:
        self.temperature = temperature

    def to_farenheit(self):
        return (self.temperature * 1.8) + 32

human = Celsius()

human.temperature = 37

print(f"{human.temperature = }")
print(f"{human.to_farenheit() = }")


print(f"{human.__dict__ = }")

