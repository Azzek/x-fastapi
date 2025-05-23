# X-FastAPI

A FastAPI-based backend project featuring authentication, authorization, and post management. Designed for simplicity, speed, and scalability.

## Features

- Logging in / Register users with google OAuth 2.0
- JWT-based Authentication and Authorization
- Create, Read, Update, and Delete (CRUD) operations for Posts
- Role-based access control
- Input validation with Pydantic

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/) (or your ORM of choice)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/) as the ASGI server
- [python-jose](https://pypi.org/project/python-jose/) for JWT handling
- [passlib](https://passlib.readthedocs.io/) for password hashing

## 🛠 Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/Azzek/x-fastapi.git
   cd x-fastapi
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # on Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Get up your .env file**
   Copy the .env.example file to .env in the project root and configure your environment variables, e.g.:
   ```ini
   cp .env.example .env
   ```
5. **Run the app**
   ```bash
   uvicorn main:app --reload
   ```

License
This project is licensed under the MIT License.
