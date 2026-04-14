# Module 1 Final Project - Security Log Classifier

# Counters
failed_logins = 0
successful_logins = 0
internal_count = 0
external_count = 0

# Track failed attempts per user/IP
failed_attempts = {}

# Read file
with open("logins.txt") as f:
    lines = f.readlines()

print(f"Loaded {len(lines)} login records.\n")

# Process each line
for line in lines:
    parts = line.strip().split()
    
    username = parts[0]
    ip = parts[1]
    result = parts[2]

    # Count success/failure
    if result == "FAILURE":
        failed_logins += 1
        
        # Track failed attempts
        key = (username, ip)
        if key in failed_attempts:
            failed_attempts[key] += 1
        else:
            failed_attempts[key] = 1
    else:
        successful_logins += 1

    # Classify IP
    if ip.startswith(("192.168.", "10.")):
        internal_count += 1
    else:
        external_count += 1

# Print Summary
print("====== Security Log Summary ======")
print(f"Total login attempts: {len(lines)}")
print(f"Successful logins: {successful_logins}")
print(f"Failed logins: {failed_logins}")
print(f"Internal IPs: {internal_count}")
print(f"External IPs: {external_count}")

# Detect brute force
print("\n=== Possible Brute Force Alerts ===")
for (user, ip), count in failed_attempts.items():
    if count >= 3:
        print(f"[!] User '{user}' had {count} failed logins from IP {ip}")