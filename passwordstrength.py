import re

password = input("Enter password: ")

score = 0

if len(password) >= 8:
    score += 1

if re.search(r"[A-Z]", password):
    score += 1

if re.search(r"[a-z]", password):
    score += 1

if re.search(r"[0-9]", password):
    score += 1

if re.search(r"[@#$%&*!]", password):
    score += 1

if score == 5:
    print("Strong Password")
elif score >= 3:
    print("Medium Password")
else:
    print("Weak Password")
