# Flask Login App

Small Flask API that exposes a `/login` endpoint for validating a username and password against a simple in-memory user map.

## Features

- Flask-based REST API
- `POST /login` endpoint
- Success and failure JSON responses
- Simple console logging for login attempts

## Requirements

- Python 3.10 or newer recommended
- `pip`

## Setup

Create and activate a virtual environment:

```powershell
cd c:\TEST\Cloud\flask-login-app
py -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run this once in the same terminal and activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run Locally

Start the Flask app:

```powershell
python app.py
```

The server runs on `http://127.0.0.1:5000`.

## API

### `POST /login`

Request body:

```json
{
  "username": "admin",
  "password": "admin123"
}
```

Successful response:

```json
{
  "message": "Login successful"
}
```

Failed response:

```json
{
  "message": "Login failed"
}
```

### Example request

Use the sample file [`test-app.http`](test-app.http) or send a request with PowerShell:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/login -Method Post -ContentType "application/json" -Body '{"username":"admin","password":"admin123"}'
```

## Project Files

- [`app.py`](app.py) - Flask application and `/login` route
- [`requirements.txt`](requirements.txt) - Python dependency list
- [`test-app.http`](test-app.http) - HTTP request examples for testing

## Notes

- User credentials are stored in memory for demo purposes only.
- The app listens on all interfaces (`0.0.0.0`) when run locally.