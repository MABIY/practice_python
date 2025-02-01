pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

# 概述客户点的披萨
print(f"You ordered a {pizza['crust']}-crust pizza"
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
