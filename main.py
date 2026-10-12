import csv
import os
from abc import ABC, abstractmethod
from decimal import Decimal, InvalidOperation


# FILE PATH

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EMPLOYEE_FILE = os.path.join(BASE_DIR, "employees.csv")


# ABSTRACT CLASS

class Employee(ABC):
    def __init__(self, emp_id, name, designation, basic_salary):
        self.__emp_id = str(emp_id).strip()
        self.__name = name.strip()
        self.__designation = designation.strip()
        self.__basic_salary = self.validate_money(basic_salary)

        if not self.__emp_id:
            raise ValueError("Employee ID cannot be empty.")

        if not self.__name:
            raise ValueError("Employee name cannot be empty.")

        if not self.__designation:
            raise ValueError("Designation cannot be empty.")

        if self.__basic_salary <= 0:
            raise ValueError("Basic salary must be positive.")

    @staticmethod
    def validate_money(amount):
        try:
            value = Decimal(str(amount))

            if not value.is_finite():
                raise ValueError("Enter a valid salary amount.")

            if value.as_tuple().exponent < -2:
                raise ValueError("Maximum two decimal places allowed.")

            return value.quantize(Decimal("0.01"))

        except (InvalidOperation, TypeError):
            raise ValueError("Enter a valid numeric amount.")

    @property
    def emp_id(self):
        return self.__emp_id

    @property
    def name(self):
        return self.__name

    @property
    def designation(self):
        return self.__designation

    @property
    def basic_salary(self):
        return self.__basic_salary

    @property
    def hra(self):
        return (self.basic_salary * Decimal("0.20")).quantize(
            Decimal("0.01")
        )

    @property
    def da(self):
        return (self.basic_salary * Decimal("0.10")).quantize(
            Decimal("0.01")
        )

    @property
    def gross_salary(self):
        return self.basic_salary + self.hra + self.da

    @property
    def deductions(self):
        return (self.basic_salary * Decimal("0.05")).quantize(
            Decimal("0.01")
        )

    @property
    def net_salary(self):
        return self.gross_salary - self.deductions

    @abstractmethod
    def employee_type(self):
        pass

    def display_details(self):
        print(
            f"{self.emp_id:<12}"
            f"{self.name:<22}"
            f"{self.designation:<20}"
            f"{self.net_salary:>12.2f}"
        )


# PERMANENT EMPLOYEE

class PermanentEmployee(Employee):

    def employee_type(self):
        return "Permanent"


# PAYROLL MANAGER

