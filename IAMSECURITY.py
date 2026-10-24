def cloud_iam():
 import os
 from cryptography.fernet import Fernet
 print("\nTOP EXP 5: CLOUD IAM AND ENCRYPTION")
 key = Fernet.generate_key()
 cipher = Fernet(key)
 users_iam = {
 "alice": {"role": "reader"},
 "bob": {"role": "writer"},
 "admin": {"role": "admin"}
 }
 role_permissions = {
 "reader": ["read"],
 "writer": ["read", "write"],
 "admin": ["read", "write", "delete"]
 }
 data = input("Enter sensitive cloud data: ").encode()
 encrypted_data = cipher.encrypt(data)
 with open("cloud_data.enc", "wb") as file:
 file.write(encrypted_data)
 print("Data encrypted and stored at rest.")
 username = input("Enter authorized username: ")
 action = input("Enter action (read/write/delete): ").lower()
 account = users_iam.get(username)
 if account and action in role_permissions[account["role"]]:
 print("IAM authorization successful.")
 if action == "read":
 with open("cloud_data.enc", "rb") as file:
 stored_data = file.read()
 print("Decrypted Data:", cipher.decrypt(stored_data).decode())
 elif action == "write":
 new_data = input("Enter new data: ").encode()
 with open("cloud_data.enc", "wb") as file:
 file.write(cipher.encrypt(new_data))
 print("Encrypted data updated.")
 elif action == "delete":
 os.remove("cloud_data.enc")
 print("Encrypted data deleted.")
 else:
 print("IAM authorization failed.")
 print("Transit encryption must be provided by HTTPS/TLS in a real cloud deployment.")
