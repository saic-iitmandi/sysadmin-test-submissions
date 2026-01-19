# Step 1: Use a minimal Golang image
FROM golang:1.20-alpine

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the Go module files and download dependencies
COPY go.mod go.sum ./
RUN go mod download

# Step 4: Copy the rest of the backend code
COPY . .

# Step 5: Build the backend application
RUN go build -o main .

# Step 6: Expose the backend service port
EXPOSE 8080

# Step 7: Start the backend application
CMD ["./main"]
