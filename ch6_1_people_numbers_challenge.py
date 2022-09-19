#-----Use a dictionary to store the first name, last name, age, and city of residence of someone you know. Print each piece of info.

sister = {'first_name': 'christina', 'last_name': 'avila', 'age': '23', 'city': 'austin, texas'}
print(sister['first_name'].title())
print(sister['last_name'].title())
print(sister['age'])
print(sister['city'].title())

#-----Make a dictionary of five people and their favorite numbers. Print the dictionary and one person's favorite number.

favorite_numbers = {
    'ian': 2,
    'christina': 4,
    'roberto': 7,
    'raquel': 13,
    'ricardo': 67,
}
print(favorite_numbers)
print(f"\nRoberto's favorite number is {favorite_numbers['roberto']}.")


#-----Using a dictionary, build a "glossary" of 5 terms you've learned in programming. Print a word on one line and the definition on another.

python_glossary = {
    'variable': 'Symbolic name that is a reference or pointer to an object.',
    'looping': 'Repeating something over and over until a particular condition is satisfied.',
    'list': 'Data structure used to store multiple items in one variable and can be created using square brackets.',
    'tuple': 'Immutable data structure used to store multiple items in a single variable and can be declared using parentheses.',
    'dictionary': 'Data structure that is more generally known as an associative array. A dictionary consists of a collection of key-value pairs.'
}

print('Variable:')
print(python_glossary['variable'])


