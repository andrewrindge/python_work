sliceprac = ['cheese', 'pep', 'hawaiian', 'margherita']
print(f"The first three items in the list are: {sliceprac[:3]}")

print(f"The middle two items in the list are: {sliceprac[1:3]}")

print(f"The last three items in the list are: {sliceprac[1:]}")

friend_pizzas = sliceprac[:]
sliceprac.append('chicken pesto')
friend_pizzas.append('mushroom')
print("My favorite pizzas are:")
for pizza in sliceprac:
    print(pizza)
print("My friends favorite pizza are:")
for pizza in friend_pizzas:
    print(pizza)
