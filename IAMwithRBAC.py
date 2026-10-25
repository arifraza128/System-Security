def cloud_iam_advanced():
 import os
 from cryptography.fernet import Fernet
 print("\nTOP EXP 8: ADVANCED CLOUD IAM")
 key_file = "iam_encryption.key"
 data_file = "iam_sensitive_data.enc"
 if os.path.exists(key_file):
 with open(key_file, "rb") as file:
 key = file.read()
 else:
 key = Fernet.generate_key()
 with open(key_file, "wb") as file:
 file.write(key)
 cipher = Fernet(key)
 roles = {
 "alice": {"password": "Alice@123", "role": "viewer"},
 "bob": {"password": "Bob@123", "role": "editor"},
 "admin": {"password": "Admin@123", "role": "admin"}
 }
 role_permissions = {
 "viewer": ["read"],
 "editor": ["read", "write"],
 "admin": ["read", "write", "delete"]
 }
 if not os.path.exists(data_file):
 with open(data_file, "wb") as file:
 file.write(cipher.encrypt(b"Confidential cloud information"))
 username = input("Username: ")
 password = input("Password: ")
 account = roles.get(username)
 if not account or not hmac_compare(
 account["password"], password
 ):
 print("Authentication failed.")
 return
 action = input("Action (read/write/delete): ").lower()
 if action not in role_permissions[account["role"]]:
 print("RBAC authorization denied.")
 return
 if action == "read":
 with open(data_file, "rb") as file:
 print(cipher.decrypt(file.read()).decode())
 elif action == "write":
 data = input("Enter new confidential data: ").encode()
 with open(data_file, "wb") as file:
 file.write(cipher.encrypt(data))
 print("Data encrypted and updated.")
 elif action == "delete":
 os.remove(data_file)
 print("Data deleted.")
def hmac_compare(first, second):
 import hmac
 return hmac.compare_digest(first.encode(), second.encode()) 
