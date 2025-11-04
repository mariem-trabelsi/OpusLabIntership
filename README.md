# Application d'Affichage d'Articles de Recherche en IA

Une application Flask conteneurisée pour gérer et afficher des articles de recherche en IA avec un pipeline CI/CD complet et infrastructure as code.

## 📋 Table des matières
- [Vue d'ensemble](#vue-densemble)
- [Décisions d'architecture](#décisions-darchitecture)
- [Prérequis](#prérequis)
- [Démarrage rapide](#démarrage-rapide)
- [Options de déploiement](#options-de-déploiement)
- [Pipeline CI/CD](#pipeline-cicd)
- [Monitoring avec Prometheus & Grafana](#monitoring-avec-prometheus--grafana)
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
  - Réduction de la taille de l'image finale
  - Sécurité améliorée (pas d'outils de build en production)
  - Temps de déploiement plus rapides

### 2. **Choix d'orchestration : Kubernetes**
- Kubernetes sélectionné plutôt que Docker Swarm pour :
  - Meilleur support de la communauté et écosystème
  - Capacités de scaling avancées
  - Intégrations cloud-native
  - Fonctionnalités de production (health checks, rolling updates)

### 3. **Pipeline CI/CD (Github Actions)** 
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


<img width="1711" height="673" alt="image" src="https://github.com/user-attachments/assets/5c2b225a-75b7-4bb6-a229-7c10607a9fd5" />



### Création du pipeline CI/CD

![Configuration du pipeline](https://github.com/user-attachments/assets/61367d4c-60d0-477d-bffc-496d2057a572)

**Échec initial dans le pipeline :** Problème d'accès au Docker Hub

![Erreur pipeline](https://github.com/user-attachments/assets/d98f3550-0b0c-4d46-8d80-fcb45d8d3ecb)

### Configuration des identifiants Docker Hub dans le dépôt GitHub

![Secrets GitHub](https://github.com/user-attachments/assets/8677bbb7-3d36-460a-90a9-c7b837f5a13d)

![Détails de l'erreur](https://github.com/user-attachments/assets/6ec11485-3c26-45a8-9b34-1ff3734c117c)

![Configuration des secrets](https://github.com/user-attachments/assets/ffeb63f0-e0fa-4b21-b84d-7aa0d816ca41)



### Résolution et succès du pipeline

![Pipeline corrigé](https://github.com/user-attachments/assets/afda63a7-3d42-4310-b702-89e928392f15)

### Image Docker publiée sur Docker Hub

![Pipeline réussi](https://github.com/user-attachments/assets/1febc4bc-4388-45fe-acbf-37e17a9fd9bf)

### Push vers main

![Services et Pods](https://github.com/user-attachments/assets/92cf7f5e-a800-4208-bcb4-3ecca9ded96a)

### Kubernetes (k8s) – Local avec Minikube

**Installation**
```bash
# Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install kubectl /usr/local/bin/kubectl
```
**Déploiement**
```bash
minikube start
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
minikube service paper-display-service --url
```

![Logs de build](https://github.com/user-attachments/assets/925d529f-cdd2-4b2a-866d-4ef515fa1e55)

![Étapes de déploiement](https://github.com/user-attachments/assets/921cbdf2-8fa9-416a-b4fd-5d42320495f7)



![Image Docker Hub](https://github.com/user-attachments/assets/9ec2ec1a-2a25-460a-80cb-48bed40733f1)

### Application déployée sur K8S

<img width="874" height="112" alt="lance" src="https://github.com/user-attachments/assets/21737dec-1fbe-4a35-9fb0-6ef21c2370bb" />


![Déploiement K8s](https://github.com/user-attachments/assets/3d806d5b-a91b-4645-b1cd-0a46970f9bda)

### Monitoring Kubernetes (Minikube) avec Prometheus + Grafana
#### 1.Prérequis
```bash
# Minikube
minikube start

# kubectl
kubectl version --short

# Helm
helm version --short
```
#### 2.Installer PROMETHEUS + GRAFANA (Monitoring Stack)
```bash
# Ajouter le repo Helm
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

# Créer namespace
kubectl create namespace monitoring

# Installer la stack complète
helm install prometheus-stack prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --set grafana.adminPassword=admin123 \
  --set prometheus.prometheusSpec.serviceMonitorSelectorNilUsesHelmValues=true
```

#### 3. Accéder à Grafana
```bash
kubectl port-forward svc/prometheus-stack-grafana 3000:80 -n monitoring
```

#### 4. Configurer le Data Source (Prometheus)
```bash
PROM_IP=$(kubectl get svc -n monitoring prometheus-stack-kube-prom-prometheus -o jsonpath='{.spec.clusterIP}')
echo "URL Prometheus : http://$PROM_IP:9090"
```

#### 5. Configurer le Data Source (Prometheus)
Import de dashboard Pods (15760)

#### 6. Configurer le Data Source (Prometheus)
Voir les métriques de paper-display
**namespace**: default
**pod**: paper-display-...

![Vérification des pods](https://github.com/user-attachments/assets/503daa6c-ca68-4d57-b86a-563cdb1175cc)


<img width="1150" height="154" alt="garafna" src="https://github.com/user-attachments/assets/033e7d76-9b52-4ddd-b048-d195e562ca60" />

<img width="1521" height="862" alt="image" src="https://github.com/user-attachments/assets/52c98c33-cce2-47ce-afa0-7b642837d9c9" />



---

## Perspectives : Évolutions futures

L'application est déjà **production-ready** avec CI/CD, Kubernetes et monitoring complet. Voici les **prochaines étapes d'amélioration** :

| Fonctionnalité | Description | Impact |
|----------------|-----------|--------|
| **Logs centralisés avec Loki** | Intégrer **Loki + Promtail** pour collecter, stocker et visualiser les logs Flask dans Grafana. | Debugging en temps réel, corrélation logs/métriques |
| **Alerting intelligent** | Configurer **Prometheus Alertmanager** → alertes Slack/Email en cas de CPU > 80%, pod crash, etc. | Réactivité opérationnelle 24/7 |
| **Métriques applicatives custom** | Ajouter un endpoint `/metrics` dans Flask (via `prometheus_client`) → exposer : requêtes/s, latence, erreurs 500 | Observabilité métier complète |
| **Déploiement Cloud (Azure AKS)** | Migrer de Minikube vers **Azure Kubernetes Service (AKS)** + **Azure Container Registry** | Scalabilité horizontale, haute disponibilité, coûts optimisés |

> **Objectif final** : Un **observability stack complet** (métriques + logs + traces) sur **Azure Cloud**, avec **alerting proactif** et **métriques business**.

---

**Tu as posé les bases d’un système moderne, scalable et observable — prêt pour la production !**
