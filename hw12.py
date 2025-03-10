#Задача 1
class Product:
    def __init__(self, name, store, price):
      self.name = name
      self.store = store
      self.price = price
    def display_info(self):
      print(f"Product: {self.name}, Store: {self.store}, Price: {self.price} rub.")

class Warehouse:
    def __init__(self):
         self.products = []

    def add_product(self, product):
             self.products.append(product)

    def get_product_by_index(self, index):
        if 0 <= index < len(self.products):
            return self.products[index]
        else:
            return "Product not found."

    def get_product_by_name(self, name):
         for product in self.products:
             if product.name == name:
                 return product
             else:
                 return "Product not found."
    def sort_by_price(self):
         self.products.sort(key=lambda product: product.price)
    def display_all_products(self):
         for product in self.products:
             product.display_info()



product1= Product ("Laptop", "Store1", 50000)
product2=Product("Tablet", "Store1", 20000)
product3=Product("Phone", "Store2", 30000)
warehouse = Warehouse()
warehouse.add_product(product3)
warehouse.add_product(product1)
warehouse.add_product(product2)

print("All Products:")
warehouse.display_all_products()
print("\nProduct at index 1:")
product = warehouse.get_product_by_index(1)
if isinstance(product, Product):
    product.display_info()
else: print(product)
print("\nSearching for 'Phone':")
product_by_name = warehouse.get_product_by_name("Phone")
if isinstance(product_by_name, Product):
    product_by_name.display_info()
else: print(product_by_name)
print("\nProducts sorted by price:")
warehouse.sort_by_price()
warehouse.display_all_products()

#Задача 2

class BeeElephant:
    def __init__(self, bee_part, elephant_part):
        self.bee_part = bee_part
        self.elephant_part = elephant_part

    def Fly(self):
        return self.bee_part >= self.elephant_part
    def Trumpet(self):
        if self.elephant_part >= self.bee_part:
            return "tu-tu-doo-doo"
        else: return "wzzzz"
    def Eat(self, meal, value):
        if meal == "nectar":
            if self.elephant_part >= value:
                self.elephant_part -= value
                self.bee_part += value
            else:
                self.bee_part += self.elephant_part
                self.elephant_part = 0
            if meal == "grass":
                if self.bee_part >= value:
                    self.bee_part -= value
                    self.elephant_part += value
                else:
                    self.elephant_part += self.bee_part
                    self.bee_part = 0
                    self.bee_part = min(max(self.bee_part, 0), 100)
                    self.elephant_part = min(max(self.elephant_part, 0), 100)

bee_elephant = BeeElephant(30, 50)
print(bee_elephant.Fly())
print(bee_elephant.Trumpet())
Eat("nectar", 20)
print(bee_elephant.bee_part)
print(bee_elephant.elephant_part)

#Задача 3
class Bus:
    def __init__(self, max_passengers, max_speed):
        self.speed = 0
        self.max_passengers = max_passengers
        self.max_speed = max_speed
        self.passengers = []
        self.has_free_seats = True if max_passengers > 0 else False
        self.seats = {i: None for i in range(1, max_passengers + 1)}

    def board(self, *names):
        for name in names:
            if len(self.passengers) < self.max_passengers:
                if name not in self.passengers:
                    seat_number = self.find_free_seat()
                if seat_number: self.passengers.append(name)
                self.seats[seat_number] = name
                print(f"{name} has boarded the bus.")
            else:
                print(f"No free seats available for {name}.")

            self.update_free_seat_flag()
    def disembark(self, *names):
        for name in names:
            if name in self.passengers:
                self.passengers.remove(name)
                seat_number = self.find_seat_by_name(name)
                self.seats[seat_number] = None
                print(f"{name} has disembarked from the bus.")
            else:
                print(f"{name} is not on the bus.")
                self.update_free_seat_flag()
    def increase_speed(self, value):
        self.speed = min(self.speed + value, self.max_speed)
    def decrease_speed(self, value):
        self.speed = max(self.speed - value, 0)
    def find_free_seat(self):
        for seat_number, occupant in self.seats.items():
            if occupant is None:
                return seat_number
            return None
    def find_seat_by_name(self, name):
        for seat_number, occupant in self.seats.items():
            if occupant == name:
                return seat_number
                return None
    def update_free_seat_flag(self):
        self.has_free_seats = len(self.passengers) < self.max_passengers
    def __contains__(self, name):
        return name in self.passengers
    def __iadd__(self, name):
        self.board(name)
        return self
    def __isub__(self, name):
        self.disembark(name)
        return self

bus = Bus(max_passengers=3, max_speed=100)
bus += "Ivanov"
bus += "Petrov"
print(bus.passengers)
bus.board("Sidorov")
print(bus.has_free_seats)
print(bus.passengers)
bus.increase_speed(50)
print(bus.speed)
bus.decrease_speed(30)
print(bus.speed)
