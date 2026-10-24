def secure_cloud_storage():
 from cryptography.fernet import Fernet
 import os
 print("\nTOP EXP 6: SECURE CLOUD STORAGE")
 key = Fernet.generate_key()
 cipher = Fernet(key)
 storage_users = {
 "owner": {"password": "owner123", "permission": "read_write"},
 "viewer": {"password": "viewer123", "permission": "read"},
 "unauthorized": {"password": "test123", "permission": "none"}
 }
 plaintext = input("Enter file content: ").encode()
 encrypted = cipher.encrypt(plaintext)
 with open("secure_storage.enc", "wb") as file:
 file.write(encrypted)
 username = input("Username: ")
 password = input("Password: ")
 account = storage_users.get(username)
 if not account or account["password"] != password:
 print("Authentication failed.")
 return
 if account["permission"] not in ("read", "read_write"):
 print("Access denied.")
 return
 with open("secure_storage.enc", "rb") as file:
 encrypted_content = file.read()
 print("Authorized Decrypted Data:",
 cipher.decrypt(encrypted_content).decode())
 if account["permission"] == "read_write":
 print("Owner can also update the encrypted data.") 
