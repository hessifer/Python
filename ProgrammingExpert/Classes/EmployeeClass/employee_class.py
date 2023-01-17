class Employee:
    # Write your code here
    average_age = 0
    average_salary = 0
    employee_count = 0
    total_salary = 0
    total_age = 0


    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.employee_count += 1
        Employee.total_salary += salary
        Employee.total_age += age
        Employee.average_age = Employee.total_age / Employee.employee_count
        Employee.average_salary = Employee.total_salary / Employee.employee_count


if __name__ == "__main__":
    e1 = Employee("joe", 34, 100000)
    e2 = Employee("bill", 23, 120000)
    e3 = Employee("cat", 45, 150000)

    print(f"Employee Count: {Employee.employee_count}")
    print(f"Average Salary: ${Employee.average_salary:,.2f}")
