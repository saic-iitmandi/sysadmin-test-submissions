# frontend/Dockerfile

# Use Node 18
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Install dependencies first (better caching)
COPY package.json package-lock.json* ./
RUN npm install

# Copy all files
COPY . .

# Build the Next.js app for production
RUN npm run build

# Expose port
EXPOSE 3000

# Start the application
CMD ["npm", "start"]