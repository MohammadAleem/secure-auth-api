from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import bcrypt
import os
import logging
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Security config
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "dev-secret-change-in-production")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-change-in-production")

# JWT setup
jwt = JWTManager(app)

# Rate limiter — prevents brute force attacks
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

# Logging suspicious activity
logging.basicConfig(
    filename="security.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# In-memory user store (replace with database later)
users = {}

# Security headers middleware
@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000"
    return response

# Register endpoint
@app.route("/register", methods=["POST"])
@limiter.limit("5 per minute")
def register():
    data = request.get_json()

    # Input validation
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username and password required"}), 400

    username = data["username"].strip()
    password = data["password"]

    # Password strength check
    if len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Hash password before storing
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    users[username] = hashed

    return jsonify({"message": "User registered successfully"}), 201

# Login endpoint
@app.route("/login", methods=["POST"])
@limiter.limit("10 per minute")
def login():
    data = request.get_json()

    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username and password required"}), 400

    username = data["username"].strip()
    password = data["password"]

    if username not in users:
        # Log failed attempt
        logging.warning(f"Failed login attempt for username: {username}")
        return jsonify({"error": "Invalid credentials"}), 401

    # Verify hashed password
    if not bcrypt.checkpw(password.encode("utf-8"), users[username]):
        logging.warning(f"Failed login attempt for username: {username}")
        return jsonify({"error": "Invalid credentials"}), 401

    # Generate JWT token
    access_token = create_access_token(identity=username)
    return jsonify({"access_token": access_token}), 200

# Protected endpoint
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Hello {current_user}, you are authenticated"}), 200

# Health check
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "running"}), 200

if __name__ == "__main__":
    app.run(debug=False)
