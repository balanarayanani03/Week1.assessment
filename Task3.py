
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------
# 1. NUMPY - STUDENT MARKS
# --------------------------------

marks = np.array([
    [80, 75, 90],
    [60, 70, 65],
    [85, 90, 95],
    [70, 80, 75]
])

print("Shape:", marks.shape)
print("Student averages:", marks.mean(axis=1))
print("Subject averages:", marks.mean(axis=0))

# Add 5 grace marks using broadcasting
grace_marks = marks + 5
print("Marks after grace marks:\n", grace_marks)

# Weighted scores: 40%, 30%, 30%
weights = np.array([0.4, 0.3, 0.3])
weighted_scores = np.dot(grace_marks, weights)
print("Weighted scores:", weighted_scores)


# --------------------------------
# 2. CREATE EMPLOYEES CSV
# --------------------------------

employees = [
    [1, "Arun", "Sales", 30000, "Chennai"],
    [2, "Priya", "HR", 45000, "Chennai"],
    [3, "Rahul", "IT", np.nan, "Bangalore"],
    [4, "Divya", "IT", 75000, "Chennai"],
    [5, "Karthik", "Finance", 90000, "Mumbai"],
    [6, "Meena", "Sales", 52000, "Bangalore"],
    [7, "Suresh", "IT", 68000, "Chennai"],
    [8, "Anitha", "HR", np.nan, "Mumbai"],
    [1, "Arun", "Sales", 30000, "Chennai"]  # Duplicate
]

columns = ["id", "name", "department", "salary", "city"]

df = pd.DataFrame(employees, columns=columns)
df.to_csv("employees.csv", index=False)


# --------------------------------
# 3. CREATE DEPARTMENTS CSV
# --------------------------------

departments = [
    ["Sales", "Ravi", 500000],
    ["HR", "Priya", 300000],
    ["IT", "Kumar", 800000],
    ["Finance", "Lakshmi", 400000],
    ["Marketing", "Anand", 250000]
]

dept = pd.DataFrame(
    departments,
    columns=["department", "head", "budget"]
)

dept.to_csv("departments.csv", index=False)


# --------------------------------
# 4. LOAD AND EXPLORE DATA
# --------------------------------

df = pd.read_csv("employees.csv")
dept = pd.read_csv("departments.csv")

print("\nData information:")
df.info()

print("\nSalary description:")
print(df.describe())

print("\nUsing loc:")
print(df.loc[0:2, ["name", "salary"]])

print("\nUsing iloc:")
print(df.iloc[0:3, 0:3])

print("\nSalary above 50000:")
print(df[df["salary"] > 50000])


# --------------------------------
# 5. CLEAN EMPLOYEE DATA
# --------------------------------

# Fill missing salaries with median
df["salary"] = df["salary"].fillna(df["salary"].median())

# Remove duplicate rows
df = df.drop_duplicates()

# Correct data types
df["id"] = df["id"].astype(int)
df["salary"] = df["salary"].astype(int)

# Save cleaned data
df.to_csv("employees.csv", index=False)

print("\nCleaned employees:")
print(df)


# --------------------------------
# 6. GROUPBY AND AGGREGATION
# --------------------------------

summary = df.groupby("department").agg(
    headcount=("id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
)

print("\nDepartment summary:")
print(summary)


# --------------------------------
# 7. MERGE DATA
# --------------------------------

# Inner join
inner = pd.merge(df, dept, on="department", how="inner")
print("\nInner join:")
print(inner)

# Left join
left = pd.merge(df, dept, on="department", how="left")
print("\nLeft join:")
print(left)

# Outer join
outer = pd.merge(df, dept, on="department", how="outer")
print("\nOuter join:")
print(outer)

# Find departments with no employees
employee_counts = df.groupby("department").size()

empty_departments = dept[
    ~dept["department"].isin(employee_counts.index)
]

print("\nDepartments with no employees:")
print(empty_departments["department"].tolist())


# --------------------------------
# 8. BAR CHART
# --------------------------------

summary["headcount"].plot(kind="bar", color="skyblue",
                          label="Employees")

plt.title("Employee Headcount by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.legend()
plt.tight_layout()
plt.savefig("bar.png")
plt.show()

print("Insight: IT has the highest headcount.")


# --------------------------------
# 9. HISTOGRAM
# --------------------------------

plt.hist(df["salary"], bins=5, color="orange",
         edgecolor="black", label="Salary")

plt.title("Distribution of Employee Salaries")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.legend()
plt.tight_layout()
plt.savefig("histogram.png")
plt.show()

print("Insight: The histogram shows how salaries are distributed.")


# --------------------------------
# 10. SCATTER PLOT
# --------------------------------

plt.scatter(df["salary"], df["id"], color="green",
            label="Employees")

plt.title("Salary vs Employee ID")
plt.xlabel("Salary")
plt.ylabel("Employee ID")
plt.legend()
plt.tight_layout()
plt.savefig("scatter.png")
plt.show()

print("Insight: The scatter plot compares each employee's salary.")


# --------------------------------
# 11. LINE CHART
# --------------------------------

plt.plot(df["name"], df["salary"], marker="o",
         color="red", label="Salary")

plt.title("Employee Salaries")
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("line.png")
plt.show()

print("Insight: The line chart compares salaries across employees.")

print("\nAll CSV files and charts created successfully.")
