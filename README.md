# Currency Converter

A Django-based currency converter application that allows users to convert between different currencies, manage exchange rates, and view conversion history.

## Features

- User registration and authentication
- Currency conversion with real-time results
- Personal and global exchange rates
- Conversion history tracking
- Admin interface for managing currencies and rates

## Requirements

- Python 3.8 or higher
- Django 4.2 or higher
- SQLite3 (included with Python)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd currency-converter
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install django
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Usage

1. Access the application at http://localhost:8000
2. Register a new account or log in with existing credentials
3. Use the currency converter to convert between currencies
4. Manage exchange rates in the Exchange Rates section
5. View your conversion history in the History section

## Admin Interface

1. Access the admin interface at http://localhost:8000/admin
2. Log in with your superuser credentials
3. Manage currencies, exchange rates, and view conversion history

## Project Structure

- `converter/` - Main application directory
  - `models.py` - Database models
  - `views.py` - View functions
  - `urls.py` - URL routing
  - `templates/` - HTML templates
  - `admin.py` - Admin interface configuration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 