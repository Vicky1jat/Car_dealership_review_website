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

