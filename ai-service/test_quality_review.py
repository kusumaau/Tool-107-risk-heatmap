import os
from dotenv import load_dotenv
from groq_client import call_groq

load_dotenv()

test_inputs = [
    "Network firewall misconfiguration exposes internal systems",
    "Ransomware encrypts all company files overnight",
    "Cloud provider experiences regional outage",
    "Developer pushes untested code directly to production",
    "Customer database exposed due to missing authentication",
    "Third party vendor suffers data breach affecting our data",
    "Employees reusing weak passwords across multiple systems",
    "Unpatched software vulnerability exploited by attacker",
    "Physical server room flooded due to pipe burst",
    "API keys accidentally committed to public GitHub repository"
]

def load_prompt(filename, text):
    path = os.path.join("prompts", filename)
    with open(path, "r") as f:
        return f.read().replace("{text}", text)

def score_response(response, endpoint):
    score = 0
    if len(response) > 100:
        score += 1
    if len(response.split()) > 50:
        score += 1
    if not response.lower().startswith("i cannot"):
        score += 1
    if endpoint == "describe":
        if any(w in response.lower() for w in ["risk", "impact", "likelihood"]):
            score += 1
        if any(w in response.lower() for w in ["high", "medium", "low"]):
            score += 1
    elif endpoint == "recommend":
        if any(w in response.lower() for w in ["recommend", "action", "prevent"]):
            score += 1
        if any(w in response.lower() for w in ["high", "medium", "low", "priority"]):
            score += 1
    elif endpoint == "report":
        if any(w in response.lower() for w in ["summary", "overview", "recommendation"]):
            score += 1
        if any(w in response.lower() for w in ["risk", "impact", "threat"]):
            score += 1
    return score

def run_review(endpoint, prompt_file):
    print(f"\n{'='*60}")
    print(f"REVIEWING — {endpoint.upper()} ENDPOINT")
    print(f"{'='*60}")
    total = 0
    for i, text in enumerate(test_inputs):
        prompt = load_prompt(prompt_file, text)
        messages = [{"role": "user", "content": prompt}]
        result = call_groq(messages)
        score = score_response(result["content"], endpoint)
        total += score
        status = "PASS" if score >= 4 else "NEEDS WORK"
        print(f"Input {i+1}: Score {score}/5 — {status}")
    avg = total / len(test_inputs)
    print(f"\nAverage: {avg:.1f}/5")
    if avg >= 4:
        print(f"STATUS: PASSED")
    else:
        print(f"STATUS: NEEDS IMPROVEMENT")
    return avg

scores = []
scores.append(run_review("describe", "describe_prompt.txt"))
scores.append(run_review("recommend", "recommend_prompt.txt"))
scores.append(run_review("report", "report_prompt.txt"))

print(f"\n{'='*60}")
print(f"OVERALL QUALITY REVIEW SUMMARY")
print(f"{'='*60}")
print(f"Describe avg:    {scores[0]:.1f}/5")
print(f"Recommend avg:   {scores[1]:.1f}/5")
print(f"Report avg:      {scores[2]:.1f}/5")
print(f"Overall avg:     {sum(scores)/len(scores):.1f}/5")
if all(s >= 4 for s in scores):
    print("RESULT: ALL ENDPOINTS PASSED — Week 2 AI quality review complete!")
else:
    print("RESULT: SOME ENDPOINTS NEED IMPROVEMENT")
print(f"{'='*60}")