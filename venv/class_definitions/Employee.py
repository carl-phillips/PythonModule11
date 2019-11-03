from Person import Person

class Employee(Person):
    """Person class using class Address, Class Composition"""
    def __init__(self, last_name, first_name, address, phone_number, start_date, salary):
        super().__init__(last_name, first_name, address, phone_number)
        self.start_date = start_date
        self.salary = salary

    def give_raise(self, add_raise):
        self.salary += add_raise

    def __str__(self):
        return "Employee Started at " + str(self.start_date) + " gets paid " + str(self.salary)

    def __repr__(self):
        return "Employee(start_date={}, salary={})".format(str(self.start_date), str(self.salary))

    def display(self):
        return ("Start Date: " + self.start_date + "\nSalary: " + self.salary)