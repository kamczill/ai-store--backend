# AI Store Backend

The AI Store Backend is a robust and scalable solution designed to manage and facilitate the operations of AI Store, a modern e-commerce platform. Built with Django and Django REST framework, this backend is deployed on AWS and Heroku, ensuring high availability and reliability.

## Features

- User Authentication and Authorization
- Product Management
- Order Processing
- Cart Management
- RESTful API Endpoints
- AWS RDS Database Integration

## Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL (AWS RDS)
- AWS (Amazon Web Services)
- Heroku

## Getting Started

### Prerequisites

- Python 3.8 or later
- Pipenv or Virtualenv
- PostgreSQL

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/ai-store-backend.git
cd ai-store-backend

2. Create a virtual environment and activate it:
```bash
pipenv shell

or

```bash
virtualenv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required dependencies:
```bash
pip install -r requirements.txt

4. Configure your database settings in settings.py:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your_db_host',
        'PORT': 'your_db_port',
    }
}

5. Run migrations to create the database schema:
```bash
python manage.py migrate

6. Create a superuser to access the Django admin interface:
```bash
python manage.py createsuperuser

7. Run the development server:
```bash
python manage.py runserver

Now you can access the Django admin interface at http://127.0.0.1:8000/admin and the API endpoints at http://127.0.0.1:8000/api

## Getting Started
API documentation is available at http://127.0.0.1:8000/docs when the development server is running.

## Contributing
We welcome contributions! Please see our Contributing Guidelines for more details.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.