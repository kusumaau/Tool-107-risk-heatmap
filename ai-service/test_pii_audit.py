import os

print("=" * 60)
print("PII AUDIT — Checking prompts for personal data")
print("=" * 60)

prompts_folder = "prompts"
pii_keywords = [
    "email", "phone", "address", "name", "password",
    "credit card", "social security", "date of birth",
    "passport", "license", "salary", "bank account"
]

all_clean = True

for filename in os.listdir(prompts_folder):
    filepath = os.path.join(prompts_folder, filename)
    with open(filepath, "r") as f:
        content = f.read().lower()

    found = [kw for kw in pii_keywords if kw in content]
    if found:
        print(f"WARNING — {filename} contains PII keywords: {found}")
        all_clean = False
    else:
        print(f"CLEAN — {filename} — no PII keywords found")

print("\n" + "=" * 60)
if all_clean:
    print("PII AUDIT RESULT: PASSED — No personal data in prompts")
else:
    print("PII AUDIT RESULT: FAILED — Fix prompts before proceeding")
print("=" * 60)