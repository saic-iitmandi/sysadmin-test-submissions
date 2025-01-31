# FROM python:3.8-slim
# WORKDIR /app
# COPY /TIP /app
# RUN pip install --no-cache-dir -r requirements.txt      
# EXPOSE 8000
# CMD ["python","app.py"]

# Step 1: Use a Node.js image as the base image
FROM node:18-alpine

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy package.json and package-lock.json to the container
# This is done separately to take advantage of Docker's caching mechanism for npm install
COPY TIP/package.json ./

# Step 4: Install the dependencies from package.json
RUN npm install

# Step 5: Copy the rest of the application code to the container
COPY TIP/ /app

# Step 6: Expose the port the app will run on (adjust this based on your app)
EXPOSE 3000

# Step 7: Define the command to run the app (e.g., "npm start")
CMD ["npm", "start"]
