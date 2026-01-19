# Q3 

## What I Did

For this challenge I had to deploy **two completely different projects** using Docker containers:

1. **RoyalChess** – MERN stack (Next + Node + Mongo)  
2. **STAC Website** – Next.js + Django + PostgreSQL


I had never deployed  mixed stacks together, so this was a lot of learning + debugging 😅.

---

## Cloning Projects

I started by cloning both repositories:

git clone https://github.com/Sachitbansal/royalchess  
git clone https://github.com/Sachitbansal/stac-clone stac  

Then I analyzed:

- where frontend/backend are  
- which database each uses  
- build commands

---

## SContainerization

I created separate Dockerfiles:

- Dockerfile.client → RoyalChess frontend  
- Dockerfile.server → RoyalChess backend  
- Dockerfile.next → STAC frontend  
- Dockerfile.django → STAC backend

Databases were taken from official images:

- mongo:6  
- postgres:15

All services were combined using **docker-compose.yml**.

---

## Step 3 – Network Design

I used **two bridge networks**:

1. royal_net  
   - royal-client  
   - royal-server  
   - mongo

2. stac_net  
   - stac-next  
   - django  
   - postgres

i learnt a bit about docker do this design
- One project cannot talk to the other  
- Databases stay internal  
- Only frontend is exposed

security thingss
- 5432 (Postgres) → NOT published  
- 27017 (Mongo) → NOT published  
- Only:
  - 3000 → RoyalChess UI  
  - 4000 → STAC UI

---

## How to Run (Exact Steps)

### 1. Build everything

docker compose build

### 2. Start services

docker compose up -d

### 3. Verify containers

docker ps

### 4. Access websites

RoyalChess  
http://localhost:3000

STAC Website  
http://localhost:4000

---

## Verification 
- Checked all containers running  
- Verified databases NOT exposed  
- Tested both UIs in browser  
- Checked logs for errors

docker logs challenge3-django-1  
docker logs challenge3-royal-server-1  

---

## Problems 
1. STAC build failed  
   → missing `next-themes`  
   → fixed by installing in Dockerfile

2. Royal server crash  
   → `dist/server.js not found`  
   → rebuild and correct workdir

3. Django dependency hell  
   → added system packages in Dockerfile

time went in reading logs and fixing one line at a time 🥲.


