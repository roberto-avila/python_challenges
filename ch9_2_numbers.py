#-----Start with your restaurant program from Exercise 9_1. Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class. Print the number of customers the restaurant has served, 
# and then change this value and print it again.
#Add a method called set_number_served() that lets you set the number of customers that have been served.
# Call this method with a new number and print the value again.
#Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
# Call this method with any number you like that could represent how many customers were served in, say, a day of business.

class Restaurant:
    """Simple model of a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant's attributes"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    def describe_restaurant(self):
        """Describes the restaurant"""
        print(f"{self.restaurant_name} serves delicious {self.cuisine_type} food!")

    def open_restaurant(self):
        """Announces that the restaurant is open"""
        print(f"{self.restaurant_name} is now open!")
    
    def set_number_served(self, customers):
        """Sets a new number of customers served"""
        if customers >= self.number_served:
            self.number_served = customers
        else:
            print("We can't decrease our number of customers!")

    def increment_number_served(self, new_customers):
        """Increments the amount of customers served"""
        if new_customers >= 0:
            self.number_served += new_customers
        else:
            print("We can't decrease our number of customers!")

restaurant = Restaurant('pizza hut', 'italian')

print(restaurant.number_served)
restaurant.number_served = 3
print(restaurant.number_served)

restaurant.set_number_served(5)
print(restaurant.number_served)

restaurant.increment_number_served(10)
print(restaurant.number_served)

print('\n')

#-----Add an attribute called login_attempts to your User class from Exercise 9_1.
#  Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
#  Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
#Make an instance of the User class and call increment_login_attempts() several times.
#  Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
#  Print login_attempts again to make sure it was reset to 0.

class User:
    """Model of a user"""

    def __init__(self, first_name, last_name, age, height, gender):
        "Initialize the class's attributes"
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.height = height
        self.gender = gender
        self.login_attempts = 0
    
    def describe_user(self):
        """Describe the user's attributes"""
        full_name = f"{self.first_name} {self.last_name}"
        attributes = [
            self.first_name, 
            self.last_name, 
            self.age, 
            self.height, 
            self.gender]
        print(f"{full_name}'s attributes are:")
        for attribute in attributes:
            print(f"- {attribute}")

    def greet_user(self):
        """Simple greeting for the user."""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello {full_name}!")

    def increment_login_attempts(self):
        """Increments the number of login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the number of login attempts back to 0"""
        self.login_attempts = 0

roberto = User('roberto', 'avila', 26, '6ft 1in', 'male')

roberto.increment_login_attempts()
roberto.increment_login_attempts()
roberto.increment_login_attempts()
print(roberto.login_attempts)

roberto.reset_login_attempts()
print(roberto.login_attempts)