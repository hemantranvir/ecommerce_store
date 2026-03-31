## Overview

Simple e-commerce backend built with FastAPI supporting cart, checkout, discount system, and admin APIs.

---

## Setup Instructions

### 1. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
uvicorn app.main:app --reload
```

App will be available at:
http://127.0.0.1:8000

Swagger docs:
http://127.0.0.1:8000/docs

---

## API Endpoints

### Cart

- POST `/cart/add`

### Checkout

- POST `/checkout`

### Admin

- POST `/admin/generate-discount`
- GET `/admin/stats`

---

## Running Tests

```bash
PYTHONPATH=. pytest
```

Run specific test file:

```bash
PYTHONPATH=. pytest tests/test_services.py
```

---

## Notes

- Uses in-memory storage (resets on restart)
- Discount applies every 3rd order
- Discount codes are one-time use

---

## Future Improvements

- Add authentication (token/JWT)
- Replace in-memory store with database
- Add API-level tests (TestClient)
- Improve error handling with custom exceptions
