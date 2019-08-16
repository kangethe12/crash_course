from user_module import User, Privelege
  
pupil=User('john', 'kangs', 34,7)
pupil.describe_user()
pupil.greetings()
pupil.increment_login_attempts()
pupil.increment_login_attempts()
pupil.increment_login_attempts()
pupil.reset_login_attempts()  


#admin subclass
class Administrator(User):
  def __init__(self,first,last,age,login_attempts):
    #initializing attributes of the parent class
    super().__init__(first,last,age,login_attempts)
    self.priveleges=Privelege()
  

admin=Administrator('dens','joseph',56,8)
admin.describe_user()
admin.priveleges.show_priveleges()