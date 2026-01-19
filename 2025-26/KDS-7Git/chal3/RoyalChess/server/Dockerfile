FROM node:20-alpine AS builder
WORKDIR /app

# Install build tools and pnpm
RUN apk add --no-cache python3 make g++
RUN npm install -g pnpm

# Copy workspace configuration
COPY RoyalChess/pnpm-workspace.yaml ./
COPY RoyalChess/package.json ./
COPY RoyalChess/pnpm-lock.yaml ./

# Copy types package
COPY RoyalChess/types ./types/

# Copy server files
COPY RoyalChess/server/package.json ./server/
COPY RoyalChess/server/tsconfig.json ./server/
COPY RoyalChess/server/ ./server/

# Install dependencies and build
RUN pnpm install --frozen-lockfile
RUN pnpm --filter @royalchess/server run build

FROM node:20-alpine AS runner
WORKDIR /app
RUN npm install -g pnpm

# Copy workspace configuration
COPY RoyalChess/pnpm-workspace.yaml ./
COPY RoyalChess/package.json ./
COPY RoyalChess/pnpm-lock.yaml ./

# Copy server package.json
COPY RoyalChess/server/package.json ./server/

# Copy built dist folder
COPY --from=builder /app/server/dist ./server/dist

# Install only production dependencies
RUN pnpm install --prod --frozen-lockfile

ENV NODE_ENV=production
EXPOSE 3001
CMD ["node","server/dist/server.js"]
