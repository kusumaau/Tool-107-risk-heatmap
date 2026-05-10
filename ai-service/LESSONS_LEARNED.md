\# Lessons Learned — Tool-107 Risk Heatmap Export Service

\## AI Developer 2 | Sprint: 14 April – 9 May 2026



\---



\## What Went Well

\- Groq API integration worked smoothly with LLaMA-3.3-70b-versatile

\- All 3 AI endpoints (/describe, /recommend, /generate-report) working correctly

\- Input sanitisation and prompt injection detection working perfectly

\- Rate limiting (30 req/min) working as expected

\- 3-retry with exponential backoff prevents crashes on AI failure

\- Fallback response (is\_fallback: true) ensures service never crashes

\- All 8 pytest unit tests passing

\- Response times within targets (\~1.8s, \~0.6s, \~2.3s)



\---



\## What Was Challenging

\- GitHub push protection blocked push when API key was accidentally

&#x20; committed in README.md

\- Had to rewrite git history using filter-branch to remove secret

\- PowerShell curl syntax is different from Linux/Mac curl

\- Groq API rate limits on free tier required careful retry logic



\---



\## Mistakes Made and Fixed

\- Accidentally committed Groq API key in README.md line 52

&#x20; Fix: Removed key, rewrote git history, rotated API key immediately

\- Dockerfile had .txt extension

&#x20; Fix: Renamed to Dockerfile using PowerShell Rename-Item command

\- Wrong branch (master vs main) confusion with forked repo

&#x20; Fix: Created fresh personal repo at Tool-107-risk-heatmap



\---



\## Features for Future Sprints

\- Add ChromaDB vector database for semantic search on past risk reports

\- Add PDF export for generated reports

\- Add email delivery of generated reports

\- Add authentication to AI service endpoints

\- Add response caching with Redis for identical inputs

\- Add dashboard showing AI usage statistics

\- Support multiple AI models (GPT-4, Claude, Gemini) as fallback chain

\- Add confidence score to each AI response



\---



\## Feedback for Mentor

\- Daily step-by-step guidance was very helpful

\- More time should be allocated for Docker Compose setup

\- Security review (OWASP ZAP) should start earlier in the sprint

\- Gro

