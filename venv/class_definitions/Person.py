
class Person:
    """Person class"""
    def __init__(self, lname, fname, addy, phone_number):
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.phone_number = phone_number


    def display(self):
        return self._last_name + ", " + self._first_name + ":" + self._address

    def __str__(self):
        return "Person named " + self.last_name + ", " + self.first_name + " is addressed at " + self.address + ", their phone number is " + str(self.phone_number)

    def __repr__(self):
        return 'Person(first_name={}, last_name={}, address={}, phone_number={}'.format(self.first_name, self.last_name, self.address, str(self.phone_number))
