# Dockerized 2-Tier Web Application with CI/CD

This project is a **Dockerized 2-tier web application** (Backend + Frontend) integrated with **GitHub Actions CI/CD** for automated build, push, and deployment to an **Azure Linux Virtual Machine**.

---

## Project Structure
dockerized-2tier-app/
│
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── frontend/
│ ├── index.html
│ ├── script.js
│ └── Dockerfile
│
├── .github/
│ └── workflows/
│ └── ci-cd.yml
│
├── screenshots/
│ ├── Backend_Build.jpg
│ ├── Frontend_Build.jpg
│ ├── Docker_Images.jpg
│ ├── DockerHub_Repo.jpg
│ ├── Containers_running.jpg
│ ├── Frontend_Connecting_to_Backend.jpg
│ ├── VM_Public_IP_Access.jpg
│ └── github_actions_success.jpg
│
├── docker-compose.yml
└── README.md


---

##  Setup and Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/sheyeoffic/dockerized-2tier-app.git
cd dockerized-2tier-app

Build and run using Docker Compose

docker compose up --build

This will:

Build both backend and frontend containers

Run them together on:

Backend → http://localhost:5000

Frontend → http://localhost:8080

 Backend Overview

Built with Python (Flask)

Exposes simple APIs:

/api/info → Project info

/api/quote → Random quote

/api/health → Status check

Dockerized with a lightweight python:3.9-slim base image.

 Frontend Overview

Simple HTML + JavaScript frontend

Fetches data from the backend APIs

Runs on Nginx web server in a separate container

 CI/CD Workflow Description

This project uses a GitHub Actions CI/CD pipeline that automatically builds, pushes, and deploys the Dockerized app.

Whenever changes are pushed to the main branch:

 The workflow builds Docker images for both backend and frontend.

 Pushes them to Docker Hub (emmanuelsheye/backend and emmanuelsheye/frontend).

 SSHs into the Azure VM.

 Pulls and redeploys the updated containers automatically.

This ensures continuous delivery and fast updates with minimal manual work.

 Screenshots
Description	Screenshot
Backend Build	

Frontend Build	

Docker Images List	

Docker Hub Repository	

Containers Running	

Frontend Connected to Backend	

Azure VM Public IP Access	

GitHub Actions CI/CD Success	

 Author

Emmanuel Faniseyi
GitHub: @sheyeoffic

Docker Hub: emmanuelsheye

 Final Notes

This project fulfills all requirements for the Azure Bootcamp Capstone Project.

It demonstrates containerization, orchestration, cloud deployment, and CI/CD automation.

The entire app can be redeployed with a single commit to main.


---

### After Copying:
1. Replace your current `README.md` content with the above.  
2. Save it.  
3. Then run in your terminal:
```bash
git add README.md
git commit -m "Updated README with structure and screenshots"
git push origin main



