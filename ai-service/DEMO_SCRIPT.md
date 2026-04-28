\# AI Demo Script — Tool-107 Risk Heatmap Export Service

\## AI Developer 2 — Demo Day: Friday 9 May 2026



\---



\## My 60-Second Tech Explanation



"Our AI service is a Python Flask microservice running on port 5000.

It connects to Groq's LLaMA-3.3-70b model — one of the fastest AI

models available, completely free to use.



When a user creates a risk record, our Java backend automatically

calls our AI service. The AI analyses the risk and returns a

structured description, 3 recommendations, and a full report —

all in under 2 seconds.



Every input is sanitised before reaching the AI. We block HTML

injection, prompt injection attacks, and rate limit at 30 requests

per minute. No personal data ever reaches the AI model — our PII

audit confirmed this.



If Groq is ever unavailable, our fallback system returns a safe

response instead of crashing — so the app always stays running."



\---



\## Demo Segment 1 — AI Describe (45 seconds)



\### Input to type live:

\### Expected output contains:

\- Risk Summary

\- Likelihood: High

\- Impact: High

\- Risk Score: 8 or above

\- Affected Areas



\### What to say:

"Watch what happens when I click AI Describe.

Our Flask service receives the input, sanitises it,

sends it to Groq, and returns this structured analysis

in under 2 seconds."



\---



\## Demo Segment 2 — AI Recommend (30 seconds)



\### Input to type live:

\### Expected output contains:

\- 3 recommendations

\- action\_type: PREVENT / DETECT / RECOVER

\- priority: HIGH / MEDIUM / LOW



\### What to say:

"Now I click Recommend. The AI returns 3 actionable

recommendations with priorities. This helps the team

know exactly what to do next."



\---



\## Demo Segment 3 — Generate Report (30 seconds)



\### Input to type live:

\### Expected output contains:

\- Professional title

\- Executive summary

\- Overview

\- Key items

\- Recommendations



\### What to say:

"Finally, Generate Report creates a full professional

report ready to share with management — all from one

click."



\---



\## Demo Segment 4 — Show /health endpoint (15 seconds)



\### What to show:

Open browser and go to: http://127.0.0.1:5000/health



\### Expected output:

```json

{

&#x20; "status": "healthy",

&#x20; "model": "llama-3.3-70b-versatile",

&#x20; "uptime": "running"

}

```



\### What to say:

"Our health endpoint confirms the AI service is live

and which model is running."



\---



\## Security Talking Points (30 seconds)



"Our AI service has multiple security layers:

1\. Input sanitisation — strips HTML, blocks injection

2\. Rate limiting — 30 requests per minute per IP

3\. 6 security headers on every response

4\. PII audit — no personal data ever sent to AI

5\. Fallback response — never returns HTTP 500"



\---



\## Q\&A Answers



Q: What AI model are you using?

A: Groq LLaMA-3.3-70b-versatile — free tier, no credit card needed.



Q: What if the AI goes down?

A: Our GroqClient has 3-retry with exponential backoff.

&#x20;  If all retries fail, we return a fallback response

&#x20;  with is\_fallback: true instead of crashing.



Q: How do you prevent prompt injection?

A: Our sanitiser.py checks every input against known

&#x20;  injection patterns and returns 400 if detected.



Q: Is user data sent to the AI?

A: No. Our PII audit confirmed no personal data

&#x20;  exists in any prompt template.

