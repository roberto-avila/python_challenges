class Employee:
    """Model of an employee and their salary."""

    def __init__(self, first_name, last_name, salary):
        """Initialize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, pay_raise=5000):
        """Gives the employee a raise. $5000 by default."""
        self.salary += pay_raise
        return self.salary
