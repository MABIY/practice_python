prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are finished."

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)

        if age < 3:
            print(" You age in free!")
        elif age < 13:
            print(" Your ticket is $10.")
        else:
            print(" Your ticket is $15.")
