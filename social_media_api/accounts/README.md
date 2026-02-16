📘 Social Media API

A RESTful Social Media API built with Django and Django REST Framework featuring custom user authentication and token-based authentication.

🚀 Features

Custom User Model

User Registration

Login with Token Authentication

User Profile Management

Followers System (self-referencing relationship)

🛠 Installation
git clone <repository-url>
cd social_media_api
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt


⚙️ Run Migrations
python manage.py makemigrations
python manage.py migrate

▶️ Run Server
python manage.py runserver


🔐 Authentication

This API uses Token Authentication.

After login, include the token in headers:

Authorization: Token your_token_here



| Endpoint       | Method  | Description                |
| -------------- | ------- | -------------------------- |
| /api/register/ | POST    | Register new user          |
| /api/login/    | POST    | Login and get token        |
| /api/profile/  | GET/PUT | Retrieve or update profile |




🧠 User Model

Custom User model extends Django AbstractUser with:

bio

profile_picture

followers (ManyToMany self-reference)