# --------------------------------
# STAC Frontend - Next.js
# --------------------------------

# ===== Stage 1: Build =====
FROM node:18-alpine AS builder

# 1. Set working directory
WORKDIR /app

# 2. Copy package files first (better caching)
COPY app/frontend/package.json ./

# 3. Install dependencies
RUN npm install

# 4. Copy frontend source code
COPY app/frontend ./

# 5. Build Next.js for production
RUN npm run build


# ===== Stage 2: Production =====
FROM node:18-alpine

# 6. Set working directory
WORKDIR /app

# 7. Set production environment
ENV NODE_ENV=production

# 8. Copy only necessary build artifacts
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json

# 9. Expose Next.js port
EXPOSE 3000

# 10. Start Next.js server
CMD ["npm", "start"]

