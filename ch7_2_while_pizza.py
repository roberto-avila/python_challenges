#-----Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. Print a message for 
#every topping added.

prompt = ("Which topping would you like to add to your pizza? ")
prompt += ("Type 'quit' once you're done choosing. ")

topping = ""

while topping != 'quit':
    topping = input(prompt)
    #if topping != 'quit':
    print(f"Adding topping: {topping.title()}")

#-----Movie theater where tickets prices are: under age 3, ticket is free. Ages between 3 and 12, ticket is $10. Ages 12 and above, ticket is $15.
#Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

prompt = ("Enter your age to check ticket prices. Enter 'quit' to exit: ")

age = ""

while age != 'quit':
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif age >= 3 and age <= 12:
        print("Your ticket is $10.")
    elif age > 12:
        print("Your ticket is $15.")

#-----Rewrite the first pizza topping program in this challenge, one time using a break, and one time using a flag.

#Flag
prompt = ("Which topping would you like to add to your pizza? ")
prompt += ("Type 'quit' once you're done choosing. ")

active = True

while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"Adding topping: {topping.title()}")

#Break
prompt = ("Which topping would you like to add to your pizza? ")
prompt += ("Type 'quit' once you're done choosing. ")

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"Adding topping: {topping.title()}")

        
