##question1

from math import pi
from abc import ABC


class Shape(ABC):
    def __init__(self, sides):
        self.sides = sides

    def compute_area(self):
        pass


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(3)
        self.base = base
        self.height = height

    def compute_area(self):
        return 0.5 * self.base * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(0)
        self.radius = radius

    def compute_area(self):
        return pi * self.radius ** 2


def main():
    list1 = []
    for i in range(3):
        s = input("Enter shape: ")
        if s == "c":
            radius = float(input("Enter radius: "))
            list1.append(Circle(radius))
        elif s == "t":
            base = float(input("Enter length: "))
            height = float(input("Enter height: "))
            list1.append(Triangle(base, height))
        else:
            print("Invalid option")

    for shape in list1:
        display(shape)


def display(shape):
    print("Shape:", shape.__class__.__name__)
    print("Area:", shape.compute_area())
    print()


main()
##question2
class Employee:
    def __init__(self, employeename, employeeid, salary):
        self.employeename = employeename
        self.employeeid = employeeid
        self.salary = salary

    def salary_status(self):
        return self.salary


class BuildingManager(Employee):
    def __init__(self, employeename, employeeid):
        super().__init__(employeename, employeeid, 10000)


class ProcurementManager(Employee):
    def __init__(self, employeename, employeeid):
        super().__init__(employeename, employeeid, 12000)


class LogisticsManager(Employee):
    def __init__(self, employeename, employeeid):
        super().__init__(employeename, employeeid, 15000)


def main():
    employees = [
        BuildingManager("zenab", 234),
        ProcurementManager("hadia", 666),
        LogisticsManager("maryam", 665)
    ]

    for employee in employees:
        print("Employee Name:", employee.employeename)
        print("Employee ID:", employee.employeeid)
        print(employee.salary_status())
        print()


if __name__ == '__main__':
    main()


