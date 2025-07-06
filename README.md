# 🧾 Exam Bill Management System

A web-based application built to automate the generation of faculty exam bills, reducing manual effort and improving calculation accuracy.

---
## 📦 Backend – Django (MVC Architecture)

### 🔧 Features

- Developed using **Django**, following the **MVC (Model-View-Controller)** architecture.
- Securely manages exam-related billing data.
- Core functionalities:
  - CRUD operations on:
    - Faculty Member details
    - Exam Committee details
    - Exam Bill Rates
  - Stores:
    - Records of Exam Bills submitted by faculty
    - Workloads for each course and semester
    - Bank account information of teachers
    - Exam Committee Chief names by session

### 🧩 Tools & Technologies

- **Django**
- **SQLite/MySQL** (or your preferred DB)
- **Python**
- **Django Admin** (for management)

---
## 🌐 Frontend – React

### 💡 Features

- Built with **React.js** and **Bootstrap** for a dynamic, responsive UI.
- Form inputs render **dynamically** based on selected criteria:
  - e.g., "No. of Hours" for Lab Exams, "No. of Students" for Evaluating Scripts.
- Functional Pages:
  - Home Page
  - Faculty Members List
  - Individual Bill Generation Form
  - Final Bill Display

### 🔄 Workflow

1. Select a semester → Relevant courses are displayed.
2. Select a course → Dynamic input fields appear.
3. Fill out the form → Click **"Prepare My Bill"** → Final bill is generated.

### 🧰 Tools & Libraries

- **React**
- **Bootstrap**
- **HTML5/CSS3**
- **Axios** (if fetching data from backend APIs)

### 📁 Sample Folder Structure
```
Exam_Billing_System_JU_FRONTEND/
├── public/
│ └── index.html
├── src/
│ ├── components/
│ │ ├── FacultyCards.js
│ │ ├── BillingForm.js
│ ├── App.js
│ ├── index.js
```

---

## ✅ System Highlights

- 🚫 **No Manual Calculations**
- ⏱️ **Saves Time and Labor**
- 📌 **Auto-suggests Routine Courses**
- 📊 **Generates Detailed Reports**
- 🔐 **Ensures Data Confidentiality, Integrity, and Availability**

---


# 🧾 Exam Bill Management System – Full Stack Setup

A full-stack web application to automate the generation and management of faculty exam bills at Jahangirnagar University.

---

## 📦 Backend – Django (MVC)

### 📁 Folder Structure 

```
Exam_Billing_System_JU_BACKEND/
├── day4app/
├── myproject/
├── templates/
│ └── day4/
├── db.sqlite3
├── manage.py
├── routine.csv
├── routine.txt

```
### 🧰 Prerequisites

- Python 3.8+
- pip (Python package installer)
- Virtualenv (recommended)

### 🚀 Local Installation Steps


# 1. Clone the repository
```
git clone https://github.com/Akila-Nipo/Exam_Billing_System_JU_BACKEND.git
cd Exam_Billing_System_JU_BACKEND
```

# 2. Create a virtual environment
```
python -m venv env
source env/bin/activate     # For Windows: env\Scripts\activate
```

# 3. Install required packages
```
pip install django
```

# 4. Run migrations
```
python manage.py makemigrations
python manage.py migrate
```

# 5. Create superuser (optional but recommended)
```
python manage.py createsuperuser
```

# 6. Run the development server
```
python manage.py runserver
```
### ✅ Access

- **App**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

  ## 🌐 Frontend – React

### 📁 Folder Structure 

```
Exam_Billing_System_JU_FRONTEND/
├── public/
├── src/
├── .gitignore
├── README.md
├── package.json
├── package-lock.json

```
### 🧰 Prerequisites

- Node.js (v16 or higher recommended)
- npm or yarn

### 🚀 Local Installation Steps


# 1. Clone the repository
```
git clone https://github.com/Akila-Nipo/Exam_Billing_System_JU_FRONTEND.git
cd Exam_Billing_System_JU_FRONTEND
```

# 2. Install dependencies
```
npm install
```

# 3. Run the React development server
```
npm start
```

### ✅ Access

- **Frontend**: [http://localhost:3000](http://localhost:3000)

> ⚠️ Make sure the Django backend is also running at [http://127.0.0.1:8000](http://127.0.0.1:8000) so that API calls work properly.

## 🛠 Technologies Used

### 🔙 Backend:
- Django (MVC architecture)
- SQLite
- HTML templates

### 🔜 Frontend:
- React
- Bootstrap
- HTML/CSS
- Axios (if API calls are used)

  ## 🖼️ Key Features

  <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx.png">
  </p>

    <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx%20(1).png">
  </p>

     <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx%20(2).png">
  </p>

     <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx%20(3).png">
  </p>

     <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx%20(4).png">
  </p>

     <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx%20(5).png">
  </p>

     <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx%20(6).png">
  </p>

     <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx%20(7).png">
  </p>

     <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx%20(8).png">
  </p>

     <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx%20(9).png">
  </p>

     <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx%20(10).png">
  </p>

     <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx%20(11).png">
  </p>
     <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx%20(12).png">
  </p>

     <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx%20(13).png">
  </p>
     <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx%20(14).png">
  </p>

     <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx%20(15).png">
  </p>

     <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx%20(16).png">
  </p>

     <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx%20(17).png">
  </p>

     <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx%20(18).png">
  </p>

     <p align="center">
   <img src="https://github.com/Akila-Nipo/django_temporary/blob/main/WEBLAB-Presentation(II).pptx%20(19).png">
  </p>
