magari=['mercedenz','prado','porsche','probox','honda']

print(f"I would like to own a {magari[1].title()} and a {magari[-3].title()}")

magari.append('bmw')
print(magari)

magari.insert(2,'v6')
print(magari)

del magari[-2]
print(magari)

#using pop now 
#if you want to use an item as you remove it, use the pop() method.

popped_garis=magari.pop(2)
print (f"\nI just removed {popped_garis} from the list")
print(magari)

expe='prado'
magari.remove(expe)
print(f"\nYou know {expe} sometimes is very expensive")
