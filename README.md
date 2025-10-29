# Dockerized 2-Tier Web Application  
### Author: Emmanuel Sheye

---

## Overview
This project demonstrates a **Dockerized 2-Tier Web Application** consisting of:
- A **Flask Backend API** serving dynamic data.
- A **Frontend Web App** built with HTML, CSS, and JavaScript served via Nginx.
- A **docker-compose.yml** configuration that runs both containers together seamlessly.

The project was developed as part of the **Azure Cloud Bootcamp**, to showcase containerization, multi-tier architecture, and deployment readiness.

---

## Project Structure

dockerized-2tier-app/
├── backend/
│ ├── app.py
│ ├── Dockerfile
│ ├── requirements.txt
├── frontend/
│ ├── index.html
│ ├── Dockerfile
├── docker-compose.yml
└── README.md


---

## Backend Service (Flask API)
The backend is a Python Flask API with three endpoints:
| Endpoint | Description |
|-----------|--------------|
| `/api/info` | Returns basic app information |
| `/api/quote` | Returns a random quote |
| `/api/health` | Returns a simple health status |

**Run locally:**
```bash
cd backend
python app.py

# Frontend Service

The frontend is a simple HTML/JS interface that fetches data from the Flask backend and displays it in a user-friendly format.

Run locally:
Open frontend/index.html in your browser or serve it via Nginx.

Docker Setup
Build Images

docker build -t backend ./backend
docker build -t frontend ./frontend

Run with Docker Compose
docker compose up --build

Access the app:

Backend → http://localhost:5000/api/info

Frontend → http://localhost:8080

Screenshots

Screenshots demonstrating successful build, Docker Compose run, and application behavior are included in the project submission folder.

Docker Hub Repositories

The Docker images for this 2-Tier Web Application are publicly available on Docker Hub.

Backend (Flask API)
emmanuelsheye/backend:v1

Frontend (Nginx + HTML)
emmanuelsheye/frontend:v1

Pull and Run the Backend Images

docker pull emmanuelsheye/backend:v1
docker run -p 5000:5000 emmanuelsheye/backend:v1

Visit:

http://localhost:5000/api/info

http://localhost:5000/api/quote

http://localhost:5000/api/health

Frontend

Pull and run the frontend image:

docker pull emmanuelsheye/frontend:v1
docker run -p 8080:80 emmanuelsheye/frontend:v1

Open your browser:
http://localhost:8080

## 🐳 Docker Hub Repositories

The following Docker images were built and pushed as part of this project:

### 🔹 Backend
- **Repository:** [emmanuelsheye/backend](https://hub.docker.com/r/emmanuelsheye/backend)
- **Tags:**  
  - `latest` — latest local build  
  - `v1` — version submitted for review  
- **Pull Command:**
  ```bash
  docker pull emmanuelsheye/backend:v1

Frontend

Repository: emmanuelsheye/frontend

Tags:

latest — latest local build

v1 — version submitted for review

Pull Command: docker pull emmanuelsheye/frontend:v1

## Deployment Instructions
...

##  CI/CD Workflow

This project uses a GitHub Actions CI/CD pipeline to automate the build and deployment process. Whenever a change is pushed to the main branch, the workflow automatically builds the Docker images for both the backend and frontend, tags them with version numbers, and pushes them to Docker Hub. It then securely connects to the Azure Linux VM via SSH to pull and run the updated containers. This ensures continuous delivery of the latest version of the application with minimal manual intervention.

## Author
Emmanuel Sheye


# Summary

This project demonstrates containerization of a 2-tier web app using Docker.
It highlights the use of:

Flask backend API

Nginx web server frontend

Docker Compose for orchestration

Docker Hub for image hosting

Author

Emmanuel Sheye
Azure Cloud Bootcamp Participant
Dockerized 2-Tier Web Application Project
