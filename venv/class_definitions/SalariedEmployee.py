from datetime import date
from Employee import Employee

class SalariedEmployee(Employee):
    def __init__(self, last_name, first_name, start_date, salary):
        super().__init__(last_name, first_name)
        self.start_date = start_date
        self.salary = salary

    def give_raise(self, add_raise):
        self.salary += add_raise

    def display(self):
        print("Salaried Employee: " + self.last_name + ", " + self.first_name + "\nStart Date: " + str(self.start_date) + "\nSalary: " + str("%.2f" % self.salary))

    def __str__(self):
        return "SalariedEmployee named " + self.last_name + self.first_name + " Salary: " + str("%.2f" % self.salary)

    def __repr__(self):
        return "SalariedEmployee(first_name={}, last_name={}, salary={})".format(self.first_name, self.last_name, str("%.2f" % self.salary))


if __name__ == '__main__':
    salary_girl = SalariedEmployee("Phillips", "Carl", date.today(), 40000)
    salary_girl.display()
    salary_girl.give_raise(5000)
    salary_girl.display()
    del salary_girl