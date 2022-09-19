#-----Make a list of five users, including admin. Loop thru the list to print a greeting, but make a special greeting
#for the admin

users=['christina', 'roberto', 'admin', 'david', 'linda']
for user in users:
    if user=='admin':
        print(f'Welcome {user.title()}, you have full access to the system!')
    else:
        print(f'Welcome, {user.title()}!')

#-----Add an if test to the greeting list you just made to check if the list is empty. If it is, print a message.

users=[]
if users:
    for user in users:
        if user=='admin':
            print(f'Welcome {user.title()}, you have full access to the system!')
        else:
            print(f'Welcome, {user.title()}!')
else:
    print('\nWait, there are no users!')

#-----Make a list of 5 users called current_users, and 5 users called new_users. A couple users should overlap between lists.
#Loop thru the new_users list to see which usernames are taken and which are available. new_users list should be compared
#against the current_users lists in a case insensitive manner (tip: create a lower case version of the current_users list
#using list comprehension, and then compare each new_user.lower() against that list)

current_users=['Roberto', 'emma', 'ian', 'christina', 'Linda']
new_users=['roberto', 'Dan', 'Emma', 'david', 'Morgan']

current_users_lower=[current_user.lower() for current_user in current_users]

#as an alternative to the list comprehension above, you could also use a for loop (tho the list comprehension is more concise)
#*********************
current_users_lower=[]
for current_user in current_users:
    current_users_lower.append(current_user.lower())
#*********************

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'Sorry, the username {new_user} is not available.')
    else: 
        print(f'Good news, the username {new_user} is available!')
    

#-----Store numbers 1 thru 9 in a list, loop thru the list, and use an if-elif-else chain inside the loop for print the
#proper ordinal ending for each number (for example, 1st, 2nd, 3rd, 4th, 5th, etc.)

numbers=list(range(1,10))
for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')

