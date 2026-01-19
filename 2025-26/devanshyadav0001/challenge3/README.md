# Challenge 3 – Docker Deployment

## 📌 Overview

This challenge focuses on deploying two full-stack web applications using Docker and Docker Compose, configuring internal networking, and ensuring database security by preventing host exposure.

### Projects Deployed
- **RoyalChess** – MERN Stack (React + Node.js + MongoDB)
- **STAC Website Clone** – Next.js Frontend + Django Backend + PostgreSQL

---

## 🎯 Objectives

- Containerize both projects  
- Run both stacks simultaneously using Docker Compose  
- Configure an internal Docker network  
- Ensure databases are not exposed to the host  
- Document full deployment process and issues faced  

---

## 📂 Folder Structure

challenge3
│
├── royalchess
│ ├── client → React frontend
│ └── server → Node backend (TypeScript + WebSockets)
│
├── stac-clone
│ ├── frontend → Next.js frontend
│ └── backend → Django backend
│
└── docker-compose.yml



---

## ⚙️ Dockerized Services

### RoyalChess Stack
- royal_db → MongoDB  
- royal_backend → Node.js backend  
- royal_frontend → React frontend  

### STAC Stack
- stac_db → PostgreSQL  
- stac_backend → Django backend  
- stac_frontend → Next.js frontend  

### Network
- Custom internal bridge network  
`challenge3_internal_net`

---

## 🔐 Security Implementation

- Databases have no host-exposed ports  
- Only backend services connect to databases internally  
- Databases inaccessible from host or external environment  

✅ Security objective successfully achieved

---

## 🚀 Deployment Steps

1. Repository inspection  
2. Dockerfile creation for all services  
3. Docker Compose configuration  
4. Build & deploy using:

```bash
docker compose up -d --build
