# Cyber Defense Login Attempt Analyzer

from datetime import datetime

print("========================================")
print("   Cyber Defense - Login Attempt Report")
print("========================================\n")

# Collect input
analyst_name = input("Enter analyst name: ")
username = input("Enter username being analyzed: ")
failed_logins = int(input("Enter number of failed login attempts: "))
privileged_input = input("Is this a privileged account? (yes/no): ").lower()

# Convert to boolean
is_privileged = True if privileged_input == "yes" else False

# Determine risk level
if failed_logins > 5 and is_privileged:
    risk_level = "HIGH"
    alert = "[*] Privileged account shows multiple failed logins!"
elif failed_logins > 5:
    risk_level = "MEDIUM"
    alert = "[!] Multiple failed logins detected."
elif failed_logins > 0:
    risk_level = "LOW"
    alert = "[-] Some failed attempts observed."
else:
    risk_level = "INFORMATIONAL"
    alert = "[+] No failed logins recorded."

# Get timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

# Print report
print("\n========================================")
print("   Cyber Defense - Login Attempt Report")
print("========================================")
print(f"Analyst: {analyst_name}")
print(f"User: {username}")
print(f"Failed Attempts: {failed_logins}")
print(f"Privileged Account: {privileged_input.capitalize()}")
print(f"Risk Level: {risk_level}")
print(f"Alert: {alert}")
print(f"Report Generated: {timestamp}")