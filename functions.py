'''def display_message():
  print("Am lerning functions")
display_message()

def fav_book(title):
  print(f"Am using {title} to study python")
fav_book('python crash course')


def pets(typee,name):
  print(f"\nIts a {typee.title()}, it's called {name.title()}")
pets('dog','simba')
pets('bird','parrot')'''


def make_shirt(size='large',message='i love python'):
  print(f"shirt size: {size}")
  print(f"message: {message}")
make_shirt('medium', 'am doing functions')
make_shirt(size='medium')


def cities(city, country='USA'):
  print(f"\n{city} is in {country}")
cities('vegas')
cities('Nairobi', 'kenya')




'''def get_name(first_name,second_name):
  fullname=f"{first_name} {second_name}"
  return fullname.title()
musician=get_name('jose','mashete')
print(musician)


def build_person(first_name,second_name,age=None):
  person={'first':first_name, 'second':second_name}
  if age:
    person['age']=age
  return person
musician= build_person('jose','mashete',27)
print(musician)


def teams(name, nick_name, number=None):
  the_team={'team':name,'nickname':nick_name}
  if number:
    the_team['position']=number
  return the_team
Epl=teams('chelsea','The blues',3)
print(Epl)'''



def get_name(first_name,last_name,middle_name=None):
  fullname=f"{first_name} {last_name}"
  return fullname.title()

while True:
  print("\nPlease tell us your name")
  print(("enter 'q' if you want to quit"))
  f_name=input("first name: ")
  if f_name=='q':
    break
  l_name=input("second name: ")
  if l_name=='q':
    break
  musician=get_name(f_name,l_name)
  print(f"\nhello {musician}")


'''def formatted_name(first_name,last_name):
  fullname=f"{first_name} {last_name}"
  return fullname.title()
#wacha tuingie kwa loop sasa
while True:
  print("\nEnter your name")
  print("(enter 'q' if you want to quit)")
  f_name=input("firstname: ")
  if f_name=='q':
    break
  l_name=input("last name: ")
  if l_name=='q':
    break

  your_name=formatted_name(f_name,l_name)
  print(f"\nMy name is {your_name}")'''
