#-----Write a function called make_shirt() and include parameters that describe the size, and what message will be printed on the shirt. Call the function using positional
#and keyword arguments.

from pydoc import describe


def make_shirt(size, message):
    """Displays a message stating size and message"""
    print("---Here's your new shirt---")
    print(f"Size: {size.title()}")
    print(f"Message: {message}")

make_shirt('small', 'I love this shirt')

#-----Modify the make_shirt() function so that shirt sizes are large by default and have a default message of I love Python! Make a large shirt and a medium shirt with 
#the default message, and make a shirt of any size with a different message.

def make_shirt(size='large', message='I love Python!'):
    """Displays a message stating size and message"""
    print("\n---Here's your new shirt---")
    print(f"Size: {size.title()}")
    print(f"Message: {message}")

make_shirt()
make_shirt('medium')
make_shirt('small', 'Python rocks!')

#-----Write a function called describe_city() that accepts the name of a city and its country. Print both in the sentence format "city is located in country". Make the country a 
#default value. Call the function for three different cities, at least one of which is not in the default country.

def describe_city(city, country = 'united states'):
    print(f"\n{city.title()} is located in {country.title()}")

describe_city('chicago')
describe_city('cleveland')
describe_city('sao paulo', 'brazil')