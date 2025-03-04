# Батьківський клас (базовий)
class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self):
        """Базовий метод, який буде перевизначений у підкласах"""
        return "Some generic sound"

# Дочірній клас (наслідує Animal)
class Dog(Animal):
    def make_sound(self):
        """Перевизначення методу make_sound для класу Dog"""
        return "Woof! Woof!"

# Ще один дочірній клас
class Cat(Animal):
    def make_sound(self):
        """Перевизначення методу make_sound для класу Cat"""
        return "Meow!"