pizzas=['kamakis','mutura','choma','njugu']
f_pizzas=pizzas[:]
print(f_pizzas)
pizzas.append('maembe')
f_pizzas.append('pepino')
print(f_pizzas)
print(pizzas)

for pizza in pizzas:
  print(f"my fav pizza is {pizza}")