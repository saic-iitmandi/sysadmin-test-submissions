# Use a compatible Node.js version for React 17
FROM node:16-alpine as build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies with legacy peer dependency handling
RUN npm install --legacy-peer-deps

# Copy the rest of the application code
COPY . .

# Build the production-ready React app
RUN npm run build

# Use Nginx to serve the static files
FROM nginx:1.25-alpine

# Copy the built files to Nginx's default directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose the port
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
