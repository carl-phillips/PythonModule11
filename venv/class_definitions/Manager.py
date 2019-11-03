from datetime import date
from Employee import Employee

class Manager(Employee):
    """Person class using class Address, Class Composition"""
    def __init__(self, last_name, first_name, address, phone_number, start_date, salary, department, direct_reports):
        super(Manager, self).__init__(last_name, first_name, address, phone_number, start_date, salary)
        self.department = department
        self.direct_reports = direct_reports

    def give_raise(self, add_raise):
        self.salary += add_raise

    def __str__(self):
        return "Employee Started at " + str(self.start_date) + " gets paid " + str(self.salary)

    def __repr__(self):
        return "Manager(last_name={}, first_name={}, address={}, phone_number={}, start_date={}, salary={}, department={}, direct_reports={})".format(self.last_name, self.first_name, self.address, self.phone_number, str(self.start_date), str(self.salary))

    def display(self):
        print("Manager Name: " + self.last_name + ", " + self.first_name + "\nStart Date: " + str(self.start_date) + "\nSalary: " + str(self.salary) + "\nDirect Reports: " +  str(self.direct_reports))


if __name__ == '__main__':
    direct_reports = ["report1", "report2", "report3"]
    epic_manager = Manager("Phillips", "Carl", "123 15th Street West Des Moines IA", 5151234567, date.today(), 40000, "", direct_reports)
    epic_manager.display()
    epic_manager.give_raise(2000)
    epic_manager.display()
    del epic_manager

