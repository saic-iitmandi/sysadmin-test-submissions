# =========================
# Stage 1: Build
# =========================
FROM node:20-alpine AS builder

# Set working directory
WORKDIR /app

# Install pnpm
RUN npm install -g pnpm

# Copy application source (unchanged)
COPY app/ /app/

# Copy startup script
COPY docker/start.sh /app/start.sh

# Install dependencies
RUN pnpm install

# Build backend (TypeScript → JavaScript)
RUN pnpm build:server

# Build frontend (Next.js production build)
RUN pnpm build:client


# =========================
# Stage 2: Runtime
# =========================
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy built app + node_modules + start.sh from builder
COPY --from=builder /app /app

# Expose frontend and backend ports
EXPOSE 3000
EXPOSE 3001

# Start application
CMD ["sh", "/app/start.sh"]
