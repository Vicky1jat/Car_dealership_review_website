# 🚗 Car Dealership Review Website

A full-stack web application for users to view, review, and rate car dealerships. The platform integrates a Django-based backend, a React frontend, and a Node.js microservice connected to MongoDB for dealer data.

## 📦 Project Structure

Car_dealership_review_website/
├── .github/ # GitHub configuration files
├── node_modules/ # Node dependencies
├── server/
│ ├── database/ # Node.js microservice for dealer data
│ ├── djangoapp/ # Django app with views, models, and microservice integration
│ ├── djangoproj/ # Django project settings and URLs
│ ├── frontend/ # React frontend for the website
│ ├── Dockerfile # Docker config for Django service
│ ├── deployment.yaml # Kubernetes deployment config
│ ├── manage.py # Django CLI
│ ├── requirements.txt # Python dependencies
├── package.json # Root-level Node.js metadata
├── .gitignore
└── README.md


---

## 🛠️ Features

- View dealerships by location
- Read and post reviews
- Login/register functionality
- Microservice-based backend (Node.js)
- Django handles authentication and APIs
- React frontend (responsive UI)
- MongoDB for dealership data
- Dockerized and Kubernetes-ready

---

## 🧰 Tech Stack

- **Frontend**: React.js, Tailwind CSS
- **Backend**: Django, Django REST Framework
- **Microservices**: Node.js + Express
- **Database**: MongoDB
- **DevOps**: Docker, Kubernetes (kubectl), Render/IBM Cloud (for deployment)
- **Others**: JWT Auth, Proxy APIs, Environment variables

---

## 🚀 Getting Started

### 1. Clone the Repository

    ```bash
      git clone https://github.com/yourusername/Car_dealership_review_website.git
      cd Car_dealership_review_website


### 2. Backend (Django)
    bash
    Copy code
    cd server
    python3 -m venv djangoenv
    source djangoenv/bin/activate
    pip install -r requirements.txt
    
    # Migrate database
    python manage.py makemigrations
    python manage.py migrate
    
    # Run server
    python manage.py runserver

###3. Node.js Microservice

      cd server/database
      npm install
      node app.js

       if containerized: 
        bash
        Copy code
        docker-compose up

### 4. Frontend (React)

      cd server/frontend
      npm install
      npm start


🐳 Docker (Alternative)

     To run everything in containers:
   
      # From project root
      docker build -t dealership-app .
      docker run -p 8000:8000 dealership-app


💡 Acknowledgments
      
      IBM Full Stack Software Developer Capstone

### 🖼 UI Preview

| Hero | Editor & Interaction | Footer |
|------|----------------------|--------|
| ![Hero](asset/hero.png.png) | ![Editor](asset/middle.png.png) | ![Footer](asset/footer.png.png) |
