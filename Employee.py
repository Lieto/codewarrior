import itertools


class Employee:

    new_id = itertools.count(start=1, step=1)

    def __init__(self, forename, surname, rate):

        self.id = next(Employee.new_id)
        self.forename = forename
        self.surname = surname
        self.hours = 0
        self.rate = rate

    def calculate_payment(self, hours):

        # Set pay to rate * hours
        pay = self.rate * hours

        if hours > 40:
            pay += 5 * (hours - 40)

        if hours > 60:
            pay += 5 * (hours - 60)

        return pay

    def payment(self, hours):

        if hours > 7 * 24 or hours < 0:
            raise ValueError("%d is not in valid range." % hours)
        else:
            return self.calculate_payment(hours)

if __name__ == "__main__":

    emp1 = Employee("Jack", "Holmes", 10.0)
    emp2 = Employee("John", "Holmes", 20.0)

    print(emp1.id)
    print(emp2.id)

    print(emp1.payment(100))
    print(emp2.payment(7*25))
