import os
import time

# List of target IP addresses or websites to monitor
targets = ["8.8.8.8", "github.com", "192.168.1.1"]
print("Starting Security Uptime Monitor...")
print("-" * 30)

for target in targets:
    # Send a single ping packet
    response = os.system(f"ping -c 1 {target} > /dev/null 2>&1")
    
    if response == 0:
        print(f"[SUCCESS] {target} is ONLINE.")
    else:
        print(f"[ALERT] {target} is OFFLINE or blocking pings.")

print("-" * 30)
print("Scan Complete.")
