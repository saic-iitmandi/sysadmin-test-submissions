

# Use Node.js
FROM node:18-alpine
WORKDIR /app
# Copy package files
COPY package*.json ./
# Install dependencies
RUN npm install
# Copy the rest of the code
COPY . .
#default port
EXPOSE 3000
# Run the Next.js development server
CMD ["npm", "run", "dev"]