# Employee Payroll Management System

A menu-driven **Employee Payroll Management System developed using Python** that demonstrates Object-Oriented Programming (OOP) concepts. The application allows users to add employees, calculate salaries, generate payslips, search employee records, and save payroll data using CSV file handling.

## Features

- **Add Employees:** Register employees with a unique ID, name, designation, and basic salary.
- **Calculate Salary:** Calculate HRA, DA, gross salary, deductions, and net salary.
- **Generate Payslips:** Generate individual employee payslips and save them as text files.
- **Search Employees:** Find employee records using their employee ID.
- **Display Employees:** View all registered employees and their net salaries.
- **Save Payroll Data:** Store employee information in a CSV file.
- **Load Payroll Data:** Automatically load previously saved records when the program starts.
- **Input Validation:** Validate employee details and salary amounts.
- **Exception Handling:** Handle invalid input, duplicate employee IDs, and file-related errors.

## Technologies Used

- **Programming Language:** Python 3
- **Programming Paradigm:** Object-Oriented Programming (OOP)
- **Data Storage:** CSV (Comma-Separated Values)
- **Payslip Format:** Text files (`.txt`)
- **Python Modules:** `csv`, `os`, `abc`, and `decimal`

## OOP Concepts Implemented

This project demonstrates the following six concepts:

1. **Classes and Objects:** Uses `Employee`, `PermanentEmployee`, and `PayrollManager` classes.
2. **Encapsulation:** Uses private attributes such as `__emp_id`, `__name`, `__designation`, and `__basic_salary`.
3. **Inheritance:** The `PermanentEmployee` class inherits from the abstract `Employee` class.
4. **Abstraction:** Uses the `ABC` module and an abstract `employee_type()` method.
5. **File Handling:** Reads and writes employee data using CSV files and generates payslip text files.
6. **Exception Handling:** Handles invalid salary values, duplicate employee IDs, and file errors.

## Salary Calculation

The project uses the following illustrative monthly salary rules:

| Component | Calculation |
|---|---|
| Basic Salary | Entered by the user |
| House Rent Allowance (HRA) | 20% of basic salary |
| Dearness Allowance (DA) | 10% of basic salary |
| Gross Salary | Basic Salary + HRA + DA |
| Deductions | 5% of basic salary |
| Net Salary | Gross Salary − Deductions |

### Example

For a basic monthly salary of ₹30,000:

- Basic Salary: ₹30,000
- HRA: ₹6,000
- DA: ₹3,000
- Gross Salary: ₹39,000
- Deductions: ₹1,500
- **Net Monthly Salary: ₹37,500**

These rules are for educational demonstration and do not represent official tax or statutory payroll calculations.

## Project Structure

```text
EmployeePayrollSystem/
├── main.py
├── employees.csv
├── payslip_E101.txt
└── README.md
```

- `main.py` — Contains the complete Python application.
- `employees.csv` — Stores employee records and salary information.
- `payslip_E101.txt` — An example of a generated employee payslip. Actual filenames depend on employee IDs.
- `README.md` — Contains project documentation.

**Note:** The CSV file and payslip files are generated automatically when the corresponding operations are performed.

## Requirements

- Python 3 installed on your system.
- A code editor such as Visual Studio Code.

No external Python packages are required.

## Installation and Setup

### 1. Clone the repository

If the project is hosted on GitHub, clone it using:

```bash
git clone YOUR_REPOSITORY_URL
```

Replace `YOUR_REPOSITORY_URL` with your actual repository URL.

### 2. Open the project folder

```bash
cd EmployeePayrollSystem
```

### 3. Run the application

On macOS or Linux:

```bash
python3 main.py
```

On Windows:

```bash
python main.py
```

## How to Use

When the application starts, it displays the following menu:

```text
======= EMPLOYEE PAYROLL SYSTEM =======
1. Add Employee
2. Calculate Salary
3. Generate Payslip
4. Search Employee
5. Display All Employees
6. Save Payroll Data
7. Exit

Enter your choice (1-7):
```

Enter the number corresponding to the operation you want to perform.

### Example: Adding an Employee

```text
Enter your choice (1-7): 1
Enter employee ID: E101
Enter employee name: Rahul Sharma
Enter designation: Software Developer
Enter basic monthly salary: Rs. 30000

Employee added successfully!
Net monthly salary: Rs. 37500.00
```

### Example: Generating a Payslip

Select option `3` and enter the employee ID:

```text
Enter your choice (1-7): 3
Enter employee ID: E101

Payslip generated successfully!
```

The payslip is saved in a text file named `payslip_E101.txt` in the project folder.

## Data Storage

Employee records are stored in `employees.csv` with the following fields:

| Field | Description |
|---|---|
| `emp_id` | Unique employee identifier |
| `name` | Employee name |
| `designation` | Employee's job designation |
| `basic_salary` | Basic monthly salary |
| `employee_type` | Type of employee |

The application loads saved employee records at startup and saves changes to the CSV file.

Payslips are generated separately as text files containing employee details, salary components, deductions, and net salary.

## Learning Objectives

This project helps demonstrate:

- Practical implementation of OOP principles in Python.
- Creating abstract classes and derived classes.
- Applying encapsulation, inheritance, and abstraction.
- Performing salary calculations using decimal arithmetic.
- Reading and writing CSV files.
- Generating employee payslips.
- Validating user input and handling exceptions.
- Building a menu-driven console application.

## Future Enhancements

Possible improvements include:

- A graphical user interface using Tkinter.
- Database integration using SQLite or MySQL.
- Employee attendance and leave management.
- Overtime and bonus calculations.
- Configurable tax and deduction rules.
- Monthly payroll reports.
- Exporting payslips to PDF.
- Support for different employee categories and salary structures.

## Author

**Your Name:** Vishal Bagdi

## License

This project is intended for educational and learning purposes. You may modify and extend it for your own use.