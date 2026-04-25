\# SECURITY.md — Tool-107 Risk Heatmap Export Service



\## Threat Model



| # | Threat | Description | Mitigation Plan |

|---|--------|-------------|-----------------|

| 1 | Prompt Injection | Attacker crafts input to manipulate the AI model | Sanitise all user input before inserting into prompts |

| 2 | SQL Injection | Malicious SQL in input fields could expose the database | Use JPA parameterised queries only |

| 3 | Broken Authentication | API endpoints accessed without a valid JWT token | Spring Security validates JWT on every request |

| 4 | Sensitive Data Exposure | PII accidentally sent to the Groq API | Audit all prompts, never include personal data |

| 5 | Rate Limit Bypass | Attacker floods Flask AI service to exhaust Groq quota | flask-limiter enforces 30 req/min per IP |



\## Status

\- \[ ] Threats identified: 5

\- \[ ] Tests conducted: Not started

\- \[ ] Findings fixed: Not started

\- \[ ] Team sign-off: Pending

