# AI Demo Script — Tool-107
## AI Developer 2 | Demo Day: Friday 9 May 2026

## My 60-Second Tech Explanation
"Our AI service is a Python Flask microservice on port 5000.
It uses Groq LLaMA-3.3-70b — one of the fastest free AI models.
Every input is sanitised before reaching the AI.
We block HTML injection and prompt injection attacks.
Rate limiting is set at 30 requests per minute.
No personal data ever reaches the AI — PII audit confirmed this.
If Groq fails, our fallback returns a safe response instead of crashing."

## Demo Input to use live
Server crashes during peak hours causing revenue loss

## Endpoint 1 — /describe (say this)
"Watch the AI return a structured risk analysis in under 2 seconds
with likelihood, impact, risk score and affected areas."

## Endpoint 2 — /recommend (say this)
"Now the AI returns 3 actionable recommendations
with action type PREVENT/DETECT/RECOVER and priority levels."

## Endpoint 3 — /generate-report (say this)
"Finally a full professional report — title, summary,
overview, key items and recommendations — one click."

## /health endpoint (say this)
"Our health endpoint confirms the AI service is live
and which model is running."
Open browser: http://127.0.0.1:5000/health

## Security Talking Points
1. Input sanitisation — strips HTML, blocks injection
2. Rate limiting — 30 requests per minute per IP
3. 6 security headers on every response
4. PII audit — no personal data sent to AI
5. Fallback — never returns HTTP 500

## Q&A Answers
Q: What AI model?
A: Groq LLaMA-3.3-70b-versatile — free, no credit card.

Q: What if AI goes down?
A: 3-retry with backoff, then fallback with is_fallback:true.

Q: How do you prevent prompt injection?
A: sanitiser.py checks every input, returns 400 if detected.

Q: Is user data sent to AI?
A: No — PII audit confirmed no personal data in any prompt.