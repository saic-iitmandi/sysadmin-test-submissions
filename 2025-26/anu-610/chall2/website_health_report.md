# 📊 Website Health Report

## 🌐 Container: `royalchess-app-1`
**Status:** Running (With Errors)
Here's an analysis of the provided logs:

---

**REPORT:**

-   **Issue:** The backend application server (`@royalchess/server`) is consistently failing to start due to an inability to resolve the hostname `db`. The error `Error: getaddrinfo EAI_AGAIN db` indicates a temporary failure in name resolution for the database server. This means the application cannot locate the database service, likely preventing it from establishing a connection pool using `pg-pool`. This occurs repeatedly, leading to the server process exiting with `Exit status 1`. While the client (frontend) appears to start successfully, the lack of a running backend makes the application non-functional.

-   **Severity:** **Critical**
    The core backend service is crashing during startup, rendering the entire application inoperable as it cannot connect to its database.

-   **Recommended Fix:**
    1.  **Verify Database Service Status:** Ensure the database container (expected to be named or aliased as `db` in the Docker network) is running and healthy. Check the `db` container's logs for any startup failures or errors.
    2.  **Docker Network Configuration:** Confirm that both the `royalchess-app-1` container and the `db` database container are configured to be on the same Docker network. Incorrect network configuration would prevent hostname resolution.
    3.  **Service Startup Order & Health Checks:**
        *   **Docker Compose:** If using `docker-compose.yml`, utilize `depends_on` with `condition: service_healthy` or `condition: service_started` for the `royalchess-app-1` service to wait for the `db` service. For example:
            ```yaml
            services:
              db:
                # ... db configuration ...
                healthcheck:
                  test: ["CMD-SHELL", "pg_isready -U user -d dbname"]
                  interval: 5s
                  timeout: 5s
                  retries: 5
              royalchess-app:
                # ... app configuration ...
                depends_on:
                  db:
                    condition: service_healthy # or service_started if healthcheck isn't defined
            ```
        *   **Application-level Retry Logic:** Implement retry logic within the Node.js application's database connection initialization. This allows the server to attempt connecting to the database multiple times with a delay, accounting for the database service taking slightly longer to become fully available than the application.
    4.  **Confirm Hostname:** Double-check that `db` is the correct hostname for the database server as configured in the application's environment variables or configuration files.
    5.  **Docker DNS Diagnostics:** From within the `royalchess-app-1` container (e.g., `docker exec -it <container_id> sh`), try to ping the database host (`ping db`) to diagnose network connectivity and name resolution.
---
## 🌐 Container: `royalchess-db-1`
**Status:** Running (With Errors)
Based on the provided logs for `royalchess-db-1`, here's an analysis:

**Issue:** The PostgreSQL database instance received a "fast shutdown request" at `2026-01-19 12:14:30 UTC`, leading to a controlled shutdown of the database system. Approximately an hour later, at `2026-01-19 13:36:03 UTC`, the database system was successfully restarted and became ready to accept connections.

**No explicit application crashes, high-traffic failures, or backend errors were observed within the database logs themselves during its operational periods.** The shutdown process was initiated externally and handled gracefully by PostgreSQL. The `background worker "logical replication launcher" (PID 32) exited with exit code 1` during shutdown is a normal occurrence when workers are terminated during a fast shutdown.

**Severity:** **Low** (from the perspective of the database application's stability; it handled the shutdown and restart gracefully).
*However, if this shutdown was unexpected or unplanned by the application team or system administrators, the operational impact could be **Medium** (due to downtime) to **Critical** (if it caused significant data unavailability or loss for the website).*

**Recommended Fix:**
1.  **Investigate Shutdown Origin:** Determine the root cause of the "fast shutdown request" that occurred at `2026-01-19 12:14:30 UTC`. This request was sent to the `royalchess-db-1` container, likely originating from:
    *   **Container Orchestration:** A `docker stop` command, Kubernetes pod termination, a redeployment, or a scaling event.
    *   **Host System:** The underlying host machine might have been rebooted or experienced an issue.
    *   **Manual Intervention:** A system administrator or automated script explicitly shut down the container.
2.  **Review Operational Procedures:** Ensure that database shutdowns (if intentional) are part of a well-defined operational procedure and that the application handles database unavailability gracefully. If the shutdown was unintentional, address the underlying issue that triggered the container's termination.
3.  **Monitor Downtime:** Assess the impact of the ~1 hour downtime on the 'royalchess' website. If this downtime was critical, implement strategies to prevent unscheduled shutdowns or to minimize recovery time (e.g., high availability configurations).
---
## 🌐 Container: `stac-clone-frontend-1`
**Status:** Running (With Errors)
Here's an analysis of the provided logs:

---

**REPORT:**

-   **Issue:** The `stac-clone-frontend-1` application is repeatedly failing to connect to its backend API endpoint, which it is attempting to reach at `http://127.0.0.1:8000`. This results in a `ECONNREFUSED` error during data fetching, leading to application instability and continuous restarts of the Next.js frontend. The specific API call failing is for `/api/coreteam/`.

    *   **Details:**
        *   `Error fetching or parsing team data: TypeError: fetch failed`
        *   `cause: Error: connect ECONNREFUSED 127.0.0.1:8000`
        *   The repeated `> STAC IIT Mandi@0.1.0 start` indicates the Next.js application is restarting multiple times, likely because the `fetch failed` error is critical enough to cause the application process to exit.

-   **Severity:** **Critical**

    *   The frontend is unable to establish a connection to its core backend services, specifically for fetching essential data like "team data." This means the application is fundamentally broken and cannot function as intended, or even start properly, leading to a non-operational website.

-   **Recommended Fix:**

    1.  **Correct Backend API Endpoint Configuration:**
        *   **Primary Suspect:** The frontend is trying to connect to `127.0.0.1:8000`. In a Dockerized environment, `127.0.0.1` inside a container refers *only* to that container itself. It will *not* reach another container or the Docker host.
        *   **Action:** Modify the frontend's configuration (e.g., environment variables, a `next.config.js` file, or a dedicated configuration file) to point to the correct network address of the backend service. This typically involves using the Docker service name of the backend container. For example, if your backend service is named `stac-clone-backend` in your `docker-compose.yml`, the frontend configuration should be updated to `http://stac-clone-backend:8000` (assuming port 8000 is exposed by the backend).
        *   **Verify:** Ensure both frontend and backend containers are on the same Docker network.

    2.  **Ensure Backend Service is Running and Healthy:**
        *   Confirm that the backend service (which should be listening on port 8000) is running, healthy, and accessible from other containers within the Docker network. Check its logs for any startup errors or crashes.

    3.  **Address Next.js Warnings (Lower Priority but Good Practice):**
        *   **Cache Configuration:** The warning `⚠ fetch for http://127.0.0.1:8000/api/coreteam/ on /team specified "cache: no-store" and "revalidate: 0", only one should be specified.` indicates a redundant or conflicting cache strategy. Choose either `cache: 'no-store'` or `revalidate: 0` (or a positive number for revalidation), but not both, for the data fetching call for `/api/coreteam/`. This is a best practice for Next.js and while not critical for the current issue, it's good to resolve.
        *   **Image Optimization (Sharp):** The warning `Warning: For production Image Optimization with Next.js, the optional 'sharp' package is strongly recommended.` suggests installing the `sharp` package (`npm i sharp`) in your frontend's Docker image to improve image optimization performance in production. This is not causing the current crashes but is a production readiness recommendation.
---
