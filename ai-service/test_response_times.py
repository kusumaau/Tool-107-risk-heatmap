import requests
import time

BASE_URL = "http://127.0.0.1:5000"
TEST_INPUT = "Server crashes during peak hours causing revenue loss"

endpoints = [
    ("/describe", "description"),
    ("/recommend", "recommendations"),
    ("/generate-report", "report")
]

print("=" * 60)
print("RESPONSE TIME TEST — Demo Day dry run")
print("=" * 60)

for endpoint, key in endpoints:
    start = time.time()
    response = requests.post(
        f"{BASE_URL}{endpoint}",
        json={"text": TEST_INPUT},
        timeout=30
    )
    elapsed = time.time() - start
    data = response.json()

    status = "PASS" if response.status_code == 200 else "FAIL"
    speed = "FAST" if elapsed < 2 else "SLOW"

    print(f"\nEndpoint: {endpoint}")
    print(f"Status: {status} ({response.status_code})")
    print(f"Response time: {elapsed:.2f}s — {speed}")
    print(f"Preview: {str(data.get(key, ''))[:100]}...")

print(f"\n{'='*60}")
print("Health check:")
r = requests.get(f"{BASE_URL}/health")
print(r.json())
print("=" * 60)