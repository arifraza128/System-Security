
print("     SECURITY RISK ASSESSMENT TOOL")


risk_score = 0

questions = [
    "1. Does the system use weak or easily guessable passwords?",
    "2. Does the system have outdated or unpatched software?",
    "3. Is sensitive data stored without encryption?",
    "4. Is there no firewall or network access control?",
    "5. Are regular data backups not performed?",
    "6. Does the system lack antivirus or endpoint protection?",
    "7. Are user access permissions not properly controlled?",
    "8. Is security monitoring or logging not enabled?"
]

risk_points = [10, 15, 20, 15, 10, 10, 10, 10]

print("\nAnswer the following questions with Yes or No.\n")

for i in range(len(questions)):
    while True:
        answer = input(questions[i] + " (Yes/No): ").strip().lower()

        if answer == "yes":
            risk_score += risk_points[i]
            break
        elif answer == "no":
            break
        else:
            print("Please enter only Yes or No.")

if risk_score <= 20:
    risk_level = "LOW"
    recommendation = "Maintain current security practices and perform regular security checks."

elif risk_score <= 50:
    risk_level = "MEDIUM"
    recommendation = "Improve password policies, software updates, backups, access control, and monitoring."

else:
    risk_level = "HIGH"
    recommendation = "Immediate security improvements are required. Strengthen authentication, encryption, firewall, endpoint protection, access control, and monitoring."


print("          SECURITY REPORT")

print("Total Risk Score :", risk_score, "/ 100")
print("Risk Level       :", risk_level)
print("Recommendation   :", recommendation)
