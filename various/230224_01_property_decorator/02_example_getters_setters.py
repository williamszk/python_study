# With getters and setters
class Celsius:
    def __init__(self, temperature=0) -> None:
        self.set_temperature(temperature)

    def to_farenheit(self):
        return (self.get_temperature() * 1.8) + 32
    
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value

human = Celsius(37)

# human.temperature = 37

print(f"{human.get_temperature() = }")
print(f"{human.to_farenheit() = }")

print(f"{human.__dict__ = }")
print(f"{type(human.__dict__) = }")
print(f"{human.__dict__['_temperature'] = }")

try:
    human.set_temperature(-300)
except ValueError as e:
    print(e)


