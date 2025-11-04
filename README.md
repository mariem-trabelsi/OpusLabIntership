# Application d'Affichage d'Articles de Recherche en IA

Une application Flask conteneurisée pour gérer et afficher des articles de recherche en IA avec un pipeline CI/CD complet et infrastructure as code.

## 📋 Table des matières
- [Vue d'ensemble](#vue-densemble)
- [Décisions d'architecture](#décisions-darchitecture)
- [Prérequis](#prérequis)
- [Démarrage rapide](#démarrage-rapide)
- [Options de déploiement](#options-de-déploiement)
- [Pipeline CI/CD](#pipeline-cicd)
- [Démonstration](#démonstration)

## 🎯 Vue d'ensemble

Application web simple qui permet aux utilisateurs de :
- Parcourir les articles de recherche en IA
- Rechercher par titre ou auteur
- Trier par année de publication
- Ajouter de nouveaux articles à la collection

**Stack technologique :** Flask, Python 3.12, Docker, Kubernetes, GitHub Actions

## 📁 Structure du projet

```
paper-display-app/
├── app.py                      # Application Flask
├── requirements.txt            # Dépendances Python
├── Dockerfile                  # Build Docker multi-étapes
├── docker-compose.yml          # Développement local
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Pipeline GitHub Actions
├── k8s/
│   ├── deployment.yaml        # Déploiement Kubernetes
│   └── service.yaml           # Service Kubernetes
├── templates/
│   └── index.html             # Template Flask
└── README.md                  # Ce fichier
```

## 🏗️ Décisions d'architecture

### 1. **Dockerfile multi-étapes**
- **Étape 1 (Builder) :** Installation des dépendances de manière isolée
- **Étape 2 (Runtime) :** Copie uniquement des artefacts nécessaires
- **Avantages :** 
  - Réduction de la taille de l'image finale (~150MB vs ~900MB)
  - Sécurité améliorée (pas d'outils de build en production)
  - Temps de déploiement plus rapides

### 2. **Choix d'orchestration : Kubernetes**
- Kubernetes sélectionné plutôt que Docker Swarm pour :
  - Meilleur support de la communauté et écosystème
  - Capacités de scaling avancées
  - Intégrations cloud-native
  - Fonctionnalités de production (health checks, rolling updates)

### 3. **Pipeline CI/CD**
- **Déclencheurs :** Push sur la branche main
- **Étapes :**
  1. Linting du code (flake8)
  2. Build de l'image Docker
  3. Push vers Docker Hub
- **Sécurité :** Utilise les GitHub Secrets pour les identifiants

## 📦 Prérequis

- Docker 20.10+
- Docker Compose 2.0+
- kubectl 1.28+ (pour Kubernetes)
- Compte GitHub
- Compte Docker Hub

## 🚀 Démarrage rapide

### Exécution locale avec Docker

```bash
# Construire l'image
docker build -t paper-display-app .

# Lancer le conteneur
docker run -p 5000:5000 paper-display-app
```

Accédez à l'application sur `http://localhost:5000`

## 📊 Démonstration

### Construction et exécution de l'image de l'application

```bash
docker build -t paper-display-app .
docker run -p 5000:5000 paper-display-app
```

![Construction Docker](https://github.com/user-attachments/assets/0c95818b-ad98-43b6-8fe5-8d1b18fbbc27)

![Application en cours d'exécution](https://github.com/user-attachments/assets/16c7e1f5-5647-46b1-9366-60a84ff65e4b)



### Création du pipeline CI/CD

![Configuration du pipeline](https://github.com/user-attachments/assets/61367d4c-60d0-477d-bffc-496d2057a572)

**Échec initial dans le pipeline :** Problème d'accès au Docker Hub

![Erreur pipeline](https://github.com/user-attachments/assets/d98f3550-0b0c-4d46-8d80-fcb45d8d3ecb)

### Configuration des identifiants Docker Hub dans le dépôt GitHub

![Secrets GitHub](https://github.com/user-attachments/assets/8677bbb7-3d36-460a-90a9-c7b837f5a13d)

![Configuration des secrets](https://github.com/user-attachments/assets/ffeb63f0-e0fa-4b21-b84d-7aa0d816ca41)

![Détails de l'erreur](https://github.com/user-attachments/assets/6ec11485-3c26-45a8-9b34-1ff3734c117c)

### Résolution et succès du pipeline

![Pipeline corrigé](https://github.com/user-attachments/assets/afda63a7-3d42-4310-b702-89e928392f15)

### Vérification de l'image dans Docker Hub

![Pipeline réussi](https://github.com/user-attachments/assets/1febc4bc-4388-45fe-acbf-37e17a9fd9bf)

![Logs de build](https://github.com/user-attachments/assets/925d529f-cdd2-4b2a-866d-4ef515fa1e55)

![Étapes de déploiement](https://github.com/user-attachments/assets/921cbdf2-8fa9-416a-b4fd-5d42320495f7)

### Image Docker publiée sur Docker Hub

![Image Docker Hub](https://github.com/user-attachments/assets/9ec2ec1a-2a25-460a-80cb-48bed40733f1)

### Déploiement Kubernetes

![Déploiement K8s](https://github.com/user-attachments/assets/3d806d5b-a91b-4645-b1cd-0a46970f9bda)

![Services et Pods](https://github.com/user-attachments/assets/92cf7f5e-a800-4208-bcb4-3ecca9ded96a)

![Vérification des pods](https://github.com/user-attachments/assets/503daa6c-ca68-4d57-b86a-563cdb1175cc)

### Application déployée

![Application finale](https://github.com/user-attachments/assets/075e6eda-b2fb-45d7-ad29-80602c80b24e)

## 🔄 Options de déploiement

### Avec Docker Compose

```bash
docker-compose up -d
```

### Avec Kubernetes

```bash
# Appliquer les manifests
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Vérifier le déploiement
kubectl get pods
kubectl get services
```

## 🔐 Configuration du pipeline CI/CD

1. **Fork le dépôt**
2. **Configurer les secrets GitHub :**
   - `DOCKER_USERNAME` : Votre nom d'utilisateur Docker Hub
   - `DOCKER_PASSWORD` : Votre token d'accès Docker Hub
3. **Push vers la branche main** pour déclencher le pipeline

