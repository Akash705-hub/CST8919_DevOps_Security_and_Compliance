# CST8919 Lab 1: Implementing User Login with Flask and Auth0


## Objective

In this lab, you will build a Python web application using Flask and integrate it with **Auth0** for secure authentication.

You will follow the official Auth0 Quickstart guide:
🔗 [Auth0 Python Web App Quickstart](https://auth0.com/docs/quickstart/webapp/python#configure-auth0)

By the end of this assignment, you should have a Flask app that supports login and logout via Auth0, with additional customization.

---
## About Auth0, Identity Provider & Service Provider

### What is Auth0?

**Auth0** is an **authentication and authorization platform** that helps developers add secure login, logout, and identity management features to applications with minimal effort. Instead of building user authentication from scratch, you can use Auth0 to handle login flows, tokens, and user profiles securely.

### Identity Provider (IdP)

An **Identity Provider (IdP)** is the system that verifies user identities. Examples include:
- Auth0
- Google
- Facebook
- Microsoft Entra ID

The IdP is responsible for:
- Handling login screens
- Verifying credentials
- Returning identity information to the app (like name, email, etc.)

### Service Provider (SP) / Relying Party (RP)

A **Service Provider (SP)** or **Relying Party (RP)** is the application or service that the user is trying to access — in this case, **your Flask web app**.

The SP:
- Redirects users to the IdP (Auth0) for login
- Receives authentication tokens from the IdP
- Grants or denies access based on login status

In this lab, **your Flask app is the Service Provider** and **Auth0 acts as the Identity Provider / Relying Party (RP)**.

---
## Setup and Execution

### 1. Install dependencies

Open a terminal in the `LAB1` folder and run:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Configure environment variables

The app uses Auth0 settings from environment variables. You can store them in a `.env` file in the `LAB1` folder, or export them in your shell.

Required variables:

- `AUTH0_DOMAIN`: Your Auth0 tenant domain, for example `dev-abc123.us.auth0.com`
- `AUTH0_CLIENT_ID`: Auth0 application client ID
- `AUTH0_CLIENT_SECRET`: Auth0 application client secret
- `AUTH0_SECRET`: Flask session secret key used by the app
- `AUTH0_REDIRECT_URI`: Callback URL configured in Auth0, for example `http://127.0.0.1:5001/callback`

Optional variable:

- `AUTH0_AUDIENCE`: Auth0 API audience if you need API access; leave blank if not used

Example `.env` file:

```env
AUTH0_DOMAIN=your-auth0-domain
AUTH0_CLIENT_ID=your-client-id
AUTH0_CLIENT_SECRET=your-client-secret
AUTH0_SECRET=some-random-secret
AUTH0_REDIRECT_URI=http://127.0.0.1:5001/callback
AUTH0_AUDIENCE=
```

### 3. Run the application

From the `LAB1` folder, start the Flask app:

```powershell
python app.py OR py app.py
```

Then open:

```text
http://127.0.0.1:5001/
```

### 4. Use the app

- Visit `/` to see the home page
- Click **Login** to authenticate with Auth0
- Visit `/profile` to view the logged-in user profile
- Use `/logout` to sign out

### 5. Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Home page showing login status and login button |
| `/login` | GET | Redirects to Auth0 for login |
| `/callback` | GET | Auth0 callback URL after login |
| `/profile` | GET | Protected profile page for logged-in users |
| `/protected` | GET | Protected page that also requires login |
| `/logout` | GET | Logs the user out and redirects back to home |
| `/hello` | GET | Simple test route returning `Hello World` |

Recording: https://drive.google.com/file/d/1Qkk3TsmSvH2yEyAP-zJ1HgCobbQMdtlV/view?usp=sharing
---
