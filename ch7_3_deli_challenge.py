#-----Make a list called sandwich_orders and fill it with various orders for sandwiches. Make an empty list of finished_orders and move
#each sandwich over to the finished_orders. Print the process and results.

sandwich_orders = ['tuna', 'baloney', 'chicken']
finished_orders = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"Making your {order} sandwich now.")
    finished_orders.append(order)
print("\n")
for sandwich in finished_orders:
    print(f"Your {sandwich} sandwich is ready!")

#-----Use the sandwich_orders list from the challenge above and repeat 'pastrami' three times. Point out that the shop is out of pastrami
#and remove the sandwich type using a while loop to make sure it doesn't end up in the finished_orders.

sandwich_orders = ['tuna', 'pastrami', 'baloney', 'pastrami', 'chicken']
finished_orders = []

print("\nSorry everyone, we're out of pastrami today.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"Making your {order} sandwich now.")
    finished_orders.append(order)
print("\n")
for sandwich in finished_orders:
    print(f"Your {sandwich} sandwich is ready!")

#-----Write a program that polls users about their dream vacation location. Print the results of the poll.

polled_users = {}

while True:
    name = input("What's your name? ")
    response = input("What's your dream vacation spot? ")
    polled_users[name] = response
    repeat = input("Would you like to ask someone else? (yes/no) ")
    if repeat == 'no':
        break
print("\n---Poll Results!---")
for name, response in polled_users.items():
    print(f"{name.title()} wants to go to {response.title()}")

