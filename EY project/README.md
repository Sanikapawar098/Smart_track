# smartComplaint_project (Flower Nursery - Complaint System)

This repository contains a minimal Django project demonstrating:

- Custom `User` model with `is_society_manager` and `is_citizen` flags.
- `CitizenProfile`, `Citizen`, and `Complaint` models.
- Basic authentication and dashboards for citizens and managers.

Quick setup:

1. Create a virtual environment and activate it.

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Commands the project was scaffolded with (examples):

```bash
django-admin startproject smartComplaint_project .
python manage.py startapp core_app
```

4. Apply migrations and create a superuser:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

Project notes:
- The `AUTH_USER_MODEL` is set to `core_app.User` in `smartComplaint_project/settings.py`.
- Login redirect is configured via `LOGIN_REDIRECT_URL = '/'`.
- Use the admin site (`/admin/`) to manage users, citizens, profiles and complaints.
