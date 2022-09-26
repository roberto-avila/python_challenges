#-----Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter 
# that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered.
# Call the function three times, using a different number of arguments each time.

def make_sandwich(size, *toppings):
    """Make a sandwich and print a summary"""
    print(f"Making a {size}-inch sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
        
make_sandwich(12, 'ham', 'turkey', 'avocado',)
make_sandwich(12, 'ham', 'lettuce', 'avocado', 'tomatoes',)
make_sandwich(12, 'salami', 'cheese',)
#-----Start with a copy of the build_profile() function. Build a profile of yourself by calling build_profile(), using your first and last names, 
#and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

me = build_profile('roberto','avila', age=26, hair_color='brown')
print(me)

#-----Write a function that stores information about a car in a dictionary. the function should always receive a manufacturer
#  and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information
#  and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one:
#car = make_car('subaru', 'outback', color='blue', tow_package=True)
#Print the dictionary that’s returned to make sure all the information was stored correctly.

def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing information about a car"""
    car_info['make'] = manufacturer
    car_info['model'] = model
    return car_info

my_car = make_car('hyundai', 'tucson', color='green', year=2022, hybrid=True)
print(my_car)



