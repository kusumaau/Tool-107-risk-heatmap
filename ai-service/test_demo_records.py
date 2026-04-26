import os
from dotenv import load_dotenv
from groq_client import call_groq

load_dotenv()

demo_records = [
    "Server crashes during peak hours",
    "Database backup fails silently",
    "Unauthorized access to admin panel",
    "Third party API goes down unexpectedly",
    "Employee accidentally deletes production data",
    "Payment gateway timeout during checkout",
    "SSL certificate expires without warning",
    "Insider threat leaks customer data",
    "DDoS attack overwhelms the web server",
    "Cloud storage bucket left publicly accessible",
    "Network firewall misconfiguration exposes systems",
    "Ransomware encrypts all company files",
    "Cloud provider experiences regional outage",
    "Developer pushes untested code to production",
    "Customer database exposed due to missing auth",
    "Third party vendor suffers data breach",
    "Employees reusing weak passwords",
    "Unpatched software vulnerability exploited",
    "Physical server room flooded",
    "API keys committed to public GitHub",
    "Login page vulnerable to brute force",
    "Outdated dependencies with known CVEs",
    "No monitoring on critical services",
    "Insufficient logging of user actions",
    "Missing data encryption at rest",
    "Weak password policy allows simple passwords",
    "No disaster recovery plan in place",
    "Single point of failure in architecture",
    "Missing input validation on forms",
    "No multi-factor authentication on admin accounts"
]

def load_prompt(filename, text):
    path = os.path.join("prompts", filename)
    with open(path, "r") as f:
        return f.read().replace("{text}", text)

print("=" * 60)
print("DEMO RECORDS TEST — 30 inputs on /describe")
print("=" * 60)

passed = 0
failed = 0

for i, text in enumerate(demo_records):
    prompt = load_prompt("describe_prompt.txt", text)
    messages = [{"role": "user", "content": prompt}]
    result = call_groq(messages)
    if result["success"] and len(result["content"]) > 50:
        passed += 1
        print(f"Record {i+1:02d}: PASS — {text[:50]}")
    else:
        failed += 1
        print(f"Record {i+1:02d}: FAIL — {text[:50]}")

print(f"\n{'='*60}")
print(f"RESULTS: {passed} passed, {failed} failed out of 30")
if failed == 0:
    print("STATUS: ALL 30 DEMO RECORDS READY!")
else:
    print("STATUS: FIX FAILING RECORDS BEFORE DEMO DAY")
print(f"{'='*60}")