pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
cat = 'cat'
while cat in pets:
    pets.remove(cat)

print(pets)
