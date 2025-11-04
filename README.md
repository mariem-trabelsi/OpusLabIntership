# AI Research Papers Display App

A containerized Flask application for managing and displaying AI research papers with full CI/CD pipeline and infrastructure as code.

## 📋 Table of Contents
- [Overview](#overview)
- [Architecture Decisions](#architecture-decisions)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Deployment Options](#deployment-options)
- [CI/CD Pipeline](#cicd-pipeline)

## 🎯 Overview

Simple web application that allows users to:
- Browse AI research papers
- Search by title or author
- Sort by publication year
- Add new papers to the collection

**Tech Stack:** Flask, Python 3.12, Docker, Kubernetes, GitHub Actions

## 📁 Project Structure

```
paper-display-app/
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Multi-stage Docker build
├── docker-compose.yml          # Local development
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions pipeline
├── k8s/
│   ├── deployment.yaml        # Kubernetes deployment
│   └── service.yaml           # Kubernetes service
├── templates/
│   └── index.html             # Flask template
└── README.md                  # This file
```

## 🏗️ Architecture Decisions

### 1. **Multi-Stage Dockerfile**
- **Stage 1 (Builder):** Installs dependencies in isolation
- **Stage 2 (Runtime):** Copies only necessary artifacts
- **Benefits:** 
  - Reduced final image size (~150MB vs ~900MB)
  - Improved security (no build tools in production)
  - Faster deployment times

### 2. **Orchestration Choice: Kubernetes**
- Selected Kubernetes over Docker Swarm for:
  - Better community support and ecosystem
  - Advanced scaling capabilities
  - Cloud-native integrations
  - Production-grade features (health checks, rolling updates)

### 3. **CI/CD Pipeline**
- **Triggers:** Push to main branch
- **Stages:**
  1. Code linting (flake8)
  2. Docker image build
  3. Push to Docker Hub
- **Security:** Uses GitHub Secrets for credentials

## 📦 Prerequisites

- Docker 20.10+
- Docker Compose 2.0+
- kubectl 1.28+ (for Kubernetes)
- GitHub account
- Docker Hub account
## Démo

### l'image de l'application :
<img width="1291" height="181" alt="cap1" src="https://github.com/user-attachments/assets/0c95818b-ad98-43b6-8fe5-8d1b18fbbc27" />

<img width="1655" height="819" alt="cap2" src="https://github.com/user-attachments/assets/16c7e1f5-5647-46b1-9366-60a84ff65e4b" />
### création de dockerhub credentials dans le repo github
<img width="683" height="278" alt="cap7" src="https://github.com/user-attachments/assets/8677bbb7-3d36-460a-90a9-c7b837f5a13d" />

<img width="853" height="671" alt="cap3" src="https://github.com/user-attachments/assets/ffeb63f0-e0fa-4b21-b84d-7aa0d816ca41" />
### création du pipeline ci-cd qui 
<img width="902" height="727" alt="cap4" src="https://github.com/user-attachments/assets/61367d4c-60d0-477d-bffc-496d2057a572" />
Echec dans le pipeline: problème d'accès au Dockerhub.
<img width="1255" height="780" alt="cap5" src="https://github.com/user-attachments/assets/d98f3550-0b0c-4d46-8d80-fcb45d8d3ecb" />

<img width="805" height="441" alt="cap6" src="https://github.com/user-attachments/assets/6ec11485-3c26-45a8-9b34-1ff3734c117c" />



<img width="1164" height="422" alt="cap8" src="https://github.com/user-attachments/assets/afda63a7-3d42-4310-b702-89e928392f15" />

<img width="1257" height="595" alt="cap9" src="https://github.com/user-attachments/assets/1febc4bc-4388-45fe-acbf-37e17a9fd9bf" />

<img width="796" height="133" alt="cap10" src="https://github.com/user-attachments/assets/925d529f-cdd2-4b2a-866d-4ef515fa1e55" />

<img width="767" height="194" alt="cap11" src="https://github.com/user-attachments/assets/921cbdf2-8fa9-416a-b4fd-5d42320495f7" />

<img width="1409" height="194" alt="cap12" src="https://github.com/user-attachments/assets/9ec2ec1a-2a25-460a-80cb-48bed40733f1" />

<img width="1835" height="660" alt="cap13" src="https://github.com/user-attachments/assets/3d806d5b-a91b-4645-b1cd-0a46970f9bda" />

<img width="1065" height="499" alt="cap14" src="https://github.com/user-attachments/assets/92cf7f5e-a800-4208-bcb4-3ecca9ded96a" />

<img width="883" height="228" alt="cap15" src="https://github.com/user-attachments/assets/503daa6c-ca68-4d57-b86a-563cdb1175cc" />

<img width="1835" height="933" alt="cap16" src="https://github.com/user-attachments/assets/075e6eda-b2fb-45d7-ad29-80602c80b24e" />

