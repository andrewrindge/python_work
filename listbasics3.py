countries = ["Italy", "Spain", "Morocco", "Greece", "Thailand"]
print(countries)

# Using sorted()

tempsort = sorted(countries)
print(f"Here's the sorted list: {tempsort}")
print(f"And the list value is still: {countries}")

print(sorted(countries,reverse=True))

print(f"And the original list: {countries}")

# Using reverse()

countries.reverse()
print(f"Using reverse, {countries}")
countries.reverse()
print(f"Using reverse again to fix, {countries}")

# Using sort()

countries.sort()
print(f"Using sort, {countries}")
countries.sort(reverse=True)
print(f"Using reverse alphabetical sort, {countries}")

print(f"The length of countries is {len(countries)}")
