# Invite some people to dinner.

guests = ['guido van rossum','jack turner','lynn hill']

def  invite_to_dinner(name):
    print(f"{name},please come to dinner.")


guest_name = guests[0].title()
invite_to_dinner(guest_name)

guest_name = guests[1].title()
invite_to_dinner(guest_name)

guest_name = guests[2].title()
invite_to_dinner(guest_name)

guest_name = guests[1].title()
print(f"\n Sorry, {guest_name} can't make it to dinner.")

# Jack can't make it! Let's invite Gary instead.
del(guests[1])
guests.insert(1,'gary snyder')

# print the invitations again
print("\n")
guest_name = guests[0].title()
invite_to_dinner(guest_name)

guest_name = guests[1].title()
invite_to_dinner(guest_name)

guest_name = guests[2].title()
invite_to_dinner(guest_name)
