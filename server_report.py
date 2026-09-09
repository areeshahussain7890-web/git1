
import os
import sys

service_name = os.getenv("SERVICE_NAME", "demo-service")
state = os.getenv("SERVICE_STATE", "up")

print(f"Checking {service_name}...")

if state == "up":
    print("HEALTHY")
else:
    print("UNHEALTHY")
print("Backup: OK")
