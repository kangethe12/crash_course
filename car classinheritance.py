class Car:
  def __init__(self,make,model):
    self.make=make
    self.model=model
    self.odometer_reading=5

  def descriptive(self):
    describe=f"\n{self.make} {self.model}"
    return describe
  
  def odometer(self):
    print(f"\nOdometer reading is {self.odometer_reading}")

  def update_odometer(self,mileage):
    #reject roll back of the odometer
    if mileage>=self.odometer_reading:
      self.odometer_reading=mileage
    else:
      print("You can't roll back an odometer")

  def increment_odometer(self,miles):
    #add the given amount to the current reading
    self.odometer_reading+=miles

my_car=Car('bmw','x6')
print(my_car.descriptive())
my_car.odometer_reading=30
my_car.update_odometer(47)
my_car.odometer()

used_car=Car('toyota','probox')
print(used_car.descriptive())
my_car.update_odometer(345)
my_car.odometer()
my_car.increment_odometer(55)
my_car.odometer()



#have commented this code to experiment on class battery
#creating a sub class through inheritance
'''class Electriccar(Car):
  def __init__(self,make,model,capacity):
    #initializing attributes of the parent class
    super().__init__(make,model)
    #iniialize atrributes specific to electric Car
    self.battery_size=75
    self.capacity=capacity
  def describe_battery(self):
    print(f"\nThe size of the battery is {self.battery_size}")
    #This method overides the original method in the parent class
  def descriptive(self):
    print(f"{self.make} {self.model} {self.capacity}")
tesla_car=Electriccar('musk','tesi',7)
print(tesla_car.descriptive())
tesla_car.describe_battery()

my_ride=Electriccar('Ellon','tesla',5)
my_ride.descriptive()'''


class Battery:
  #modelling a battery away from the subclass electric Car since the Battery methods look long
  def __init__(self,battery_size=75):
    self.battery_size=battery_size
  #a new method to describe Battery
  def describe_battery(self):
    print(f"The battery is {self.battery_size} Kw")
  def get_range(self):
    #printing the range which the Battery provides
    if self.battery_size==75:
      rangee=200
    elif self.battery_size==100:
      rangee=300
    print(f"this car can go about {rangee} miles on full charge")
  #upgrading the Battery to 100
  def upgrage_battery(self):
    #check if battery is 100
    if self.battery_size!=100:
      self.battery_size=100
    else:
      print("The Battery is 100 already")


class Electriccar(Car):
  def __init__(self,make,model,capacity):
    #initializing attributes of the parent class
    super().__init__(make,model)
    #iniialize atrributes specific to electric Car
    self.battery=Battery()
    self.capacity=capacity
    #This method overides the original method in the parent class
  def descriptive(self):
    print(f"{self.make} {self.model} {self.capacity}")
tesla_car=Electriccar('musk','tesi',7)
print(tesla_car.descriptive())
tesla_car.battery.describe_battery()
tesla_car.battery.get_range()

my_ride=Electriccar('Ellon','tesla',5)
my_ride.descriptive()
my_ride.battery.describe_battery()
my_ride.battery.get_range()
my_ride.battery.upgrage_battery()
my_ride.battery.describe_battery()
my_ride.battery.get_range()

