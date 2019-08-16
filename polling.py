unconfirmed_users=['alice','bobby','zack','zack']
confirmed_users=[]
while unconfirmed_users:
  current_user=unconfirmed_users.pop()
  print(f"Hi {current_user.title()} you are now verified")
  confirmed_users.append(current_user)
print("\nThis is the list of confirmed users:")
for current_user in confirmed_users:   
  print(f"\t {current_user}")
while 'zack' in confirmed_users:
  confirmed_users.remove('zack')
print("New listing")
for current_user in confirmed_users:   
  print(f"{current_user}")



responses={}
polling_active=True
while polling_active:
  name=input("\nWhat's your name: ")
  response=input("\nWhich mountain would you like to climb: ")
  responses[name]=response
  repeat=input("would you like another person to take the poll?(y/n): ")
  if repeat=='n':
    polling_active=False
print("...This are the results...")
for name, response in responses.items():
  print(f"{name.title()} would love to climb {response}")