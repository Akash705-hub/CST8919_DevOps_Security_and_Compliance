# Assignment 1 - Flask Auth0 App with Structured Logging

## Overview

This assignment extends the Flask application from Lab 1 by integrating Auth0 authentication and adding structured application logging for:

- successful logins
- access to the `/protected` route
- unauthorized access attempts

## Features

- Auth0 login and logout flow
- Protected routes for authenticated users
- Structured JSON logging with fields such as:
  - `event`
  - `timestamp`
  - `user_id`
  - `email`
  - `path`
  - `remote_addr`

## Project Structure

- `app.py` - Flask application and route handlers
- `auth.py` - Auth0 server client configuration
- `templates/` - HTML templates for login/profile pages
- `static/` - CSS assets
- `tests/` - basic logging regression tests

## Prerequisites

- Python 3.10+
- An Auth0 tenant and application
- Access to Azure App Service (optional, for deployment/testing logs)

## Environment Variables

Create a `.env` file in the Assignment1 folder with the following values:

```env
AUTH0_DOMAIN=your-auth0-domain
AUTH0_CLIENT_ID=your-auth0-client-id
AUTH0_CLIENT_SECRET=your-auth0-client-secret
AUTH0_SECRET=your-flask-secret-key
AUTH0_REDIRECT_URI=http://127.0.0.1:5001/callback
AUTH0_AUDIENCE=
```

## Installation

From the Assignment1 folder, run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q tests/test_logging.py
```

## Run the Application

```powershell
py app.py
```

Then open:

```text
http://127.0.0.1:5001/
```

## Routes

- `/` - Home page
- `/login` - Redirects to Auth0 login
- `/callback` - Auth0 callback handler
- `/profile` - Protected profile page
- `/protected` - Protected route that logs access
- `/logout` - Logout endpoint
- `/hello` - Simple test endpoint

## Logging Behavior

The app logs the following events:

- `login_event` for successful authentication
- `protected_route_access` for authorized access to `/protected`
- `unauthorized_attempt` when access is denied

These logs are emitted using `app.logger.info()` and `app.logger.warning()` in JSON format.

## Explanation of Logging and Detection Logic

The application uses structured logging so each event contains a consistent format with fields such as `event`, `timestamp`, `user_id`, `email`, `path`, and `remote_addr`.

This makes it possible to detect suspicious behavior in Azure Monitor:

- A user who repeatedly accesses `/protected` may be showing abnormal behavior.
- The detection logic groups log entries by `user_id`.
- If the same user has more than 10 accesses within a 15-minute window, the condition is flagged.

## KQL Query for Detection

Use the following KQL query in Log Analytics or Azure Monitor Logs:

```kusto
AppServiceConsoleLogs
| where TimeGenerated > ago(15m)
| where ResultDescription has "protected_route_access"
| extend json_text = extract(@'\{.*\}', 0, ResultDescription)
| extend payload = parse_json(json_text)
| extend user_id = tostring(payload.user_id)
| where isnotempty(user_id)
| summarize access_count = count(), timestamp = max(TimeGenerated) by user_id
| where access_count > 10
| project user_id, timestamp, access_count
| order by access_count desc
```

## Alert Logic

To trigger an alert in Azure Monitor:

- Create a Log Alert in Azure Monitor
- Use the query above
- Set the alert to evaluate every 5 minutes
- Use an aggregated log query with:
  - Measure: `access_count`
  - Aggregation type: `Total`
  - Threshold type: `Static`
  - Operator: `Greater than`
  - Threshold value: `10`
- Add an Action Group to send email notifications
- Set severity to `3 (Low)`

## Notes

If you deploy this app to Azure App Service, you can view the logs in:

- Log stream
- Application Insights (if configured)
- Log Analytics workspace (if connected)
