#Matthew Tyler
#11/7/25
#Employee

class Employee():
    def __init__(self, name, ID, department, title):
        self.name = name
        self.ID = ID
        self.department = department
        self.title = title
        pass
    def display_employee(self):
        print(self.name)
        print(self.ID)
        print(self.department)
        print(self.title)
        print("\n")



employee1 = Employee("Susan_Meyers", 47899, "Accounting", "Vice_President")
employee2 = Employee("Mark_Jones", 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

employee1.display_employee()
employee2.display_employee()
employee3.display_employee()
