sandwich_orders= ['veggie','grilled cheese','turkey','roast beef']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich." )
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")

alien_0 = {}
alien_0['y'] ='green'
alien_0['y'] = 'value'

for item,value in alien_0.items():
    print(item,value)