FROM node:18-alpine

WORKDIR /app

RUN npm install -g pnpm@10.28.1

COPY pnpm-workspace.yaml pnpm-lock.yaml ./
COPY server/package.json ./server/

RUN pnpm install --frozen-lockfile

COPY server ./server/

WORKDIR /app/server

EXPOSE 5000

CMD ["pnpm", "start"]
