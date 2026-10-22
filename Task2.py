
import csv
import json
import requests
from dotenv import load_dotenv

load_dotenv()

# 1. Read employee.csv
employee = []

with open("employee.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["id"] = int(row["id"])
        row["salary"] = float(row["salary"])
        employee.append(row)

print("Rows read:", len(employee))

# 2. Write employees.json
with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)

# 3. Write high_earners.csv
high_earners = [e for e in employee if e["salary"] > 50000]

with open("high_earners.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=employee[0].keys())
    writer.writeheader()
    writer.writerows(high_earners)

print("High earners:", len(high_earners))


# 4. Get users from API
try:
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    users = response.json()

    for user in users[:3]:
        print(user.get("id"), "-", user.get("name"), "-", user.get("email"))

    # Read nested JSON using get()
    for user in users:
        address = user.get("address", {})
        user["city"] = address.get("city")

    # Save users to JSON
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error")


# 5. Check 404 error
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999",
        timeout=5
    )

    if response.status_code == 404:
        print("/users/9999 -> 404 Not found")

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error")
