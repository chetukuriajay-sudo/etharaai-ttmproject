# 🚀 Team Task Manager

A full-stack web application built using **Django** that helps teams manage projects and tasks efficiently.

---

## 📌 Features

- 👤 User Authentication (Login / Signup / Logout)
- 📊 Dashboard with task overview
- 📁 Project Management
- ✅ Task Management
- 🗑️ Delete Account feature
- 🔍 Searchable dropdowns using Select2
- 💻 Responsive UI with custom CSS

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Deployment:** Railway
- **Server:** Gunicorn
- **Static Files:** WhiteNoise

---

## 📂 Project Structure

```
team_task_manager/
│── manager/             # Main app
│── static/              # CSS, JS files
│── templates/           # HTML templates
│── team_task_manager/   # Project settings
│── manage.py
│── requirements.txt
│── Procfile
```

---

## ⚙️ Installation (Run Locally)

```bash
git clone https://github.com/chetukuriajay-sudo/etharaai-ttmproject.git
cd etharaai-ttmproject

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

---

## 🌐 Live Demo

👉 https://etharaai-ttmproject-production.up.railway.app

---

## 🚀 Deployment

This project is deployed using **Railway** with:

- Gunicorn server
- WhiteNoise for static files

---

## 👨‍💻 Author

**Chethukuri Ajay Kumar**

- GitHub: https://github.com/chetukuriajay-sudo

---

## ⭐ Future Improvements

- Better UI/UX design
- Notifications system
- Role-based access
- Task deadlines & reminders
- Analytics dashboard

---

## 📌 Note

Make sure static files are properly configured using **WhiteNoise** for production deployment.

---

⭐ If you like this project, give it a star!
