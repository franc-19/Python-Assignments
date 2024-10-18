import math

class Temperature:
    def convert_fahrenheit(self, celsius):
        if not isinstance(celsius, (int, float)):
            return "Invalid input: Please enter a numeric value."
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    def convert_celsius(self, fahrenheit):
        if not isinstance(fahrenheit, (int, float)):
            return "Invalid input: Please enter a numeric value."
        celsius = (fahrenheit - 32) * 5/9
        return celsius

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

# User input for temperature conversion
temperature = Temperature()
celsius_value = float(input("Enter temperature in Celsius: "))
fahrenheit_value = temperature.convert_fahrenheit(celsius_value)
print(f"{celsius_value} degrees Celsius is equal to {fahrenheit_value:.2f} degrees Fahrenheit")