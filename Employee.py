import itertools


class Employee:

    new_id = itertools.count(start=1, step=1)

    def __init__(self, forename, surname, rate):

        self.id = next(Employee.new_id)
        self.forename = forename
        self.surname = surname
        self.hours = 0
        self.rate = rate

    def payment(self, hours):

        if hours >= 60:
            pay = self.rate * 40 + \
                  1.5 * self.rate * 20 + \
                  2 * self.rate * (hours - 60)
        else:
            if hours >= 40:
                pay = self.rate * 40 + 1.5 * self.rate * (hours - 40)
            else:
                pay = self.rate * hours

        return pay

if __name__ == "__main__":

    emp1 = Employee("Jack", "Holmes", 10.0)
    emp2 = Employee("John", "Holmes", 20.0)

    print(emp1.id)
    print(emp2.id)

    print(emp1.payment(100))
