import hashlib
import secrets
import hmac
import time


def hash_password(password, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        100000
    )

    return salt, password_hash.hex()


def verify_password(password, salt, stored_hash):
    _, password_hash = hash_password(password, salt)

    return hmac.compare_digest(password_hash, stored_hash)




users = {}

roles = {
    "Administrator": {
        "read",
        "write",
        "delete",
        "manage_users"
    },

    "Faculty": {
        "read",
        "write"
    },

    "Staff": {
        "read",
        "write"
    },

    "Student": {
        "read"
    }
}


def create_user(username, password, role):

    if role not in roles:
        print("Invalid role!")
        return

    if username in users:
        print("Username already exists!")
        return

    salt, password_hash = hash_password(password)

    users[username] = {
        "salt": salt,
        "password": password_hash,
        "role": role,
        "failed_attempts": 0,
        "locked_until": 0
    }

    print(f"User '{username}' created successfully.")


def login(username, password):

    if username not in users:
        print("Invalid username or password.")
        return None

    user = users[username]

    # Check account lock
    if time.time() < user["locked_until"]:
        print("Account temporarily locked.")
        return None

    # Verify password
    if verify_password(
        password,
        user["salt"],
        user["password"]
    ):
        user["failed_attempts"] = 0

        print("Login successful!")
        print("Role:", user["role"])

        return username

    # Failed login
    user["failed_attempts"] += 1

    print("Invalid username or password.")

    # Lock after 3 failed attempts
    if user["failed_attempts"] >= 3:

        user["locked_until"] = time.time() + 30
        user["failed_attempts"] = 0

        print("Account locked for 30 seconds.")

    return None



def check_permission(username, permission):

    if username not in users:
        print("User not authenticated.")
        return False

    role = users[username]["role"]

    if permission in roles[role]:
        return True

    return False


def access_resource(username, permission):

    if check_permission(username, permission):

        print(
            f"Access GRANTED: "
            f"{username} can perform '{permission}'."
        )

    else:

        print(
            f"Access DENIED: "
            f"{username} cannot perform '{permission}'."
        )



create_user(
    "admin",
    "Admin@123",
    "Administrator"
)

create_user(
    "faculty",
    "Faculty@123",
    "Faculty"
)

create_user(
    "staff",
    "Staff@123",
    "Staff"
)

create_user(
    "student",
    "Student@123",
    "Student"
)

print("\n--- LOGIN ---")

username = input("Username: ")
password = input("Password: ")

logged_user = login(username, password)

if logged_user:

    print("\n--- ACCESS CONTROL ---")

    access_resource(
        logged_user,
        "read"
    )

    access_resource(
        logged_user,
        "write"
    )

    access_resource(
        logged_user,
        "delete"
    )

    access_resource(
        logged_user,
        "manage_users"
    )
