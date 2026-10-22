# Employee data
employees = [
    {"id": 1, "name": "Arun", "department": "Sales", "salary": 30000, "city": "Chennai"},
    {"id": 2, "name": "Priya", "department": "HR", "salary": 45000, "city": "Chennai"},
    {"id": 3, "name": "Rahul", "department": "IT", "salary": 60000, "city": "Bangalore"},
    {"id": 4, "name": "Divya", "department": "IT", "salary": 75000, "city": "Chennai"},
    {"id": 5, "name": "Karthik", "department": "Finance", "salary": 90000, "city": "Mumbai"},
    {"id": 6, "name": "Meena", "department": "Sales", "salary": 52000, "city": "Bangalore"},
    {"id": 7, "name": "Suresh", "department": "IT", "salary": 68000, "city": "Chennai"},
    {"id": 8, "name": "Anitha", "department": "HR", "salary": 48000, "city": "Mumbai"}
]


# 1. Bonus function using *args and **kwargs
def bonus(salary, rate=0.1, *extras, **options):
    result = salary * rate + sum(extras)

    if "cap" in options:
        result = min(result, options["cap"])

    return result


print("Bonus:", bonus(30000, 0.1, 500, 1000, cap=4000))


# 2. Employee class and custom exception
class InvalidSalaryError(Exception):
    pass


class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")

        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


# 3. Manager class using inheritance and super()
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}, Team Size: {self.team_size}"


emp = Employee("Arun", 30000)
print(emp.get_details())
print("Annual Salary:", emp.annual_salary())

manager = Manager("Priya", 45000, 5)
print(manager.get_details())


# 4. Custom exception handling
try:
    emp2 = Employee("Test", -500)
except InvalidSalaryError as e:
    print("Error:", e)
finally:
    print("Transaction finished")


# 5. List comprehension: names with salary above 50000
above_50000 = [
    emp["name"] for emp in employees if emp["salary"] > 50000
]
print("Above 50000:", above_50000)


# 6. Map and lambda: add 10% raise
raised_salaries = list(
    map(lambda emp: emp["salary"] * 1.10, employees)
)
print("Salaries after 10% raise:", raised_salaries)


# 7. Filter: keep Chennai employees
chennai_employees = list(
    filter(lambda emp: emp["city"] == "Chennai", employees)
)
print("Chennai:", [emp["name"] for emp in chennai_employees])


# 8. For loop using continue and break
for emp in employees:
    salary = emp["salary"]

    if salary == 0:
        continue

    if salary > 85000:
        break

    print("Processed:", emp["name"], salary)
