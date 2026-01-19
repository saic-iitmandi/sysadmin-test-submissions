FROM node:18-alpine
WORKDIR /app
# Install pnpm
RUN npm install -g pnpm
# Copy the ENTIRE monorepo
COPY . .
# Install dependencies
RUN pnpm install
# Move into the client directory
WORKDIR /app/client
EXPOSE 3000
CMD ["npm", "run", "dev"]