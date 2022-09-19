#-----An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant 
# class you wrote in Exercise 9_1.
# Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.

class Restaurant:
    """Simple model of a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant's attributes"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describes the restaurant"""
        print(f"{self.restaurant_name} serves delicious {self.cuisine_type} food!")

    def open_restaurant(self):
        """Announces that the restaurant is open"""
        print(f"{self.restaurant_name} is now open!")

class IceCreamStand(Restaurant):
    """Model of an ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type="ice cream"):
        """Initializing attributes"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']

    def list_flavors(self):
        """Prints a list fo ice cream flavors"""
        print(f"Here are the ice cream flavors we offer at {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

jenis = IceCreamStand('Jenis')
jenis.list_flavors()

#-----An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9_2.
# Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of privileges.
# Create an instance of Admin, and call your method.

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
        attributes = [self.first_name, self.last_name, self.age, self.height, self.gender]
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

class Admin(User):
    """A model of an admin user."""

    def __init__(self, first_name, last_name, age, height, gender):
        """Initializes attributes for admin."""
        super().__init__(first_name, last_name, age, height, gender)
        self.privileges = []

    def show_privileges(self):
        """Prints out the admin's privileges."""
        print(f"User admin {self.first_name} has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

roberto = Admin('roberto', 'avila', 26, '6ft1in', 'male')
roberto.describe_user()
roberto.privileges = [
    'can read',
    'can write', 
    'can execute',
    'can create users',
    'can delete users'
]
roberto.show_privileges()

#-----Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings 
# as described in the prior exercise. Move the show_privileges() method to this class. Make a Privileges instance as an attribute
# in the Admin class. Create a new instance of Admin and use your method to show its privileges.

class Admin(User):
    """A model of an admin user."""

    def __init__(self, first_name, last_name, age, height, gender):
        """Initializes attributes for admin."""
        super().__init__(first_name, last_name, age, height, gender)
        self.permissions = Privileges()

class Privileges:
    """Model of admin privileges"""

    def __init__(self, privileges=[]):
        """Initialize attributes"""
        self.privileges = privileges
    
    def show_privileges(self):
        """Prints out the admin's privileges."""
        if self.privileges:
            print(f"This user admin has the following privileges:")
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("This user has no privileges.")


print('\n')
roberto = Admin('roberto', 'avila', 26, '6ft1in', 'male')
roberto.describe_user()
roberto.permissions.show_privileges()
print("Adding privileges...")
roberto.permissions.privileges = [
    'can read',
    'can write', 
    'can execute',
    'can create users',
    'can delete users'
]
roberto.permissions.show_privileges()

#-----Use the final version of electric_car.py from this section. Add a method to the Battery class called upgrade_battery().
# This method should check the battery size and set the capacity to 100 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery.
# You should see an increase in the car’s range.

class Car:
    """Representation of a car."""

    def __init__(self, make, model, year):
        """Initialize car's attributes"""
        self.make = make.title()
        self.model = model.title()
        self.year = year
        self.odometer_reading = 0 
    
    def get_descriptive_name(self):
        """Return descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Updates the car's odometer reading
        Rejects the change if the odometer attempts to rollback.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back the odometer.")
    
    def increment_odometer(self, miles):
        """
        Increments the car's odometer reading
        Rejects the change if the odometer attempts to rollback.
        """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You cannot roll back the odometer.")

    def fill_gas_tank(self):
        """Fills up the gas tank"""
        print("The gas tank is now full.")

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of parent class"""
        super().__init__(make, model, year)  
        self.battery = Battery()

class Battery:
    """Simple model of an electric car's battery"""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        """Upgrades the car's battery to 100-kWh"""
        print("Upgrading battery to 100-kWh...")
        self.battery_size = 100

print('\n')
my_tesla = ElectricCar('tesla', 'model y', 2020)
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

