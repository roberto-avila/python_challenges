#-----Make a list of three people and a dictionary of their attributes (similar to the dicitionary from ch6_1 challenge). Loop through the list of people, and print
#everything you know about each person.
family = []

sister = {'first_name': 'christina', 'last_name': 'avila', 'age': '23', 'city': 'austin, texas'}
family.append(sister)
dad = {'first_name': 'ricardo', 'last_name': 'avila', 'age': '53', 'city': 'austin, texas'}
family.append(dad)
mom = {'first_name': 'raquel', 'last_name': 'duran', 'age': '47', 'city': 'panama city, panama'}
family.append(mom)

for person in family:
    full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = f"{person['city'].title()}"
    print(f"{full_name} lives in {city} and is {age} years old.")


#-----Make several dictionaries for pets and their attributes. Include them in a list. Loop through the list and print the pets' attributes.

pets = []

pet = {
    'animal type': 'python',
    'name': 'sparky',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'chicky',
    'owner': 'linda',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")

#-----Make a dictionary called favorite_places. Think of three names to use as keys, and store one to three favorite places for each person. Print each person's
#name and their favorite places.

favorite_places = {
    'roberto': ['austin', 'el salvador', 'italy'],
    'christina': ['san antonio', 'panama', 'paris'],
    'ian': ['houston', 'colorado', 'spain'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"-{place.title()}")



#-----Modify the favorite_number dictionary from ch6_1 challenge so each person has more than one favorite number. Print each person's name along with their favorite numbers.

favorite_numbers = {
    'ian': [2, 8, 16],
    'christina': [4, 6],
    'roberto': [7],
    'raquel': [13, 1],
    'ricardo': [67, 54],
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")

#-----Make a dictionary caled cities, include in it 3 cities and create a dictionary for each one containing three facts (country, continent, polpulation). Print the name of each
#city and their facts

cities = {
    'austin': {
        'country': 'united states',
        'continent': 'north america',
        'population': 1028225,
    },
    'san salvador': {
        'country': 'el salvador',
        'continent': 'central america',
        'population': 6000000,
    },
    'brasilia': {
        'country': 'brazil',
        'continent': 'south america',
        'population': 212000000,
    },
}

for city, facts in cities.items():
    country = f"{facts['country'].title()}"
    continent = f"{facts['continent'].title()}"
    population = f"{facts['population']}"
    print(f"Info about {city.title()}:")
    print(f"\tCountry: {country}")
    print(f"\tContinent: {continent}")
    print(f"\tPopulation: {population}")

#-----Take one of the above programs and extend it by adding new keys and values, improving the output formatting, etc.

favorite_numbers = {
    'ian': [2, 8, 16],
    'christina': [4, 6],
    'roberto': [7],
    'raquel': [13, 1],
    'ricardo': [67, 54],
    'rolando': [5],
}

for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"{name.title()}'s favorite number is:")
    elif len(numbers) > 1:
        print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"{number}")

    