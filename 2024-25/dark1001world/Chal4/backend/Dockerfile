# Stage 1: Build
FROM golang:1.20 AS builder

# Set working directory
WORKDIR /backend

# Copy Go modules manifests
COPY go.mod go.sum ./

# Download dependencies
RUN go mod download

# Copy the source code
COPY . .

# Build the Go application
RUN go build -o backend-app .


# Stage 2: Run
FROM alpine:latest

# Install necessary certificates for Go apps
RUN apk --no-cache add ca-certificates


# Set working directory
WORKDIR /backend

# Copy the built application from the builder stage
COPY --from=builder /backend/backend-app .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["/backend/backend-app"]
