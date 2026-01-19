# Stage 1: Build Stage
FROM node:16 AS builder

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy all files (source code, assets, etc.) into the container
COPY . .

# Build the app
RUN npm run build

# Stage 2: Serve Stage
FROM nginx:alpine

# Copy the build files to the Nginx HTML folder
COPY --from=builder /app/build /usr/share/nginx/html

# Expose the port Nginx is listening on
EXPOSE 80

# Run Nginx server
CMD ["nginx", "-g", "daemon off;"]
