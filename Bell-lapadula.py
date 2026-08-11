security_levels = {
    "public": 1,
    "confidential": 2,
    "secret": 3,
    "top secret": 4
}

users = {
    "Arif": "top secret",
    "Anil": "secret",
    "Alice": "confidential",
    "Bob": "public"
}

files = {
    "Employee List": "public",
    "Company Report": "confidential",
    "Weapon Design": "secret",
    "Nuclear Launch Code": "top secret"
}

print("===== USERS =====")

for user, level in users.items():
    print(user, "->", level)

print("\n===== FILES =====")

for file, classification in files.items():
    print(file, "->", classification)

user = input("\nEnter username: ")

if user not in users:
    print("User not found!")

else:
    print("\nAvailable Files:")

    for file in files:
        print("-", file)

    file_name = input("\nEnter file name: ")

    if file_name not in files:
        print("File not found!")

    else:
        user_level = security_levels[users[user]]
        file_level = security_levels[files[file_name]]

        print("\n===== ACCESS CHECK =====")
        print("User:", user)
        print("User Level:", users[user])
        print("File:", file_name)
        print("File Level:", files[file_name])

        if user_level >= file_level:
            print("Result: ACCESS GRANTED")
        else:
            print("Result: ACCESS DENIED")
