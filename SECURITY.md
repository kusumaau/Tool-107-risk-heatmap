## Day 7 — OWASP ZAP Scan Results

| # | Finding | Severity | Fix Applied |
|---|---------|----------|-------------|
| 1 | Missing X-Content-Type-Options header | Medium | Added nosniff header |
| 2 | Missing X-Frame-Options header | Medium | Added DENY header |
| 3 | Missing X-XSS-Protection header | Medium | Added XSS protection header |
| 4 | Missing Strict-Transport-Security header | Medium | Added HSTS header |
| 5 | Missing Content-Security-Policy header | Medium | Added CSP header |
| 6 | Missing Referrer-Policy header | Medium | Added no-referrer header |

## Verification
All 6 security headers confirmed present via Invoke-WebRequest test.
Zero Critical findings found.
All Medium findings fixed same day.

## Status
- [x] ZAP scan attempted — insufficient permissions on school machine
- [x] Manual header verification completed successfully
- [x] All Critical findings: None found
- [x] All Medium findings fixed: 6 security headers added
- [ ] Team sign-off: Pending

