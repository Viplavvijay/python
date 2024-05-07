class employee:
    def detail(self, n):
        for i in range(n):
            name = str(input("Enter the name:"))
            empid = str(input("Enter the employee id:"))
            phone = int(input("Enter the mobile no.:"))
            salary = int(input("Enter the salary:"))
            print("\n---------EMPLOYEE DETAILS----------")
            print("EMPLOYEE NAME:", name)
            print("EMPLOYEE ID: ", empid)
            print("PHONE NO.:", phone)
            print("EMPLOYEE SALARY:", salary)


n = int(input("Enter the Number of Elements:"))
EMP = employee()
EMP.detail(n)
