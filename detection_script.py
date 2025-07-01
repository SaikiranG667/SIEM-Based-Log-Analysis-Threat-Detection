import re
from collections import defaultdict


log_file = "sample1_logs\Linux_2k.log"  

# Regex pattern for failed logins
pattern = r"authentication failure.*rhost=([^\s]+)"

#count IPs
ip_counts = defaultdict(int)

with open(log_file, 'r') as f:
    for line in f:
        match = re.search(pattern, line)
        if match:
            ip = match.group(1)
            ip_counts[ip] += 1

# display top offending IPs
print("🔐 Failed Login Attempts by IP:")
for ip, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{ip}: {count} attempts")

#brute-force attempts (more than 5 tries)
print("\n🚨 Suspected Brute Force IPs (more than 5 failures):")
for ip, count in ip_counts.items():
    if count > 5:
        print(f"⚠️ {ip} - {count} failures")
