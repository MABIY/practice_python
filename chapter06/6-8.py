# make the empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type':'python',
    'name':'john',
    'owner':'guido',
    'weight':43,
    'eats':'bugs',
}

pets.append(pet)

pet = {
    'animal type':'chicken',
    'name':'clarencee',
    'owner':'tiffany',
    'weight':2,
    'eats':'seeds',
}
pets.append(pet)

pet = {
    'animal type':'dog',
    'name':'peso',
    'owner':'eric',
    'weight':37,
    'eats':'shoes',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}")
    for k,v in pet.items():
        print(f"\t{k}: {v}")