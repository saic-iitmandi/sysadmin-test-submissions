**How to run**
- SETUP n RUNNING OF THE CONTAINER
  - to build the container 
    docker compose build
  - to wake up the container 
    docker compose up -d
- ports:
  1. 3000 RoyalChess
  2. 3001 STAC frontend
  3. 8000 STAC backend
  4. 27017 Mongo
  5. 5432 Postgres



**Objective (MY WORK/POV)**
- Deploy and containerize two separate codebases — STAC and RoyalChess — using Docker. 
- Connect all services via Compose, ensure networking between frontend ↔ backend, and make both applications run locally in a reproducible environment.

The challenge required understanding containerization, build processes, environment configs, migrations, and debugging runtime issues across multiple stacks (Next.js + Django + Mongo + Postgres).

**Environment & Setup**
- Tools i used:
  1. Docker & Docker Compose
  2. Node (Next.js) for frontends
  3. Django + Gunicorn for STAC backend
  4. MongoDB for RoyalChess backend
  5. Postgres for STAC backend
  6. Linux host environment (CLI)

- downloaded all content using git clone in a shared working directory

**Dockerizing the Apps**
- was my first time doing something like this so did some research some youtube, google and came up with that both platforms required separate dockerfiles
1. RoyalChess: separate Dockerfiles for frontend & backend
2. STAC: Next.js frontend + Django backend

- Multiple configurations also has to be aligned
  - Service ports (3000, 3001, 8000)
  - Container networking
  - Environment variables
  - Build commands
  - Runtime commands

- docker-compose.yml linked 6 containers total:

1. royal-frontend
2. royal-backend
3. royal-mongo
4. stac-frontend
5. stac-backend
6. stac-postgres

**Networking Fix**

- Original code assumed localhost-based URLs:
 http://127.0.0.1:8000
 http://localhost:8000

Inside Docker these failed because containers talk by service names, so all endpoints had to be rewritten to:
http://stac-backend:8000


Next.js also required:
NEXT_PUBLIC_API_URL=http://stac-backend:8000


- This was applied across:
  - next.config.js
  - page.tsx
  - Notification fetchers
  - Photo/video gallery fetchers

**Build Issues & Fixes**
-  RoyalChess
RoyalChess built surprisingly clean. After building, visiting browser showed the UI loading successfully.
Referenced screenshot: RoyalChess

- STAC Frontend
STAC frontend had heavy build errors(literally fked my brain):
Static page generation timeouts
Data fetch failures during build
Undefined API URLs
SSR/Next.js behavior mismatches

After correcting API URLs for hours n hours and changing the dockerfile (especially the CMD part), the build finally worked.
Referenced screenshot: STAC Frontend

- STAC Backend
STAC backend ran via Gunicorn but failed on DB access:
no such table: HomePage_projects
Later queries revealed Postgres container was empty and no migrations were applied.

- Attempted fixes:
Enter backend container
Create .env (DEBUG, SECRET_KEY, ALLOWED_HOSTS)
Set DATABASE_URL
Attempt python manage.py migrate
Hit auth failure due to wrong DB credentials
Updated configs to match docker-compose envs
Even after reconciling passwords and reentering container, migrations still didn’t populate tables, likely due to model mismatches or missing manage scripts.
Referenced screenshot: STAC Backend Error

**Final Runtime Check**
- Running:
  docker compose ps
Showed 6 active containers running correctly:
Referenced screenshot: Running Containers

Testing in browser:
- RoyalChess frontend responded
- STAC frontend responded
- STAC backend responded but errored due to DB not migrated

**Where I Landed(CONCLUSION)**
- finally after going through tons of errors finally everything was build and all containers were alive without any error no fetching problem no nothing. 
- Got another problem as royalchess worked fine and responded same goes for stac frontend but for some reason, I wasn't getting any data from stac backend, at one point i thought maybe the saic backend was just a proxy and the data which is intended to come for stac frontend was in royalchess's backend (yeah i was wrong:\ )
- After wasting another hour came up with an bash file named database, thought maybe this is it, imported it, ran it again still nothing. 
- Again tried the migration and surprizingly it worked (tbh i have no idea how it did maybe cause i changed the user ig ?? )
- Then again after doing some changes in backend dockerfile, migrating file ran it again and surprizingly it worked somehow (no idea how it did)
- Agin went to browser still nothing, and finally after giving atleast 10 hours, I thought maybe this is it, maybe i'll come back to it if i got any remaining time.
