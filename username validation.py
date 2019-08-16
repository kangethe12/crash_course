current_users=['kangs','kibs','beks','dougs']
new_users=['KANGS','kengs','odors','kips','beks']
current_users_lookup = {user.lower() for user in current_users}
for user in new_users:
  if user.lower() in current_users:
    print(f"\nHi {user}, you will need to provide a new username")
  else:
    print(f"\nHi {user}, thats a cool username")

#another test

numbers=[1,2,3,4,5,6,7,8,9]
for number in numbers:
  if number==1:
    print("1st")
  elif number==2:
    print("2nd")
  elif number==3:
    print ("3rd")
  else:
    print(f"{number}th")