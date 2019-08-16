sandwiches_orders=['mayai','mutura','pastrami','choma','pastrami','pastrami']
finished_orders=[]
while sandwiches_orders:
  sandwich=sandwiches_orders.pop()
  print(f"I love eating {sandwich}")
  finished_orders.append(sandwich)
for sandwich in finished_orders:
  print(f"\nNow am finished with {sandwich}")
  
while 'pastrami' in finished_orders:
  finished_orders.remove('pastrami')
print(finished_orders)



responses={}
poll_active=True
while poll_active:
  name=input("\nWhat's name?: ")
  destination=input("\nWhat's your favourite destination: ")
  responses[name]=destination
  repeat=input("\nWould you like you friend to take this poll(yes/no): ")
  if repeat=='no':
    poll_active=False
print("...poll results...")
for name,destination in responses.items():
  print(f"{name.title()} would love to travel to {destination.title()}")