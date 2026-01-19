# Methodology
- Created a working directory:
   - mkdir challenge-3
   - cd challenge-3
- Accessed Windows files from WSL using /mnt/c and copied project folders:
   - cp -r /mnt/c/Users/<username>/Downloads/royalchess-main .
   - cp -r /mnt/c/Users/<username>/Downloads/stac-clone-main .
- Identified that both repositories contained nested folders:
  - royalchess-main
  - stac-clone-main
- Inspected directory structures using ls
- Identified Frontend and backend of each project

## RoyalChess

### RoyalChess Backend
- Navigated to backend directory: cd royalchess/royalchess-main/server
- Created Dockerfile using: nano Dockerfile
- Configured Node.js backend using pnpm workspace setup.

### RoyalChess Frontend
- Navigated to frontend directory: cd ../client
- Created Dockerfile with pnpm-based build and workspace support.

## STAC

### STAC Backend
- Navigated to backend directory: cd stac/stac-clone-main/backend
- Created Dockerfile using Python 3.10 base image.
- Installed dependencies via pip.
- Resolved multiple ML dependency conflicts manually.

### STAC Frontend
- Navigated to frontend directory: cd ../frontend
- Created Dockerfile using Node.js and npm.
- Built Next.js frontend inside container.

## Docker Compose Configuration
- Created a single docker-compose.yml file at project root.
- Defined services for:
   - MongoDB
   - RoyalChess backend
   - RoyalChess frontend
   - STAC backend
   - STAC frontend
- Configured two isolated bridge networks.
- Ensured database container had no exposed ports.

## Dependency Debugging & Fixes (Terminal-Based)
- Fixed Windows UTF-16 encoded files using:
  - file requirements.txt
    
    iconv -f UTF-16 -t UTF-8 requirements.txt > fixed.txt
    
    mv fixed.txt requirements.txt

## Errors
- Tried running (docker compose up --build) several times but kept getting errors continuously in requirements.txt due to several download issues .
- Resolved Python dependency conflicts by editing requirements.txt
   - TensorFlow
   - NumPy
   - PyTorch
   - Protobuf
   - grpcio-status
   - wrapt
   - keras
- Verified dependency changes using:
   - grep tensorflow requirements.txt
   - grep numpy requirements.txt
- Installed missing frontend dependencies: npm install next-themes

## Conclusion 
I wasn't able to run both royal-chess and stac simultaneously


