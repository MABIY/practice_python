guests = ['guido van rossum','jack turner','lynn hill']

def  invite_to_dinner():
    print(f"{name},please come to dinner.")

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
