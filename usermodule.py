class User:
  #modelling the User
  def __init__(self,first,last,age,login_attempts):
    #initializing the attributes
    self.first=first
    self.last=last
    self.age=age
    self.login_attempts=login_attempts
  def describe_user(self):
    print(f"\n{self.first} {self.last} {self.age}")
  def greetings(self):
    print(f"\nHi {self.first} {self.last}")

  def increment_login_attempts(self):
    self.login_attempts +=1
    print(f"login attempts are: {self.login_attempts}")
  
  def reset_login_attempts(self):
    self.login_attempts=0
    print(f"login attempts are: {self.login_attempts}")



class Privelege:
  def __init__(self,priveleges=['can add post','can delete post','can ban user']):
    self.priveleges=priveleges
  def show_priveleges(self):
    print(f"An admin {self.priveleges}")