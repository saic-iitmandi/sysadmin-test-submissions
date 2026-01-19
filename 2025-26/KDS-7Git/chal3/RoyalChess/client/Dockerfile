FROM node:20-alpine AS builder
WORKDIR /app

# Install pnpm
RUN npm install -g pnpm

# Copy workspace configuration
COPY RoyalChess/pnpm-workspace.yaml ./
COPY RoyalChess/package.json ./
COPY RoyalChess/pnpm-lock.yaml ./

# Copy types package
COPY RoyalChess/types ./types/

# Copy client files
COPY RoyalChess/client/package.json ./client/
COPY RoyalChess/client/ ./client/

# Install dependencies and build
RUN pnpm install --frozen-lockfile
RUN pnpm --filter @royalchess/client run build

FROM node:20-alpine AS runner
WORKDIR /app
RUN npm install -g pnpm

# Copy workspace configuration
COPY RoyalChess/pnpm-workspace.yaml ./
COPY RoyalChess/package.json ./
COPY RoyalChess/pnpm-lock.yaml ./

# Copy client package.json
COPY RoyalChess/client/package.json ./client/

# Copy built files from builder
COPY --from=builder /app/client/.next ./client/.next
COPY --from=builder /app/client/public ./client/public
COPY --from=builder /app/client/next.config.js ./client/next.config.js

# Install only production dependencies
RUN pnpm install --prod --frozen-lockfile

ENV NODE_ENV=production
EXPOSE 3000
WORKDIR /app/client
CMD ["pnpm","start"]
