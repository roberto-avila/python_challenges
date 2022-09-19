#-----Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
#Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant()
#that prints a message indicating that the restaurant is open.
#Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant:
    """Simple model of a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant's attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describes the restaurant"""
        print(f"{self.restaurant_name} serves delicious {self.cuisine_type} food!")

    def open_restaurant(self):
        """Announces that the restaurant is open"""
        print(f"{self.restaurant_name} is now open!")

my_restaurant = Restaurant('Numero 28', 'Italian')

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

#-----Start with your previous class. Create three different instances from the class, and call describe_restaurant() for each instance.

print('\n')
mcdonalds = Restaurant('McDonalds', 'fast')
mcdonalds.describe_restaurant()

maikos = Restaurant('Maikos', 'Japanese')
maikos.describe_restaurant()

cava = Restaurant('CAVA', 'Mediterranean')
cava.describe_restaurant()

#-----Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes 
#that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information.
#Make another method called greet_user() that prints a personalized greeting to the user.
#Create several instances representing different users, and call both methods for each user.
print('\n')

class User:
    """Model of a user"""

    def __init__(self, first_name, last_name, age, height, gender):
        "Initialize the class's attributes"
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.height = height
        self.gender = gender
    
    def describe_user(self):
        """Describe the user's attributes"""
        full_name = f"{self.first_name} {self.last_name}"
        attributes = [self.first_name, self.last_name, self.age, self.height, self.gender]
        print(f"{full_name}'s attributes are:")
        for attribute in attributes:
            print(f"- {attribute}")

    def greet_user(self):
        """Simple greeting for the user."""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello {full_name}!")

christina = User('christina', 'avila', 23, '5ft 6in', 'female')
roberto = User('roberto', 'avila', 26, '6ft 1in', 'male')

christina.describe_user()
christina.greet_user()
print('\n')
roberto.describe_user()
roberto.greet_user()
