# propety as decorator
class Celsius:
    def __init__(self, temperature=0) -> None:
        self.temperature = temperature

    def to_farenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value


human = Celsius(37)

# human.temperature = 37

print(f"{human.temperature = }")
print(f"{human.to_farenheit() = }")

print(f"{human.__dict__ = }")
print(f"{type(human.__dict__) = }")
print(f"{human.__dict__['_temperature'] = }")

try:
    human.temperature = -300
except ValueError as e:
    print(e)

