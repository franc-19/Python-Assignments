from abc import ABC, abstractmethod

# Base Employee class with the common interface for all employee types
class Employee(ABC):
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    # Abstract method that each derived class will implement
    @abstractmethod
    def calculate_payroll(self):
        pass

# SalaryEmployee class that inherits from Employee
class SalaryEmployee(Employee):
    def __init__(self, emp_id, name, weekly_salary):
        super().__init__(emp_id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

# HourlyEmployee class that inherits from Employee
class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        super().__init__(emp_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate

# CommissionEmployee class that inherits from SalaryEmployee
class CommissionEmployee(SalaryEmployee):
    def __init__(self, emp_id, name, weekly_salary, commission_rate, sales):
        super().__init__(emp_id, name, weekly_salary)
        self.commission_rate = commission_rate
        self.sales = sales

    def calculate_payroll(self):
        return self.weekly_salary + (self.commission_rate * self.sales)

# Function to create employees based on user input
def create_employee():
    print("\nChoose employee type:")
    print("1. Salary Employee")
    print("2. Hourly Employee")
    print("3. Commission Employee")
    
    choice = input("Enter the type of employee (1, 2, or 3): ")
    
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    
    if choice == '1':
        weekly_salary = float(input("Enter Weekly Salary: "))
        return SalaryEmployee(emp_id, name, weekly_salary)
    
    elif choice == '2':
        hours_worked = float(input("Enter Hours Worked: "))
        hourly_rate = float(input("Enter Hourly Rate: "))
        return HourlyEmployee(emp_id, name, hours_worked, hourly_rate)
    
    elif choice == '3':
        weekly_salary = float(input("Enter Weekly Salary: "))
        commission_rate = float(input("Enter Commission Rate (as a decimal): "))
        sales = float(input("Enter Sales Amount: "))
        return CommissionEmployee(emp_id, name, weekly_salary, commission_rate, sales)
    
    else:
        print("Invalid choice! Please try again.")
        return None

# Main function to demonstrate the payroll system
def main():
    employees = []
    
    print("Welcome to the Payroll System!")
    
    num_employees = int(input("How many employees would you like to add? "))
    
    for _ in range(num_employees):
        employee = create_employee()
        if employee:
            employees.append(employee)
    
    print("\nPayroll Summary:")
    for employee in employees:
        print(f"{employee.name}'s payroll: {employee.calculate_payroll()}")

if __name__ == "__main__":
    main()
