# Challenge 3: Multi-Project Docker Deployment Report

**January 18, 2026**

---

## 1 Introduction

So for this project, again, I didn’t know how to create a Dockerfile and that docker-
compose.yml, so I saw that on YouTube and tried to build it. But of course, there were
some issues, so then I gave my code to Gemini to check it, and there I had to change the
code a lot of times to get it working. This project required deploying two full-stack applica-
tions (RoyalChess and STAC) simultaneously on different containers with production-grade
security.

---

## 2 Containerization Strategy

To deploy the two full-stack applications, I created custom Dockerfiles optimized for stability
and security.

### 2.1 Frontend Containerization

• RoyalChess (MERN): I utilized a multi-stage Node.js build. Since the project uses
pnpm, I configured the Dockerfile to enable corepack and used the –filter client flag to
strictly isolate the frontend build process from the backend logic.

• STAC (Next.js): I used a standard Node.js image to serve the application on port 3001.

### 2.2 Backend Containerization

The biggest challenge was in the STAC Backend Dockerfile (stac-clone/backend/Dockerfile)
where Python was used. I at first used Python 3.13, but then when I tried to create the
docker image, it gave an error. That was because there was a tensorflow version that needed
to be installed, and I have a history with tensorflow as the latest version of tensorflow doesnt
let gpu to work with the latest py we have to degrade the py version to 3.10. Therefore, I
knew that py 3.10 has to be used here. So, I had to degrade the py version to 3.10 to ensure
compatibility.

---

## 3 Network Architecture & Security

For the networking, I created custom bridge networks. I set internal=true in the database
and backend connection to satisfy the security condition imposed by the test.

### 3.1 Network Type Selection

I utilized User-Defined Bridge Networks for all containers.

• Justification: The bridge driver is the standard for containers running on a single host.
It allows for automatic DNS resolution between containers by name (e.g., royal-backend
can ping royal-db) while providing isolation from the host network. Host networking
was rejected as it removes network isolation, and Overlay was unnecessary for this
single-host deployment.

### 3.2 Network Segmentation

To adhere to the requirement that databases must not be accessible from outside, I imple-
mented a segmented network architecture:

• Public Networks (royal public net, stac public net): Connect the Frontends to their
respective Backends.

• Internal Networks (royal internal net, stac internal net): Connect the Backends to
their respective Databases.

---

## 4 Hosting & Security Implementation

Then for the docker-compose.yml, I created the database, frontend, and backend services
for each project, and I have learnt a lot about how all of these interact and what the code
means.

I passed the database connection string into the backend’s environment variables to tell it
to ask from the database at first. I did the same thing to the frontend; I passed the backend
and I also stored the database in a file in my PC using Docker Volumes. Since the containers
are temporary, they would otherwise forget the database every time they restarted.

I implemented the following measures to satisfy the “Production Grade” requirements:

• Host Isolation: The database services do not have a ports section. This guarantees
that port 5432 and 27017 are not exposed to the host machine (localhost), making
them invisible to the host.

• Service Separation: The frontend containers are not attached to the internal networks,
preventing any direct access from the web client to the database.

---

## 5 Troubleshooting & Methodology

To resolve build failures, I adopted a hybrid debugging strategy, utilizing Gemini to diagnose
low-level system errors while applying my own experience to resolve library conflicts.

### 5.1 Dependency Management (Resolved via Personal Experience)

The build failed with a ResolutionImpossible error between numpy==2.1.1 and tensorflow.
Drawing on my past experience with Python library conflicts, I recognized this as a classic
“Dependency Hell” scenario where pinned versions were strictly conflicting. I manually
relaxed the constraints by unpinning the numpy version in requirements.txt, allowing pip to
automatically resolve a version (e.g., 2.0.x) that satisfied all constraints.

### 5.2 System & Platform Issues (Resolved via Gemini Consultation)

I faced opaque errors regarding UnicodeDecodeError and missing packages like tensorflow-
intel and torch+cpu. Gemini identified that the provided requirements.txt was likely gen-
erated on a Windows environment (using UTF-16 encoding and Windows-specific binaries),
which caused the Linux-based Docker container to fail. Following Gemini’s guidance, I con-
verted the file encoding to UTF-8 and sanitized the requirements list to remove Windows-
specific tags.

---

## Table of Contents

- Introduction
- Containerization Strategy
- Frontend Containerization
- Backend Containerization
- Network Architecture & Security
- Network Type Selection
- Network Segmentation
- Hosting & Security Implementation
- Troubleshooting & Methodology
- Dependency Management (Resolved via Personal Experience)
- System & Platform Issues (Resolved via Gemini Consultation)
