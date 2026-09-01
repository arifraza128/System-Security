users = {
    "admin": {
        "password": "admin123",
        "failed_attempts": 0,
        "locked": False
    }
}

def login(username, password):
    if username not in users:
        return "Invalid username or password"

    user = users[username]

    if user["locked"]:
        return "Account locked"

    if password == user["password"]:
        user["failed_attempts"] = 0
        return "Login successful"

    user["failed_attempts"] += 1

    if user["failed_attempts"] >= 3:
        user["locked"] = True
        return "Account locked due to multiple failed attempts"

    return "Invalid username or password"


print(login("admin", "wrong"))
print(login("admin", "wrong"))
print(login("admin", "wrong"))
print(login("admin", "admin123"))
