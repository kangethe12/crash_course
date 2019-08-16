def sandwich_maker(*ingredients):
  print("A sandwich needs the following ingredients:")
  for ingredient in ingredients:
    print(f"-{ingredient}")


def build_person(first,last,**profile):
  #building the dictionary
  profile['firstname']=first
  profile['lastname']=last
  return profile