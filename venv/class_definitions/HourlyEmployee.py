from datetime import date
from Employee import Employee

class HourlyEmployee(Employee):
    def __init__(self, last_name, first_name, start_date, hourly_pay):
        super().__init__(last_name, first_name)
        self.start_date = start_date
        self.hourly_pay = hourly_pay

    def give_raise(self, add_raise):
        self.hourly_pay += add_raise

    def display(self):
        print("Hourly Employee: " + self.last_name + ", " + self.first_name + "\nStart Date: " + str(self.start_date) + "\nHourly Pay: " + str("%.2f" % self.hourly_pay))

    def __str__(self):
        return "HourlyEmployee named " + self.last_name + self.first_name + " Hourly Pay: " + str("%.2f" % self.hourly_pay)

    def __repr__(self):
        return "HourlyEmployee(first_name={}, last_name={}, hourly_pay={})".format(self.first_name, self.last_name, str("%.2f" % self.hourly_pay))


if __name__ == '__main__':
    hourly_boy = HourlyEmployee("Phillips", "Carl", date.today(), 10.00)
    hourly_boy.display()
    hourly_boy.give_raise(2.00)
    hourly_boy.display()
    del hourly_boy