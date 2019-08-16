from random import choice
players=[5,7,1,6,5,'kangs','deno','dougie','becks','kipto']

winners=[]
print("The winning tickets are")
#to avoid repeating a ticket we use while loop

while len(winners)<4:
  winner=choice(players)
#only append a player to the winners if they have not been repeated
#we use if not in
  if winner not in winners:
    
    winners.append(winner)
    print(winner)