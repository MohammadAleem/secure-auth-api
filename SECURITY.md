# Security Policy

---

## 🔐 Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x   | ✅ Yes    |

---

## 🚨 Reporting a Vulnerability

If you discover a security vulnerability in this project:

**Do NOT open a public GitHub issue.**

Instead:
1. Email directly with subject: `[SECURITY] secure-auth-api vulnerability`
2. Describe the vulnerability in detail
3. Include steps to reproduce
4. Include potential impact

---

## ⏱️ Response Timeline

- **Initial response** within 48 hours
- **Fix timeline** within 7 days for critical issues
- **Credit** given to reporter in CHANGELOG

---

## 🛡️ Security Best Practices Used

- Passwords hashed with bcrypt
- JWT tokens for stateless authentication
- Rate limiting to prevent brute force attacks
- Security headers on all responses
- Input validation and sanitization
- Suspicious activity logging
- Secrets managed via environment variables
- `.env` excluded from version control

---

## ⚠️ Known Limitations

- Currently uses in-memory user storage
- No refresh token rotation yet
- No 2FA implemented yet

These are tracked in GitHub Issues and will be resolved in future versions.
