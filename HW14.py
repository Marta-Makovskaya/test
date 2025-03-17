import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    Name TEXT,
    Position TEXT,
    Department TEXT,
    Salary REAL
)
''')


employees_data = [
    ('Alice', 'Developer', 'IT', 6000),
    ('Bob', 'Manager', 'HR', 7000),
    ('Charlie', 'Sales Executive', 'Sales', 4500),
    ('Diana', 'Manager', 'Sales', 8000)
]

cursor.executemany('INSERT INTO Employees (Name, Position, Department, Salary) VALUES (?, ?, ?, ?)', employees_data)


cursor.execute('''
UPDATE Employees 
SET Position = 'Senior Developer'
WHERE Name = 'Alice'
''')


cursor.execute('ALTER TABLE Employees ADD COLUMN HireDate TEXT')


hire_dates = [
    '2022-01-15',  # Alice
    '2021-05-22',  # Bob
    '2022-03-10',  # Charlie
    '2020-11-30'   # Diana
]

cursor.executemany('UPDATE Employees SET HireDate = ? WHERE Name = ?', zip(hire_dates, [row[0] for row in employees_data]))

cursor.execute('SELECT * FROM Employees WHERE Position = "Manager"')
managers = cursor.fetchall()

cursor.execute('SELECT * FROM Employees WHERE Salary > 5000')
high_salary_employees = cursor.fetchall()

cursor.execute('SELECT * FROM Employees WHERE Department = "Sales"')
sales_employees = cursor.fetchall()

cursor.execute('SELECT AVG(Salary) FROM Employees')
average_salary = cursor.fetchone()[0]

cursor.execute('DROP TABLE Employees')

conn.commit()
conn.close()

print("Managers:", managers)
print("High Salary Employees:", high_salary_employees)
print("Sales Employees:", sales_employees)
print("Average Salary:", average_salary)