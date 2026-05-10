\# AI Talking Points Card — Tool-107

\## AI Developer 2 | Demo Day: Friday 9 May 2026



\---



\## What is Groq?

\- Groq is a free AI API that runs LLaMA-3.3-70b-versatile model

\- No credit card needed — free tier at console.groq.com

\- Extremely fast inference — responses in under 2 seconds

\- We send a prompt, Groq returns AI-generated text as JSON



\---



\## How Our 3 AI Endpoints Work



\### 1. POST /describe

\- User sends a risk scenario text

\- We load describe\_prompt.txt template

\- Send it to Groq with temperature 0.3 (factual)

\- Groq returns: summary, likelihood, impact, score

\- Response time: \~1.8 seconds



\### 2. POST /recommend

\- User sends a risk scenario text

\- We load recommend\_prompt.txt template

\- Groq returns 3 recommendations as JSON array

\- Each has: action\_type, description, priority

\- Response time: \~0.6 seconds



\### 3. POST /generate-report

\- User sends a risk scenario text

\- We load report\_prompt.txt template

\- Groq returns full professional risk report

\- Fields: title, summary, overview, key items, recommendations

\- Response time: \~2.3 seconds



\---



\## How Prompts Work

\- Prompt templates are plain text files in prompts/ folder

\- We load the template, inject the user's risk text

\- Send to Groq with messages array format

\- Temperature 0.3 = factual and consistent output

\- Temperature 0.7 = more creative output

\- max\_tokens = 1000 to control response length



\---



\## What Happens if Groq Fails?

\- Every Groq call is wrapped in try-except

\- We retry 3 times with exponential backoff

\- 1st retry after 1 second

\- 2nd retry after 2 seconds

\- 3rd retry after 4 seconds

\- If all fail — return fallback template with is\_fallback: true

\- We NEVER return HTTP 500 because AI is unavailable



\---



\## Security Talking Points



\### Input Sanitisation

\- Every request passes through sanitiser.py

\- Strips all HTML tags from input

\- Detects prompt injection attempts

\- Returns HTTP 400 if injection detected

\- User never gets direct access to our prompts



\### Rate Limiting

\- flask-limiter blocks IPs after 30 requests/minute

\- Prevents abuse and API key exhaustion

\- Returns HTTP 429 Too Many Requests



\### 6 Security Headers

Applied to every response:

\- X-Content-Type-Options: nosniff

\- X-Frame-Options: DENY

\- X-XSS-Protection: 1; mode=block

\- Strict-Transport-Security

\- Content-Security-Policy

\- Referrer-Policy



\### PII Audit

\- No personal data ever sent to Groq

\- Only risk scenario text is sent

\- Confirmed clean in PII audit



\---



\## One Line Answers for Q\&A



Q: What AI model do you use?

A: Groq LLaMA-3.3-70b-versatile — free, fast, no credit card needed.



Q: What if AI is down?

A: 3 retries with backoff, then fallback response. Never crashes.



Q: How do you prevent prompt injection?

A: sanitiser.py detects and blocks it with HTTP 400.



Q: What is temperature in AI?

A: Controls creativity. 0.3 = factual, 0.7 = creative. We use 0.3.



Q: How fast are your endpoints?

A: /describe \~1.8s, /recommend \~0.6s, /generate-report \~2.3s

