# 🔐 Secure Auth API



![CI Pipeline](https://github.com/MohammadAleem/secure-auth-api/actions/workflows/ci.yml/badge.svg)



A production-ready secure REST API built with Flask featuring JWT authentication, 
bcrypt password hashing, rate limiting, and security headers.

---

## 🛡️ Security Features

- JWT token based authentication
- bcrypt password hashing
- Rate limiting to prevent brute force attacks
- Security headers (XSS, CSRF, Clickjacking protection)
- Input validation and sanitization
- Suspicious activity logging

---

## 🛠️ Tech Stack

Python • Flask • JWT • bcrypt • Docker • GitHub Actions

---

## 🚀 Quick Start

### Run Locally
### Run with Docker
---

## 📡 API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | /register | Register new user | No |
| POST | /login | Login and get JWT token | No |
| GET | /protected | Access protected resource | Yes |
| GET | /health | Health check | No |

---

## 🔒 Security Concepts Demonstrated

- Password hashing with bcrypt (never store plain text passwords)
- JWT tokens for stateless authentication
- Rate limiting to block brute force attacks
- Security headers to prevent common web attacks
- Activity logging for suspicious behavior detection

---

## 📋 Future Improvements

- [ ] PostgreSQL database integration
- [ ] Refresh token rotation
- [ ] Two factor authentication (2FA)
- [ ] IP blacklisting
- [ ] Full test coverage
