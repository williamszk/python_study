# With property class
class Celsius:
    def __init__(self, temperature=0) -> None:
        self.temperature = temperature

    def to_farenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)


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

