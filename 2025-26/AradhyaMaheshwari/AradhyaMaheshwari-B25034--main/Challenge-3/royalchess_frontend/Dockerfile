FROM node:18-alpine

WORKDIR /app

RUN npm install -g pnpm@10.28.1

COPY pnpm-workspace.yaml pnpm-lock.yaml ./
COPY client/package.json ./client/
COPY types/package.json ./types/

RUN pnpm install --frozen-lockfile
RUN pnpm --filter ./types... build || true

COPY client ./client/
COPY types ./types/

WORKDIR /app/client

RUN pnpm build

EXPOSE 3000

CMD ["pnpm", "start"]
