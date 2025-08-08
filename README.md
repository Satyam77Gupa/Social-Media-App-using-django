# Social Media Dashboard using Django

A web-based Social Media Dashboard built using **Django Framework** that provides users with an interactive interface to manage, analyze, and visualize social media activities across different platforms.

---

## 🚀 Features
- **User Authentication**: Secure login and signup functionality.
- **Dashboard Overview**: Displays social media metrics and analytics.
- **Post Scheduling**: Schedule posts for different platforms.
- **Analytics Charts**: Visual representation of followers, engagement, and reach.
- **Responsive Design**: Fully responsive layout for all devices.

---

## 🛠️ Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Database**: SQLite (default Django DB)
- **Version Control**: Git & GitHub

---

Social-Media-Dashboard-using-Django/
│
├── dashboard/          # Main app
├── templates/          # HTML Templates
├── static/             # CSS, JS, Images
├── manage.py
├── requirements.txt
└── README.md

Set By step process to run the programming.

# 1. Unzip the project

- Copy code

unzip Social-Media-Dashboard-using-Django-main.zip
cd Social-Media-Dashboard-using-Django-main

# 2. Create and activate a virtual environment (recommended)

- Copy code
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate


# 3.Install dependencies

- If the project has a requirements.txt:

Copy code
pip install -r requirements.txt

# 4. Run database migrations

- Copy code
python manage.py migrate


# 5. Start the development server

- Copy code
python manage.py runserver

# 6. View in browser

- Open & copy to paste in Browser:

http://127.0.0.1:8000/

# Note: 1.  Installed SQLite.
#        2.   If python manage.py gives an error like "No such file or directory", it means you’re not inside the folder that contains manage.py.
#             We’ll need to cd into the right subfolder first.
