FROM node:20-alpine AS builder
WORKDIR /app
COPY STAC/frontend/package.json STAC/frontend/package-lock.json* ./
COPY STAC/frontend/ ./
RUN npm install
RUN npm run build

FROM node:20-alpine AS runner
WORKDIR /app
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/public ./public
COPY STAC/frontend/package.json ./package.json

ENV NODE_ENV=production
EXPOSE 3000
CMD ["npm","start"]
