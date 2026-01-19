# Challenge 3 – Docker Deployments

## Overview
Deployed two projects using Docker Compose with isolated services.

## Network Design
- Used a custom bridge network.
- Backend services communicate internally.
- Databases are not exposed to the host.

## Security Considerations
- No database ports mapped to host.
- Environment variables for configuration.
- Only required services exposed.

## How to Run
1. `docker-compose up -d`
2. Access services on mapped ports.
