#---Write a class called Employee. The __init__() method should take in a first name, a last name, and an annual salary,
#and store each of these as attributes. Write a method called give_raise() that adds $5000 to the annual salary 
#by default but also accepts a different raise amount.
#Write a test case for Employee. Write two test methods, test_give_default_raise() and test_give_custom_raise(). 
#Use the setUp() method so you don’t have to create a new employee instance in each test method. 
#Run your test case, and make sure both tests pass.

import unittest
from employees import Employee

class TestEmployee(unittest.TestCase):
    """Testing class Employee"""

    def setUp(self):
        first = 'Roberto'
        last = 'Avila'
        salary = 75_000
        self.my_employee = Employee(first, last, salary)

    def test_give_raise(self):
        """Testing for giving the default raise"""
        new_salary = self.my_employee.give_raise()
        self.assertEqual(new_salary, 80_000)

    def test_custom_give_raise(self):
        """Testing for giving a custom raise"""
        new_salary = self.my_employee.give_raise(10_000)
        self.assertEqual(new_salary, 85_000)

if __name__ == '__main__':
    unittest.main()
