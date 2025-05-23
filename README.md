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
- [SQLAlchemy](https://www.sqlalchemy.org/) 
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
   Create a .env file in the project root and define your environment variables, e.g.:
   ```ini
    GOOGLE_CLIENT_ID=
    GOOGLE_CLIENT_SECRET=
    SECRET_KEY= 
    ACCESS_SECRET=
    REFRESH_SECRET=
    REFRESH_TOKEN_EXPIRE_DAYS=
    ACCESS_TOKEN_EXPIRE_MINUTES=
    JWT_ALGORITHM=HS256
    REFRESH_COOKIE_NAME=
    ACCESS_COOKIE_NAME=
   ```
5. **Run the app**
   ```bash
   uvicorn main:app --reload
   ```

License
This project is licensed under the MIT License.


   

