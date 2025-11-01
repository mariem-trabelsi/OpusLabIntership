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



