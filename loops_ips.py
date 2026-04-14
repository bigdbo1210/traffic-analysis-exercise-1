# Week 4 – Loops and Iteration
# Automating IP classification

print("=== IP Address Classification ===\n")

# List of IP addresses
ip_addresses = [
    "192.168.1.25",
    "10.0.0.8",
    "172.16.5.14",
    "8.8.8.8",
    "172.15.3.2"
]

# Counters
internal_count = 0
external_count = 0

# Lists
internal_ips = []
external_ips = []

# Loop through IPs
for ip in ip_addresses:

    # Check if internal
    if ip.startswith(("192.168.", "10.")):
        print(f"{ip} → Internal")
        internal_count += 1
        internal_ips.append(ip)
    else:
        print(f"{ip} → External")
        external_count += 1
        external_ips.append(ip)

# Summary
print("\n=== Summary ===")
print(f"Internal IPs: {internal_count}")
print(f"External IPs: {external_count}")

print("\nInternal List:", internal_ips)
print("External List:", external_ips)