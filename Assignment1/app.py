import json
import logging
import os
import sys
from datetime import datetime, timezone

from flask import Flask, redirect, render_template, request, url_for, g
from auth0_server_python.auth_types import LogoutOptions
from auth import auth0
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("AUTH0_SECRET")
app.logger.setLevel(logging.INFO)

if not app.logger.handlers:
    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    app.logger.addHandler(handler)

app.logger.propagate = False


def log_event(level, event_name, **details):
    """Emit structured application logs with JSON payloads."""
    payload = {
        "event": event_name,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        **details,
    }
    message = json.dumps(payload, default=str)
    if level == "warning":
        app.logger.warning(message)
    else:
        app.logger.info(message)


# Configure session for Auth0
app.config.update(
    SESSION_COOKIE_SECURE=False,  # Set to True in production with HTTPS
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)


@app.before_request
def store_request_response():
    """Make request/response available for Auth0 SDK"""
    g.store_options = {"request": request}


@app.route("/")
async def index():
    """Home page - shows login button or user profile"""
    user = await auth0.get_user(g.store_options)
    return render_template("index.html", user=user)


@app.route("/login")
async def login():
    """Redirect to Auth0 login"""
    authorization_url = await auth0.start_interactive_login({}, g.store_options)
    return redirect(authorization_url)


@app.route("/callback")
async def callback():
    """Handle Auth0 callback after login"""
    try:
        result = await auth0.complete_interactive_login(
            str(request.url), g.store_options
        )
        user = await auth0.get_user(g.store_options)
        if user:
            log_event(
                "info",
                "login_event",
                user_id=user.get("sub") or user.get("user_id") or "unknown",
                email=user.get("email") or "unknown",
            )
        return redirect(url_for("index"))
    except Exception as e:
        return f"Authentication error: {str(e)}", 400


@app.route("/profile")
async def profile():
    """Protected route - shows user profile"""
    user = await auth0.get_user(g.store_options)

    if not user:
        return redirect(url_for("login"))

    return render_template("profile.html", user=user)


@app.route("/protected")
async def protected_page():
    """Protected route - shows user profile"""
    user = await auth0.get_user(g.store_options)

    if not user:
        log_event(
            "warning",
            "unauthorized_attempt",
            path=request.path,
            remote_addr=request.remote_addr or "unknown",
        )
        return redirect(url_for("login"))

    log_event("info", "protected_route_access", user_id=user.get("sub") or "unknown")
    return render_template("profile.html", user=user)


@app.route("/logout")
async def logout():
    """Logout and redirect to Auth0 logout"""
    options = LogoutOptions(return_to=url_for("index", _external=True))
    logout_url = await auth0.logout(options, g.store_options)
    return redirect(logout_url)


@app.route("/hello")
async def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
