class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def display_info(self):
        return f"{self.year} {self.make} {self.model} with a {self.battery_size}kWh battery."

# Example Usage
electric_car = ElectricCar("Tesla", "Model S", 2023, 100)
print(electric_car.display_info())
