


FROM node:20-alpine AS builder


ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable

WORKDIR /app


COPY pnpm-lock.yaml pnpm-workspace.yaml package.json ./


COPY client/package.json ./client/
COPY server/package.json ./server/
COPY types/package.json ./types/


RUN pnpm install --frozen-lockfile

COPY . .

RUN pnpm build:client
RUN pnpm build:server

FROM node:20-alpine AS runner

ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable

WORKDIR /app

COPY --from=builder /app ./

EXPOSE 3000
EXPOSE 3001


CMD ["sh", "-c", "(export PORT=3001 && pnpm start:server) & (export PORT=3000 && pnpm start:client)"]