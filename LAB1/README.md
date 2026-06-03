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
