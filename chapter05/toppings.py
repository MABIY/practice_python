requested_toppings = ['mushrooms', 'green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out ot green peppers right now.")
    else:
        print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")