## Requirements

- Python 3.x
- Django 3.x or higher
- Django Channels (for WebSocket support)
- A database (SQLite is used by default)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/chat-application.git
   cd chat-application

   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   http://127.0.0.1:8000/

