# Asset Tagger Script

print("=== Asset Tagger ===\n")

# Collect user input
hostname = input("Enter hostname: ")
criticality = input("Enter asset criticality (low, medium, high): ").lower()
risk_score = int(input("Enter risk score (0–100): "))

# Determine risk level
if risk_score >= 80 or criticality == "high":
    risk_level = "HIGH RISK"
elif risk_score >= 50:
    risk_level = "MEDIUM RISK"
else:
    risk_level = "LOW RISK"

# Output report
print("\n=== Asset Risk Report ===")
print(f"Hostname: {hostname}")
print(f"Criticality: {criticality}")
print(f"Risk Score: {risk_score}")
print(f"Risk Classification: {risk_level}")