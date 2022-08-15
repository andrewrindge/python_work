motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Modifying list elements

motorcycles[0] = 'ducati'
print(motorcycles)

# Adding list elements

motorcycles.append('honda')
print(motorcycles)

# Starting with an empty list

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Adding list elements (in the middle)

motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing using del

del motorcycles[0]
print(motorcycles)

# Removing using .pop()

last = motorcycles.pop()
print(motorcycles)
print(last)

# Removing based on value
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)
