#-----Make a class Die with one attribute called sides, which has a default value of 6.
#  Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.
#  Make a 6-sided die and roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die:
    """Model of a die."""

    def __init__(self, sides = 6):
        """Intialize attributes."""
        self.sides = sides
    
    def roll_die(self):
        """Rolls the die."""
        return randint(1,self.sides)

d6 = Die()
results = []

for rolled_number in range(10):
    result = d6.roll_die()
    results.append(result)

print("10 rolls of a 6-sided die result in:")
print(results)

d10 = Die(10)
results = []

for rolled_number in range(10):
    result = d10.roll_die()
    results.append(result)

print("10 rolls of a 10-sided die result in:")
print(results)

d20 = Die(20)
results = []

for rolled_number in range(10):
    result = d20.roll_die()
    results.append(result)

print("10 rolls of a 20-sided die result in:")
print(results)



#-----Make a list or tuple containing a series of 10 numbers and five letters.
#  Randomly select four numbers or letters from the list and print a message saying that any ticket
#  matching these four numbers or letters wins a prize.
print('\n')
from random import choice

lottery_characters = ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

winning_characters = []

while len(winning_characters) < 4:
    draw = choice(lottery_characters)
    if draw not in winning_characters:
        winning_characters.append(draw)

print("The winning draws are:")
print(winning_characters)
print('\n')


#-----You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket.
#  Write a loop that keeps pulling numbers until your ticket wins.
#  Print a message reporting how many times the loop had to run to give you a winning ticket.

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_ticket = []

    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket


def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    ticket = []
    
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


def check_ticket(played_ticket, winning_ticket):
    """
    Check all elements in the played ticket. If any are not in the 
    winning ticket, return False.
    """
    
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    # We must have a winning ticket!
    return True

winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

# Let's set a max number of tries, in case this takes forever!
max_tries = 1_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
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

