# Challenge 3 – Web Application Deployment & Analysis (STAC + RoyalChess)

  

> **Status:** Partial completion with detailed technical analysis  
> **Environment:** Windows 11 + WSL (Ubuntu) + Docker Desktop  
> **User Skill Level Assumed:** Beginner (all steps explicit)

  

---

  

## Overview

Challenge 3 involved two independent full‑stack web applications:

1. **STAC Website** (Docker-based, Django + Next.js + PostgreSQL)
2. **RoyalChess Website** (Monorepo using PNPM, Next.js frontend, Node backend)

The goal was to **build, run, and analyze** these applications locally and document the process, including failures.
---

  

# Part A – STAC Website

## Files Provided

- `stac-clone-main.zip`
- Backend: Django (Python)
- Frontend: Next.js
- Database: PostgreSQL
- Orchestration: Docker Compose
---
## Step 1 – Environment Verification (Screenshot 1)

Commands:

```bash

docker --version

docker compose version

```

✔ Docker Desktop was running  
✔ WSL integration enabled  

---

## Step 2 – Project Structure Inspection (Screenshot 2)

  
```bash

cd Challenge3/stac

ls

```

  

Observed:

- `backend/`
- `frontend/`
- `docker-compose.yml`  
---

## Step 3 – Docker Compose Build Attempt (Screenshot 3)

  

```bash

docker compose up -d --build
```

  

### Result

- Frontend image started building
- Backend build **failed** during:
```text

RUN pip install --no-cache-dir -r requirements.txt

```

  

### Root Cause
- `requirements.txt` contained:
  - `tensorflow==2.18.0`
  - `tensorflow_intel==2.18.0`
- These **do not support Python 3.11**
- Dockerfile originally used:

```dockerfile

FROM python:3.11-slim

```


---
## Step 4 – Python Version Downgrade Attempt (Screenshot 4)

  

Modified backend Dockerfile:

```dockerfile

FROM python:3.10-slim

```

  

Rebuild:

```bash

docker compose build --no-cache

```

  

### Result

- TensorFlow wheel downloaded
- Build stalled >10 minutes
- Eventually failed again at `pip install`

### Conclusion (STAC)
- Backend dependency set is **extremely heavy**
- Build failure is due to:
  - TensorFlow CPU wheels
  - Resource constraints
  - Poor dependency pinning
❌ STAC could not be fully deployed  
✔ Root cause identified and documented

---

# Part B – RoyalChess Website
  
## Files Provided

- `royalchess-main.zip`
- Monorepo using `pnpm`
- Frontend: Next.js
- Backend: Node/TypeScript

---
## Step 1 – Node & PNPM Setup (Screenshot 5)

```bash

node -v

npm -v

sudo npm install -g pnpm

pnpm -v

```

  

✔ Node v20  

✔ PNPM installed correctly  


---


## Step 2 – Install Dependencies 
```bash

cd Challenge3/royalchess

pnpm install

```

  
Result:
- All workspace dependencies installed
- No fatal errors
  
---
## Step 3 – Client Build (Screenshot 7)

```bash

pnpm --filter client build

```
### Output

- Next.js production build succeeded
- Static routes generated
- `.next/` directory created

  

✔ Frontend build successful

  

---

  

## Step 4 – Backend Status

  
- Backend code present
- No production `start` script
- No database configuration
- No Docker or runtime instructions


❌ Backend could not be executed meaningfully

---
## RoyalChess Conclusion

  

✔ Frontend builds successfully  
✖ Backend incomplete / not runnable  
✖ Full application deployment not possible

---
# Final Summary

  

| Application | Status | Notes |

| STAC | ❌ Failed | Python/TensorFlow dependency conflict |

| RoyalChess | ⚠ Partial | Frontend works, backend incomplete |

  

---

  

## What Was Achieved

  

- Correct environment setup
- Proper debugging methodology
- Root‑cause analysis (not guesswork)
- Honest documentation of failures

---
