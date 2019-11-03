class Employee:
    """Person class using class Address, Class Composition"""
    def __init__(self, last_name, first_name, address="", phone_number=''):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.phone_number = phone_number

    def __str__(self):
        return "";

    def __repr__(self):
        return "";

    def display(self):
        return (self._last_name + ", " + self._first_name + "(" + str(self.student_id) + ") " + str(self.major) +
              " GPA: " + str(self.gpa))