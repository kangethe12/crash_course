number=1
while number<=10:
  print (number)
  number+=1

'''prompt="Enter something and i will repeat: "
prompt+="\n Enter 'quit' to end the game: "
message=""
while message!='quit':
  message=input(prompt)
  if message!='quit':
    print(message.title())'''

#Use of flag to stop the loop
'''prompt="Enter something and i will repeat: "
prompt+="\n Enter 'quit' to end the game: "
active=True
while active:
  message=input(prompt)
  if message=='quit':
    active=False
    print("Game over")
  else:
   print(message.title())'''


#Usage of break
'''prompt="Enter something and i will repeat: "
prompt+="\n Enter 'quit' to end the game: "
active=True
while active:
  message=input(prompt)
  if message=='quit':
    break
    print("Game over")
  else:
   print(message.title())'''


'''prompt="Enter Uji ingredients"
prompt+="\nEnter 'quit' to stop adding: "
active=True
while active:
  message=input(prompt)
  if message=='quit':
    active=False
  else:
    print(f"We will add {message}")'''



prompt="Enter 'done' to complete applying"
prompt+="\nwhats your age: "
active=True
while active:
  age=input(prompt)
  if age == 'done':
    break
  age = int(age)
  if age<3:
    print(f"You are {age} years, thats under age, the ticket is free")
  elif age<=12:
    print(f"You are {age} years, the ticket is $10")
  elif age>12:
    print(f"You are {age} years, the ticket is $15")
    
