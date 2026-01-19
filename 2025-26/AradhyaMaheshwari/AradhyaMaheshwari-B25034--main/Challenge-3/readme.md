# Challenge 3 – Docker Deployments

## Overview

This challenge focuses on deploying **two different web applications** using **Docker and Docker Compose** in a production-like setup.  
Each project uses a different technology stack, and both applications are required to run **simultaneously** on the local machine using isolated Docker containers.

The goal of this challenge is to understand:
- Containerization of frontend and backend services
- Multi-container orchestration using Docker Compose
- Secure networking between containers
- Handling real-world dependency and build issues

---

## Projects Deployed

### 1. RoyalChess(https://github.com/Sachitbansal/royalchess)
**Technology Stack**
- Frontend: Next.js
- Backend: Node.js (Express)
- Database: MongoDB
- Package Manager: pnpm (monorepo)

### 2. STAC Website(https://github.com/Sachitbansal/stac-clone)
**Technology Stack**
- Frontend: Next.js
- Backend: Django (Python)
- Machine Learning Libraries: TensorFlow, PyTorch
- Package Manager: npm (frontend), pip (backend)

## Environment Setup

- Used **WSL 2 (Ubuntu)** as the Linux environment.
- Installed and configured **Docker Desktop** on Windows.
- Enabled **WSL integration** in Docker Desktop settings.

## Commands Used (Linux / WSL)

- `ls` – Lists files and directories in the current directory.
- `tree` – Displays the directory structure in a tree format.
- `pwd` – Shows the current working directory path.
- `cd <directory>` – Navigates to the specified directory.
- `mkdir <name>` – Creates a new directory.
- `cp -r <source> <destination>` – Copies directories recursively from one location to another.
- `rm -rf <name>` – Deletes files or directories forcefully.
- `nano <file>` – Opens a file in the Nano text editor.
- `file <filename>` – Identifies the file type and encoding.
- `iconv -f UTF-16 -t UTF-8 <in> > <out>` – Converts file encoding from UTF-16 to UTF-8.
- `mv <source> <destination>` – Renames or moves files and directories.
- `grep <pattern> <file>` – Searches for specific text inside a file.
- `curl <url>` – Downloads content from a URL via the terminal.
- `node -v` – Displays the installed Node.js version.
- `npm -v` – Displays the installed npm version.
- `npm install <package>` – Installs a Node.js package.
- `npm install -g <package>` – Installs a package globally on the system.
- `docker --version` – Displays the installed Docker version.
- `docker ps` – Lists currently running Docker containers.
- `docker compose up --build` – Builds images and starts all containers defined in docker-compose.
- `docker compose down` – Stops and removes all running containers.
- `docker system prune -af` – Removes unused Docker images, containers, and cache.
- `docker logs <container>` – Displays logs from a specific container.
- `pnpm install` – Installs dependencies using pnpm package manager.
- `pnpm install --frozen-lockfile` – Installs dependencies strictly from the lockfile.
- `pnpm build` – Builds the application using pnpm scripts.

