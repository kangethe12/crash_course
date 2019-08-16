aliens=[]
for alien_num in range(30):
  n_alien={'color':'green','speed':'slow','points':'5'}
  aliens.append(n_alien)
for alien in aliens[:5]:
  print(alien)
print(len(aliens))

for alien in aliens[:3]:
  if alien['color']=='green':
    alien['color']='yellow'
    alien['speed']='medium'
    alien['points']='10'
for alien in aliens[:5]:
  print(alien)


fav_languages={
  'jen':['c','html'],
  'mir':['python','ruby','java'],
  'mut':['ruby','css'],
  'kib':['python']
}
for name, languages in fav_languages.items():
  if len(languages)<2:
    print(f"\n {name.title()} fav language is:")
  else:
   print(f"\n {name.title()} fav languages are:")
  for language in languages:
    print(f"\t {language.title()}")


keny={'kids':'4','rank':'1'}
moi={'kids':'6','rank':'2'}
pres=[keny,moi]
for info in pres:
  print(info)


fav_places={
  'maguts':['mombasa','mwea'],
  'mukoms':['ranga','meru','japan']
}
for name, places in fav_places.items():
  if len(places)<3:
    print(f"\nHi {name} please add more places")
  else:
    print(f"{name.title()} top places are:")
    for place in places:
      print(f"\t{place}")


cities={
  'Nairobi':{
    'country':'kenya',
    'population':'3m',
    'fact':'wizi ni mingi sana'
  },
  'kampala':{
    'country':'uganda',
    'population':'1m',
    'fact':'naskianga pombe ni cheap mbaya'
  },
  'Dar':{
    'country':'tanzania',
    'population':'1.5m',
    'fact':'shobe shobe ni mingi sana'
  }
}
for city, info in cities.items():
  print(f"\n\n\t{city}:")
  
  print(f"country: {info['country'].title()}")
  print(f"population: {info['population'].upper()}")
  print(f"fact: {info['fact'].title()}")
