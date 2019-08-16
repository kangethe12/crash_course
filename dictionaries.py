ball={'mpira':'player','food':'eat'}
print (ball['mpira'].upper())
ball['game']='ref'
del ball['food']
print(ball)

alien={'xpos':0,'ypos':25,'speed':'high'}
print(f"\nOriginal position is {alien['xpos']}")

if alien['speed']=='slow':
  x_increment=1
elif alien['speed']=='medium':
  x_increment=2
else:
  x_increment=3
alien['xpos']=alien['xpos'] + x_increment
print(f"\nThe new position is {alien['xpos']}")

#what do you think
languages={
  'central':'kikuyu',
  'nyanza':'luo',
  'western':'luhya',
  'eastern':'kamba',
  'nairobi':'sheng',
}
nairobi_value=languages.get('nairobi','Nairobi doesnt have a language')
for region, language in languages.items():
  print(f"\n {region.title()} fav language is {language.title()}")
print(nairobi_value)


rivers={
  'kenya':'tana',
  'sudan':'juba',
  'brazil':'amazon',
  'egypt':'nile'
}
for country, river in rivers.items():
  print(f"\n {river.title()} runs through {country.title()}")

for river in rivers.values():
  print(f"{river.title()}")