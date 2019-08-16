class Dog:
  #modelling a dog 
  def __init__(self,name,age):
    #initialize the attributes
    self.name=name
    self.age=age
  
  #creating a method sit
  def sit(self):
    #simulate the dog sitting in response to a command
    print(f"{self.name.title()} is now sitting")
  #creating another method rollover
  def roll_over(self):
    print(f"{self.name} is rolling over")

my_dog=Dog('simba',6)
doggi=Dog('tiger',10)
print(f"my dog is {my_dog.age} years and its called {my_dog.name} ")
my_dog.sit()
my_dog.roll_over()
print(f"I loved {doggi.name.title()}, it died when it was {doggi.age}")
doggi.sit()


class Restaurant:
  #modelling a restaurant
  def __init__(self,name,cuisine):
    #initialize the attributes
    self.name=name 
    self.cuisine=cuisine
  #create method
  def describe_restaurant(self):
    print(f"\n{self.name} offers wonderful food called {self.cuisine}")
  def opening_restaurant(self):
    print(f"{self.name} is now open")
  
restaurant=Restaurant('kwa msupa','choma')
print(f"\nIf we go {restaurant.name} we can eat {restaurant.cuisine}")
restaurant.describe_restaurant()
restaurant.opening_restaurant()