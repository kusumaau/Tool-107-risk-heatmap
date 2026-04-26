import requests

print("Testing rate limiting — sending 15 requests rapidly...")
blocked = False

for i in range(15):
    response = requests.post(
        "http://127.0.0.1:5000/describe",
        json={"text": "test risk scenario"},
        timeout=5
    )
    print(f"Request {i+1}: Status {response.status_code}")
    if response.status_code == 429:
        print(f"Rate limit triggered at request {i+1} — WORKING!")
        blocked = True
        break

if blocked:
    print("\nRate limiting: PASS")
else:
    print("\nRate limiting: All requests went through — check config")