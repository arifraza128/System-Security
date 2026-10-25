def mfa_authentication():
 import hashlib
 import hmac
 import secrets
 import time
 import struct
 import base64
 print("\nTOP EXP 7: MULTI-FACTOR AUTHENTICATION")
 username = "alice"
 password_hash = hashlib.sha256(b"SecurePass123!").hexdigest()
 otp_secret = secrets.token_bytes(20)
 entered_username = input("Username: ")
 entered_password = input("Password: ")
 entered_hash = hashlib.sha256(
 entered_password.encode()
 ).hexdigest()
 if (
 entered_username != username
 or not hmac.compare_digest(entered_hash, password_hash)
 ):
 print("First-factor authentication failed.")
 return
 counter = int(time.time()) // 30
 message = struct.pack(">Q", counter)
 digest = hmac.new(
 otp_secret, message, hashlib.sha1
 ).digest()
 oƯset = digest[-1] & 0x0F
 code = (
 struct.unpack(">I", digest[oƯset:oƯset + 4])[0]
 & 0x7FFFFFFF
 ) % 1000000
 otp = f"{code:06d}"
 print("Demo OTP (normally delivered through an authenticator app):", otp)
 entered_otp = input("Enter OTP: ")
 if hmac.compare_digest(entered_otp, otp):
 print("MFA successful. Access granted.")
 else:
 print("MFA failed. Access denied.")
