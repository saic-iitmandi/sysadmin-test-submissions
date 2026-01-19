

FROM node:18-alpine
WORKDIR /app
RUN corepack enable && corepack prepare pnpm@latest --activate
# 2. Copy the entire project
COPY . .
# 3. Install dependencies from the root
RUN pnpm install
# 4. EXPLICITLY run only the client
EXPOSE 3000
CMD ["pnpm", "--filter", "client", "dev"]