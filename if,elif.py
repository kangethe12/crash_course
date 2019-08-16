age=19
if age<=2:
  stage='baby'
elif age<=4:
  stage='toddler'
elif age<=13:
  stage='kid'
elif age<=18:
  stage='teenager'
else:
  stage='adult'
print(f"This is a {stage}")



fruits=['bananas','oranges','pineapples']
if 'bananas' in fruits:
  print("\nOoooh i love bananas")
elif 'ovacado' in fruits:
  print("I love ovacado more")


pizza=['pilipili']
if pizza:
  for ingredients in pizza:
    print(f"\nJust added {ingredients}")
else:
  print("\nAre you sure you dont want a pizza")


pizza_ingredients=['pilipili','mayai','unga','maji']
ingredients_req=['unga','pilipili','cheese']
for ingredient in ingredients_req:
  if ingredient in pizza_ingredients:
    print(f"\nAdding {ingredient}")
  else:
    print("\nthats not a pizza ingredient")