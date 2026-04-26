import os
from dotenv import load_dotenv
from groq_client import call_groq

load_dotenv()

test_inputs = [
    "Server crashes during peak hours",
    "Database backup fails silently",
    "Unauthorized access to admin panel",
    "Third party API goes down unexpectedly",
    "Employee accidentally deletes production data",
    "Payment gateway timeout during checkout",
    "SSL certificate expires without warning",
    "Insider threat leaks customer data",
    "DDoS attack overwhelms the web server",
    "Cloud storage bucket left publicly accessible"
]

def load_prompt(filename, text):
    path = os.path.join("prompts", filename)
    with open(path, "r") as f:
        return f.read().replace("{text}", text)

def score_response(response):
    score = 0
    if len(response) > 100:
        score += 3
    if any(word in response.lower() for word in ["risk", "impact", "likelihood", "recommend"]):
        score += 3
    if len(response.split()) > 50:
        score += 2
    if not response.lower().startswith("i cannot"):
        score += 2
    return score

print("=" * 60)
print("PROMPT TUNING RESULTS — DESCRIBE ENDPOINT")
print("=" * 60)

total_score = 0
for i, text in enumerate(test_inputs):
    prompt = load_prompt("describe_prompt.txt", text)
    messages = [{"role": "user", "content": prompt}]
    result = call_groq(messages)
    score = score_response(result["content"])
    total_score += score
    print(f"\nInput {i+1}: {text}")
    print(f"Score: {score}/10")
    print(f"Response preview: {result['content'][:150]}...")

avg = total_score / len(test_inputs)
print("\n" + "=" * 60)
print(f"AVERAGE SCORE: {avg:.1f}/10")
if avg >= 7:
    print("STATUS: PASSED — prompts are performing well!")
else:
    print("STATUS: NEEDS IMPROVEMENT — rewrite prompts")
print("=" * 60)