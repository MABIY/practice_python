guests = ['guido van rossum','jack turner','lynn hill']

def  invite_to_dinner():
    print(f"{name},please come to dinner.")
def no_invite_to_dinner():
    print(f"Sorry, {name.title()} there's no room at the table.")
name = guests[0].title()
invite_to_dinner()

name = guests[1].title()
invite_to_dinner()

name = guests[2].title()
invite_to_dinner()

name = guests[1].title()
print(f"\n Sorry, {name} can't make it to dinner.")

del(guests[1])
guests.insert(1,'gary shyder')

#print the invitations again.
name = guests[0].title()
invite_to_dinner()

name = guests[1].title()
invite_to_dinner()
name = guests[2].title()
invite_to_dinner()

# We got a bigger table, so let's add some more people to the list.
print("\n we got a bigger table!")
guests.insert(0,'frida kahlo')
guests.insert(2,'reinhold messner')
guests.append('elizabeth peratrovich')

name = guests[0].title()
invite_to_dinner()
name = guests[1].title()
invite_to_dinner()
name = guests[2].title()
invite_to_dinner()
name = guests[3].title()
invite_to_dinner()
name = guests[4].title()
invite_to_dinner()
name = guests[5].title()
invite_to_dinner()

# Oh no, the tabel won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")
name = guests.pop()
no_invite_to_dinner()

name = guests.pop()
no_invite_to_dinner()

name = guests.pop()
no_invite_to_dinner()

name = guests.pop()
no_invite_to_dinner()

# There should be two people left. Let's invite them.
name = guests[0].title()
invite_to_dinner()

name = guests[1].title()
invite_to_dinner()

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty
print(guests)
