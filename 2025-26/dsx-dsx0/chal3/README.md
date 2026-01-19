# Docker Deployment  
RoyalChess & STAC

---

## 1. Overview

This document records the complete technical process undertaken during the containerization and deployment challenges. The scope includes:

- A fully working Docker-based deployment of RoyalChess
- A partially completed Docker deployment of STAC, with all technical issues documented
- due to this reason, both the applications have a different docker-compose.yml file

All meaningful steps, decisions, errors, and fixes are recorded as they occurred.

---

## 2. RoyalChess Deployment

---

## 2.1 Objective

The objective was to deploy the RoyalChess application using Docker in a way that allows:

- Correct session handling
- Stable runtime behavior across container restarts

---

## 2.2 Architecture

RoyalChess was deployed using Docker Compose with the following services:

- Application service (Node.js)
- Database service (PostgreSQL)
- Docker-managed internal network

Services communicate using Docker service names rather than localhost or hardcoded IPs.

---
## Security Considerations (Service Connections)

- The frontend communicates with the backend exclusively over defined HTTP APIs, with no direct access to the database or internal services.
- All database connections are restricted to the backend service and isolated within the Docker network, preventing external access.
- Inter-service communication relies on Docker’s internal bridge network, avoiding unnecessary port exposure to the host system.
- Environment variables are used to configure service connections, ensuring credentials and endpoints are not hardcoded into the application.


## 2.3 Configuration and Setup

### 2.3.1 Environment Variables

All configuration values were provided through environment variables, including:

- Application port
- Database connection details
- Session secret
- Runtime environment mode

---

### 2.3.2 Session and Cookie Handling Issue

#### Problem Observed

After containerizing the application, authentication sessions were not persisting correctly. Users were being logged out unexpectedly, and cookies were not behaving consistently across requests.

#### Root Cause

The issue was traced to session configuration in a containerized environment:

- A missing or unstable session secret caused cookies to be invalidated on container restarts
- Cookie behavior differed when running behind Docker networking compared to local development

#### Fix Applied

- A fixed, explicit SESSION_SECRET value was provided via environment variables
- The secret was made sufficiently long and constant to ensure session signing remained consistent
- Cookie behavior stabilized once the session secret was no longer regenerated implicitly

format used:
SESSION_SECRET=9f3c2b4e7a8d1c6f0a2e5b9d7c4a8f1e6b3d9c2a5e7f8b4c6d0a1e9

After this change:
- Sessions persisted correctly
- Cookies remained valid across restarts
- Authentication behavior became consistent

---

### 2.3.3 Docker Compose Orchestration

Docker Compose was used to:

- Start all services together
- Ensure the application waits for database availability
- Provide a single entry point for build and runtime

Command used:
docker compose up --build

---

### 2.3.4 Port Exposure

Only required ports were exposed to the host. Internal communication between services remained container-scoped.

---

## 2.4 Result

- Images built successfully
- Containers started without runtime errors
- Application was accessible from the host
- Session handling worked correctly after fixes

Status: Successful

---

## 2.5 Possible Improvements

The following are reasonable next steps if the project were to be extended further:

1. Health checks for service readiness   
2. Externalized secrets management  
3. Structured logging instead of console output  

---

## 3. STAC Deployment Attempt

---

## 3.1 Initial Environment

- Host OS: Linux
- CPU Architecture: AMD
- Backend Framework: Django
- Python Version (container): 3.11
- Orchestration: Docker Compose

Project structure (simplified):

stac/
├── app/
│   ├── backend/
│   │   ├── manage.py
│   │   ├── settings.py
│   │   ├── requirements.txt
│   │   └── ...
│   ├── frontend/
│   └── ...
├── docker-compose.yml
└── Dockerfile

---

## 3.2 Initial Build Attempt

Command executed:
docker compose up --build

Result:
- Frontend image built successfully
- Backend image failed during dependency installation

---

## 3.3 Dependency Issues Encountered

### 3.3.1 tensorflow_intel Package

Problem  
The backend requirements included tensorflow_intel, which is platform-specific and unsuitable for the current environment.

Fix Applied  
tensorflow_intel was removed and tensorflow was retained.

---

### 3.3.2 PyTorch CPU Build Resolution

Problem  
torch==2.6.0+cpu could not be resolved using default PyPI sources.

Fix Applied  
The requirement was changed to torch==2.6.0.

---

### 3.3.3 NumPy Version Conflicts

Problem  
numpy==2.1.1 conflicted with multiple scientific and ML libraries. TensorFlow required numpy < 2.1.0.

Fix Applied  
NumPy was downgraded to a compatible version.

---

## 3.4 Build Outcome After Fixes

After applying the above changes, Docker images built successfully and docker compose up completed without build-time errors.

---

## 3.5 Runtime Failure

When starting the backend container, the following error occurred:

ModuleNotFoundError: No module named 'corsheaders'

---

### Root Cause

- corsheaders was included in INSTALLED_APPS
- django-cors-headers was missing from requirements.txt

---

### Intended Fix (Not Executed)

Add the missing dependency to requirements.txt and rebuild containers.

---

## 3.6 Environment Variable Warning

Warning observed:
.env file not found at /app/.env

This indicated that environment variables were being sourced from the container environment rather than a file. This was not a blocking issue.

---

## 4. Final Status Summary

Completed:
- RoyalChess Docker deployment with stable session handling
- Docker Compose orchestration
- Resolution of multiple dependency conflicts in STAC

Not Completed:
- Final runtime startup of STAC backend due to a missing Django dependency

---

## 5. Conclusion

Although the STAC application did not fully start, involved dependency conflicts, platform-specific issues, and container configuration problems. 

