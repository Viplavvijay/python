//class Employee:
    def _init__(self, *args):
        if (len(args) == 0):
            self.name = "hi"
            self.desig = "Hi"
            self.salary = 100
            self.number = 100
        elif (len(args) == 4):
            self.name = args[0]
            self.desig = args[1]
            self.salary = args[2]
            self.number = args[3]
        try:
            print(" ")
            print("Try Part Executed ")
            raise
        except:
            print("Exception raised")
        finally:
            print("Always executed")
            print("")

    def displayDetails(self):
        print("{:<16} {:<17} {:<15} {:<21}".format(
            self.name, self.desig, self.salary, self.number))

    def p_input(self):
        self.name = input("Enter employee name: ")
        self.desig = input("Enter employee Designation: ")
        self.salary = input("Enter employee Salary: ")
        self.number = input("Enter employee Number: ")


el = Employee("george", "Tester", 86000, 9550905058)
e2 = Employee("martin", "Tester", 45000, 9459987629)
e3 = Employee("sam", "Devops", 35000, 9909636889)
e4 = Employee("richie", "Tester", 40000, 8777859757)
e5 = Employee()
e5.p_input()
print("{:<16} {:<17} {:<15} {:<21}".format('Name', 'Designation', 'Salary', 'Number'))
el.displayDetails()
e2.displayDetails()
e3.displayDetails()
e4.displayDetails()
e5.displayDetails()
