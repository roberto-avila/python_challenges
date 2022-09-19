#-----Write a program that asks what rental car a customer wants, and print a message for them.

rental_car = input("Which car would you like to rent? ")

print(f"Let me find you a {rental_car.title()}")

#-----Write a program that asks a user how large their party is. If they have more than 8 people, they'll have to wait for a table.

guests = input("How many guests are in your party? ")
guests = int(guests)

if guests > 8:
    print("Sorry, you'll have to wait for a table.")
else:
    print("We have a table ready!")

#-----Ask the user for a number. Point out if it's a multiple of 10.

number = input("Tell me a number and I'll let you know if it's a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print(f"The number {number} is a multiple of 10.")
else: 
    print(f"The number {number} is not a multiple of 10.")