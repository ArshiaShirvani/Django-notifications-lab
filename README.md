# Django Notifications Lab

A lightweight Django sandbox project for testing and comparing different JavaScript-based notification systems (such as Toastify, SweetAlert2, Notiflix, and others).  
This repository is intended as a practical reference for developers who want to quickly experiment with UI notification patterns and integrate them into Django applications.

## Purpose

The project provides:

- A simple Django environment for experimenting with toast/alert notification libraries.
- Examples of how JavaScript notification components can be integrated into Django templates.
- A structured playground to help developers evaluate and select the most suitable notification system for their own projects.

## Project Structure

```
core/               # Main Django project
templates/          # HTML templates including notification demos
website/            # Static files (JS / CSS) for notification libraries
requirements.txt    # Python dependencies
manage.py           # Django management script
```

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/ArshiaShirvani/Django-notifications-lab.git
cd Django-notifications-lab
```

### 2. (Optional) Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
# or
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations and start the development server
```bash
python manage.py migrate
python manage.py runserver
```

### 5. Open in browser
Visit:
```
http://127.0.0.1:8000/
```
You can explore templates that demonstrate various notification libraries.

## Usage

You can:

- Inspect HTML templates to see how each notification library is integrated.
- Review JavaScript files under `website/` to understand how notifications are triggered.
- Add new notification libraries and compare differences in styling, UX, and integration complexity.
- Use this project as a boilerplate for implementing toasts/alerts in real Django applications.

## Roadmap

Planned or recommended enhancements:

- Add more JavaScript notification libraries.
- Show Django backend-triggered notifications (e.g., after POST actions).
- Provide reusable mixins or helper utilities for Django messages.
- Add screenshots or GIF demos.
- Add example REST notification endpoints.

## License

This project is released under the MIT License.

## Contact

You can reach me via:

- Email:  mailto:arshiashirvani.f1385@gmail.com
- LinkedIn:  https://www.linkedin.com/in/arshia-shirvani-2ba593325/


