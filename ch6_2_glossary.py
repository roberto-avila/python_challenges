#-------Use the same glossary from the previous challenge, but loop through the keys and values instead of printing each entry separately.


python_glossary = {
    'variable': 'Symbolic name that is a reference or pointer to an object.',
    'looping': 'Repeating something over and over until a particular condition is satisfied.',
    'list': 'Data structure used to store multiple items in one variable and can be created using square brackets.',
    'tuple': 'Immutable data structure used to store multiple items in a single variable and can be declared using parentheses.',
    'dictionary': 'Data structure that is more generally known as an associative array. A dictionary consists of a collection of key-value pairs.'
}

for term, definition in python_glossary.items():
    print(f"{term.title()}:\n {definition}")

#-------Make a dictionary containing three rivers and their location. Use a loop to print a sentence about each river and its location,
#use another loop to print the name of each river, and a third loop to print the name of each location.

rivers = {
    'nile river': 'egypt',
    'colorado river': 'texas',
    'lempa river': 'el salvador'
}

for river, location in rivers.items():
    print(f"\nThe {river.title()} is located in {location.title()}")

#-------Use the favorite_languages dictionary. Make a list of people you want to poll. Include in this list some people that have already been
#polled, and print a message for those who haven't been polled, and those who have.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

poll_takers = ['jen', 'roberto', 'sarah', 'jamie']

for name in poll_takers:
    if name in favorite_languages.keys():
        print(f"\n{name.title()}, thanks for taking our poll!")
    else:
        print(f"\n{name.title()}, please take our poll!")