# EASY EXAMPLE

# Step 1:- Define the product class
"""
class Car:
  def __init__(self, name):
    self.name = name

  def drive(self):
    pass


class Sedan(Car):
  def drive(self):
    return "Sedan car is being driven"


class SUV(Car):
  def drive(self):
    return "SUV car is being driven"

#Step 2 :-Create the factory clas

class CarFactory:
  def create_car(self,car_type):
    if car_type == 'sedan':
      return Sedan("Sedan Car")

    elif car_type == 'suv':
      return SUV("SUV car")

    else:
      raise ValueError("Invalid Car type")

# Step 3 :- Client Code that uses the factory

car_factory = CarFactory()

sedan_car = car_factory.create_car("sedan")
print(sedan_car.drive())

suv_car = car_factory.create_car("suv")
print(suv_car.drive())
"""

#ADVANCED EXAMPLE

#1.Product class
class Product:
  def __init__(self):
    pass
  def method(self):
    raise NotImplementedError

#2.Concrete Product class

class ConcreteProduct1(Product):
  def __init__(self):
    super().__init__()
    print("Creating ConcreteProduct1")
  def method(self):
    print("This is ConcreteProduct1")

class ConcreteProduct2(Product):
  def __init__(self):
    super().__init__()
    print("Creating ConcreteProduct 2")
  def method(self):
    print("This is ConcreteProduct2")


# 3.Creator Class (Abstract Base Class)
class Creator:
  def factory_method(self):
    pass

  def do_something(self):
    # print("SELF ==>",self)
    product = self.factory_method()
    # print("PRODUCT==>",product)
    result = product.method()

# 4. Concrete creator classr

class ConcreteCreator1(Creator):
  def factory_method(self):
    print("INSIDE CONCRETE CREATOR 1")
    return ConcreteProduct1()

class ConcreteCreator2(Creator):
  def factory_method(self):
    print("INSIDE CONCRETE CREATOR 2")
    return ConcreteProduct2()

#5 .Client Code

def client_code(creator):
  creator.do_something()

print("Using ConcreteCreator1")
r

print("Using ConcreteCreator2")
client_code(ConcreteCreator2())