class PayrollManager:
    def __init__(self):
        self.__employees = {}
        self.load_employees()

    # ADD EMPLOYEE

    def add_employee(self):
        try:
            emp_id = input("Enter employee ID: ").strip()

            if not emp_id:
                raise ValueError("Employee ID cannot be empty.")

            if emp_id in self.__employees:
                raise ValueError("Employee ID already exists.")

            name = input("Enter employee name: ").strip()
            designation = input("Enter designation: ").strip()
            salary = input("Enter basic monthly salary: Rs. ")

            employee = PermanentEmployee(
                emp_id, name, designation, salary
            )

            self.__employees[emp_id] = employee

            try:
                self.save_employees()
            except OSError:
                del self.__employees[emp_id]
                raise

            print("Employee added successfully!")
            print(f"Net monthly salary: Rs. {employee.net_salary:.2f}")

        except ValueError as error:
            print("Invalid input:", error)

        except OSError as error:
            print("File error:", error)

    # SEARCH EMPLOYEE

    def search_employee(self):
        emp_id = input("Enter employee ID: ").strip()
        employee = self.__employees.get(emp_id)

        if employee:
            self.show_header()
            employee.display_details()
        else:
            print("Employee not found.")

    # DISPLAY ALL EMPLOYEES

    @staticmethod
    def show_header():
        print("-" * 66)
        print(
            f"{'ID':<12}"
            f"{'Name':<22}"
            f"{'Designation':<20}"
            f"{'Net Salary':>12}"
        )
        print("-" * 66)

    def display_employees(self):
        if not self.__employees:
            print("No employee records found.")
            return

        self.show_header()

        for employee in self.__employees.values():
            employee.display_details()

        print("-" * 66)

    # CALCULATE SALARY

    def calculate_salary(self):
        emp_id = input("Enter employee ID: ").strip()
        employee = self.__employees.get(emp_id)

        if not employee:
            print("Employee not found.")
            return

        print(f"\nSalary details for {employee.name}")
        print(f"Basic Salary : Rs. {employee.basic_salary:.2f}")
        print(f"HRA (20%)    : Rs. {employee.hra:.2f}")
        print(f"DA (10%)     : Rs. {employee.da:.2f}")
        print(f"Gross Salary : Rs. {employee.gross_salary:.2f}")
        print(f"Deductions   : Rs. {employee.deductions:.2f}")
        print("-" * 35)
        print(f"Net Salary   : Rs. {employee.net_salary:.2f}")

    # GENERATE PAYSLIP

    def generate_payslip(self):
        emp_id = input("Enter employee ID: ").strip()
        employee = self.__employees.get(emp_id)

        if not employee:
            print("Employee not found.")
            return

        filename = os.path.join(
            BASE_DIR, f"payslip_{employee.emp_id}.txt"
        )

        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write("=" * 42 + "\n")
                file.write("           EMPLOYEE PAYSLIP\n")
                file.write("=" * 42 + "\n")
                file.write(f"Employee ID : {employee.emp_id}\n")
                file.write(f"Name        : {employee.name}\n")
                file.write(f"Designation : {employee.designation}\n")
                file.write(f"Employee Type: {employee.employee_type()}\n")
                file.write("-" * 42 + "\n")
                file.write(
                    f"Basic Salary: Rs. {employee.basic_salary:.2f}\n"
                )
                file.write(f"HRA (20%)   : Rs. {employee.hra:.2f}\n")
                file.write(f"DA (10%)    : Rs. {employee.da:.2f}\n")
                file.write(
                    f"Gross Salary: Rs. {employee.gross_salary:.2f}\n"
                )
                file.write(
                    f"Deductions  : Rs. {employee.deductions:.2f}\n"
                )
                file.write("-" * 42 + "\n")
                file.write(
                    f"NET SALARY  : Rs. {employee.net_salary:.2f}\n"
                )
                file.write("=" * 42 + "\n")

            print("Payslip generated successfully!")
            print("Saved at:", filename)

        except OSError as error:
            print("Could not generate payslip:", error)

    # SAVE EMPLOYEE RECORDS TO CSV

    def save_employees(self):
        with open(EMPLOYEE_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "emp_id",
                "name",
                "designation",
                "basic_salary",
                "employee_type"
            ])

            for employee in self.__employees.values():
                writer.writerow([
                    employee.emp_id,
                    employee.name,
                    employee.designation,
                    f"{employee.basic_salary:.2f}",
                    employee.employee_type()
                ])

    # LOAD EMPLOYEE RECORDS FROM CSV

    def load_employees(self):
        if not os.path.isfile(EMPLOYEE_FILE):
            print("No existing employees.csv file. Starting fresh.")
            return

        try:
            with open( EMPLOYEE_FILE, "r", newline="", encoding="utf-8" ) as file:
                reader = csv.DictReader(file)
                required_columns = {
                    "emp_id",
                    "name",
                    "designation",
                    "basic_salary",
                    "employee_type"
                }

                if not reader.fieldnames or not required_columns.issubset(
                    reader.fieldnames
                ):
                    raise ValueError("Invalid employees.csv format.")

                loaded_employees = {}

                for row in reader:
                    emp_id = row["emp_id"].strip()

                    if emp_id in loaded_employees:
                        raise ValueError(
                            f"Duplicate employee ID: {emp_id}"
                        )

                    if row["employee_type"].strip() != "Permanent":
                        raise ValueError("Unsupported employee type.")

                    employee = PermanentEmployee(
                        emp_id,
                        row["name"],
                        row["designation"],
                        row["basic_salary"]
                    )

                    loaded_employees[emp_id] = employee

                self.__employees = loaded_employees

            print(
                f"Loaded {len(self.__employees)} employee(s) successfully."
            )

        except (OSError, ValueError, KeyError, csv.Error) as error:
            self.__employees.clear()
            print("Could not load employee records:", error)


# MAIN PROGRAM

def main():
    payroll = PayrollManager()

    while True:
        print("\n======= EMPLOYEE PAYROLL SYSTEM =======\n")
        print("1. For Add Employee -> press 1")
        print("2. For Calculate Salary -> press 2")
        print("3. For Generate Payslip -> press 3")
        print("4. For Search Employee -> press 4")
        print("5. For Display All Employees -> press 5")
        print("6. For Save Payroll Data -> press 6")
        print("7. For Exit -> press 7")

        choice = int(input(" ✹ Enter your choice (1-7): "))

        try:
            if choice == 1:
                payroll.add_employee()

            elif choice == 2:
                payroll.calculate_salary()

            elif choice == 3:
                payroll.generate_payslip()

            elif choice == 4:
                payroll.search_employee()

            elif choice == 5:
                payroll.display_employees()

            elif choice == 6:
                payroll.save_employees()
                print("Payroll data saved successfully!")

            elif choice == 7:
                payroll.save_employees()
                print("Payroll data saved. Goodbye!")
                break

            else:
                print("Invalid choice. Enter a number from 1 to 7.")

        except OSError as error:
            print("File operation failed:", error)


if __name__ == "__main__":
    main()
