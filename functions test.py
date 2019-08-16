'''def city_country(city, country):
  city_combination=f"{city}, {country}"
  return city_combination
while True:
  print("\nEnter the city and the country")
  print("(press 'q' if you want to opt out)")
  city=input("\nCity: ")
  if city=='q':
    break
  country=input("Country: ")
  if country=='q':
    break
  city_country=city_country(city, country)
  print(f'\n"{city}", "{country}"')'''


def make_album(name, album, number=None):
  artiste={'artiste_name': name, 'artiste_album': album}
  if number:
    artiste['songs']=number
  return artiste
while True:
  print("\nEnter artiste name and the album:")
  print("(press 'q' to opt out)")
  name=input("\nArtiste name: ")
  if name=='q':
    break
  album=input("Album: ")
  if album=='q':
    break
  albume=make_album(name,album)
  print(f"\n{name} are relising an album called {album}")




  #another subtopic
def greetings(names):
  for name in names:
    message=f"Hi {name}"
    print(message)
people=['ken','kaka']
greetings(people)


unprinted_designs=['kangs', 'dans', 'luochs']
printed_designs=[]
while unprinted_designs:
  design=unprinted_designs.pop()
  print (f"\ncompleted design: {design}")
  printed_designs.append(design)
print("\n...printed....")
for design in printed_designs:
  print(design)



def yet_designs(unprinted_designs, printed_designs):
  while unprinted_designs:
    design=unprinted_designs.pop()
    print (f"\ncompleted design: {design}")
    printed_designs.append(design)
def done_designs(printed_designs):
  print("\n...printed....")
  for design in printed_designs:
    print(design)

unprinted_designs=['kangs', 'dans', 'luochs','dougs']
printed_designs=[]

yet_designs(unprinted_designs, printed_designs)
done_designs(printed_designs)'''

#8.9
def show_messages(messages):
  for message in messages:
    print(message)

mmesages=['need u','love u']
show_messages(mmesages)

#8.10
def send_messages(unsent,sent):
  while unsent:
    msg=unsent.pop()
    print(f"\nmessage: {msg}")
    sent.append(msg)
def show_msgs(sent):
  print("\n...this are sent messages..")
  for msg in sent:
    print(msg)

unsent=['you cute','such adorable']
sent=[]
send_messages(unsent,sent)
show_msgs(sent)
print(unsent)


#passing a copy of the original list
def send_messages(unsent,sent):
  while unsent:
    msg=unsent.pop()
    print(f"\nmessage: {msg}")
    sent.append(msg)
def show_msgs(sent):
  print("\n...this are sent messages..")
  for msg in sent:
    print(msg)

unsent=['you cute','such adorable']
sent=[]
send_messages(unsent[:],sent)
show_msgs(sent)
print(unsent)