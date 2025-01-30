FROM golang:1.20 AS builder
WORKDIR /app

COPY ./q4/backend/go.mod ./q4/backend/go.sum ./
RUN go mod download

COPY ./q4/backend ./
RUN go build -o main .


FROM debian:bullseye-slim
WORKDIR /app
COPY --from=builder /app/main .
EXPOSE 5000
CMD ["./main"]