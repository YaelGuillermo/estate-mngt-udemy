# 🏡 Real Estate Management System

### (Django + React Fullstack Project)

## 📌 Overview

This project is a full-stack real estate management web application built using Django (backend) and React (frontend). It allows users to browse, create, update, and manage property listings with interactive maps and authentication.

The system integrates modern technologies like Django REST Framework, GeoDjango, and React-Leaflet to deliver a scalable and feature-rich platform.

---

## 🚀 Features

### 🏘️ Property Listings

* Create, update, delete property listings
* Upload and display property images
* View listings in card and map formats

### 🗺️ Location-Based Search

* Interactive maps using Leaflet
* Display properties by geographic location
* Perform spatial queries (distance, area, etc.)

### 🔐 Authentication System

* User registration & login
* JWT-based authentication
* Secure API endpoints

### ⚙️ Backend (Django)

* Django REST Framework API
* Custom user model
* PostgreSQL + PostGIS (spatial database)
* Media handling and storage

### 🎨 Frontend (React)

* Modern UI with Material UI
* Axios for API requests
* React Hooks (useState, useEffect)
* Routing with React Router

### 🌐 Deployment

* Nginx + Gunicorn setup
* Production-ready configuration
* Cloud media storage

---

## 🛠️ Tech Stack

**Frontend:**

* React.js
* Material UI
* React-Leaflet

**Backend:**

* Django
* Django REST Framework
* GeoDjango

**Database:**

* PostgreSQL + PostGIS

**DevOps:**

* Nginx
* Gunicorn

---

## 📚 What You Will Learn

* Connecting React with Django APIs
* Building RESTful backend services
* Creating map-based applications
* Implementing authentication systems
* Deploying fullstack applications

---

## 📋 Requirements

* Basic knowledge of:

  * Python
  * JavaScript
  * HTML/CSS
* Familiarity with Django and React is helpful

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/real-estate-app.git
cd real-estate-app
```

### 2. Backend Setup (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the backend folder:

```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
```

### 4. Run Migrations

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Start Django Server

```bash
python manage.py runserver
```

### 6. Frontend Setup (React)

```bash
cd ../frontend
npm install
```

### 7. Start React App

```bash
npm start
```

---

## 📂 Project Structure

```
real-estate-app/
│
├── backend/
│   ├── api/
│   ├── users/
│   ├── listings/
│   └── manage.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

## 🎯 Use Cases

* Real estate platforms
* Property listing websites
* Location-based services
* Fullstack portfolio projects

---

## 🧠 Summary

This project demonstrates how to build a production-ready real estate management system using Django and React, combining backend APIs, frontend UI, and geolocation features into one scalable application.
