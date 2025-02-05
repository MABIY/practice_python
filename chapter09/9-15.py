from random import choice


def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_ticket = []

    # We don't want to repeat winning numbers or letters, so we'll use a while loop.
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the winning ticket if it hasn't
        # already been pulled
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
    return winning_ticket


def check_ticket(played_ticket,winning_ticket):
    # Check all elements in the played ticket. If any are not in the
    # Winning ticket, return False.
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    # We must have a winning ticket!
    return True

def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    tickets = []
    # We don't want to repeat numbers or letters, so we'll use a while loop
    while len(tickets)< 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the ticket if it hasn't already
        # been pulled
        if pulled_item not in tickets:
            tickets.append(pulled_item)
    return tickets

possibilities = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

# Let's set a max number or tries, in case this  takes forever!
max_tries = 1_000_000
while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket,winning_ticket)
    plays +=1
    if plays >= max_tries:
        break
    if won:
        print("We have a winning ticket!")
        print(f"Your ticket: {new_ticket}")
        print(f"Winning ticket: {winning_ticket}")
        print(f"It only took {plays} tries to win!")
    else:
        print(f"Tried {plays} times, without pulling a winner. :(")
        print(f"Your ticket: {new_ticket}")
        print(f"Winning ticket: {winning_ticket}")



