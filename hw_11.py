# Задача 1

class Soda:

    def __init__(self, flavor=None):
        self.flavor = flavor


    def __str__(self):
        if self.flavor:
            return f"У вас газировка с {self.flavor} вкусом"
        else:
            return "У вас обычная газировка"

soda1 = Soda("Cerry")
print(soda1)
soda2 = Soda()
print(soda2)

#Задача 2
class Math:
    def addition(self, a, b):
        result = a + b
        print(f"Результат сложения: {result}")
    def subtraction(self, a, b):
        result = a - b
        print(f"Результат вычитания: {result}")
    def multiplication(self, a, b):
        result = a * b
        print(f"Результат умножения: {result}")
    def division(self, a, b):
        if b != 0:
            result = a / b
            print(f"Результат деления: {result}")
        else:
            print("Ошибка: Деление на ноль!") #
math_operations = Math()
math_operations.addition(5, 3)
math_operations.subtraction(10, 4)
math_operations.multiplication(7, 6)
math_operations.division(8, 2)
math_operations.division(8, 0)

#Задача 3
class Car:
    def __init__(self, color, car_type, year):
        self.color = color
        self.car_type = car_type
        self.year = year

    def start(self): print("Автомобиль заведён")
    def stop(self): print("Автомобиль заглушен")
    def set_year(self, year):
        self.year = year
        print(f"Год выпуска автомобиля обновлён на: {self.year}")

    def set_type(self, car_type):
        self.car_type = car_type
        print(f"Тип автомобиля обновлён на: {self.car_type}")
    def set_color(self, color):
        self.color = color
        print(f"Цвет автомобиля обновлён на: {self.color}")

my_car = Car("красный", "седан", 2020)
my_car.start()
my_car.stop()
my_car.set_year(2021)
my_car.set_type("внедорожник")
my_car.set_color("Blue")