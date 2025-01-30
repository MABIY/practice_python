locations = ['himalaya','andes','tierra del fuego','labrador','guam']
print('Original order:')
print(locations)

print("\n Alphabetical:")
print(sorted(locations))

print("\n Original order:")
print(locations)

print("\nReverse alphabetical:")
print(sorted(locations,reverse=True))

print("\n Original order")
print(locations)

print("\n Reversed")
locations.reverse()
print(locations)

print("\n Original order:")
locations.reverse()
print(locations)

print("\nAlphabetical")
locations.sort()
print(locations)

print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)