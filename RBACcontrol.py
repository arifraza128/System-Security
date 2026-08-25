users = {
    "admin": {"password": "admin123", "role": "Administrator"},
    "faculty": {"password": "faculty123", "role": "Faculty"},
    "staff": {"password": "staff123", "role": "Staff"},
    "student": {"password": "student123", "role": "Student"}
}

permissions = {
    "Administrator": ["View", "Add", "Update", "Delete"],
    "Faculty": ["View", "Update"],
    "Staff": ["View", "Add"],
    "Student": ["View"]
}


def rbac_system(username, password, operation):
    # Step 1: Authentication
    if username not in users:
        return "Authentication Failed: User not found."

    if users[username]["password"] != password:
        return "Authentication Failed: Incorrect password."

    # Step 2: Identify Role
    role = users[username]["role"]

    print("Authentication Successful")
    print("Role:", role)

    # Step 3 & 4: Check Permission and Authorize
    if operation in permissions[role]:
        return "Access Granted"
    else:
        return "Access Denied"


# ---------------- TEST CASE 1 ----------------
print("===== TEST CASE 1 =====")

username = "faculty"
password = "faculty123"
operation = "Update"

print("Username:", username)
print("Operation:", operation)
print(rbac_system(username, password, operation))


# ---------------- TEST CASE 2 ----------------
print("\n===== TEST CASE 2 =====")

username = "student"
password = "student123"
operation = "Delete"

print("Username:", username)
print("Operation:", operation)
print(rbac_system(username, password, operation))
