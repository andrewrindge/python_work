for num in range(1, 21):
    print(num)

onemil = list(range(1, 1_000_001))
#for num in onemil:
#   print(num)

print(min(onemil))
print(max(onemil))

total = sum(onemil)
print(total)

oddnum = range(1, 20, 2)
for num in oddnum:
    print(num)

threes = range(3, 30, 3)
for num in threes:
    print(num)

cubes = []
for num in range(1, 11):
    cubes.append(num ** 3)
for val in cubes:
    print(val)

cubescomp = [value**3 for value in range(1,11)]
print(cubescomp)
