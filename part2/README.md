# HBnB - Minimal Modular Python Project

This is a starter project for the HBnB application with a clean, layered structure:
- presentation (Flask + Flask-RESTx)
- business (facade + services)
- persistence (in-memory repository + models)

## Run locally

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Run:
   ```bash
   python run.py
   ```

3. Example endpoints:
   - `POST /api/users` to create a user (JSON: {"username": "...", "email":"..."})
   - `GET /api/users/<id>` to retrieve a user

This project uses an in-memory repository (persistence/in_memory/repository.py) designed to be replaced later by SQLAlchemy.
