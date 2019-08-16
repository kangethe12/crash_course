guests=['kep','azp','rud']

print (f"Hi {guests[0].title()} welcome to my party")

print (f"\nHi {guests[-1].title()} you are more than welcome to my party")

print (f"\nHave been notified that {guests[2]} will not make to the party so am going to replace him")

guests[2]='pul'
print (f"\nHi {guests[2].title()} welcome to my party")

print('\nHi all i have a bigger table now am adding more')

guests.insert(0,'cab')
guests.insert(2,'jor')
guests.append('abr')
print (f"\nHi {guests[0]}, {guests[2]} and {guests[-1]} welcome to the party")

print('\nHi all the bigger table will be late am removing you guys')

popped_guests=guests.pop(0)
print(f"\nSorry {popped_guests} for the eviction")
popped_guests=guests.pop(2)
print(f"\nSorry {popped_guests} for the eviction")
popped_guests=guests.pop(-1)
print(f"\nSorry {popped_guests} for the eviction")
print(guests)

del guests[0]
del guests[1]
del guests[-1]
print(f"\nSorry{guests} you are all evicted")


print(guests)