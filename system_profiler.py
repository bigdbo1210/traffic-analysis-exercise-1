import os
import platform
import getpass

# Mini System Profiler

print("=== System Information ===")

# Get hostname
hostname = platform.node()
print(f"Hostname: {hostname}")

# Get operating system
os_name = platform.system()
print(f"Operating System: {os_name}")

# Get OS version
os_version = platform.version()
print(f"OS Version: {os_version}")

# Get current user
user = getpass.getuser()
print(f"Current User: {user}")
