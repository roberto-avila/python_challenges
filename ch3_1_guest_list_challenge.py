guests=['ian','chris','emma','david','linda']
for guest in guests:
    print(f'{guest.title()}, you are invited to the party!')


print(f'\nLooks like {guests[3].title()} cannot make it! Let me find a new guest!')

guests[3]='katie'
print(guests)
print(f'\n{guests[3].title()}, you are invited to the party!')

print('\nLooks like we have a bigger table! Let me invite two more people!')

guests.insert(2,'jose')
guests.append('bill')
print(guests)

print(f'\n{guests[2].title()}, you are invited to the party!')
print(f'{guests[6].title()}, you are invited to the party!')

print('\nShoot, they lied! Looks like we got a smaller table instead! I can only invite four people now!')

bye_jose,bye_bill,bye_linda=guests.pop(2),guests.pop(5),guests.pop(4)

print(f'\nSorry {bye_jose.title()}!')
print(f'Sorry {bye_bill.title()}!')
print(f'Sorry {bye_linda.title()}!')
print(f'\n{guests}')
print(f'\nThe number of people going to this party is now {len(guests)}')
print("\nParty's over!")
del guests[3]
del guests[2]
del guests[1]
guests.remove('ian')

print(guests)
