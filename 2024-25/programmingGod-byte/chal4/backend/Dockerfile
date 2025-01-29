
FROM golang:1.15 AS build

WORKDIR /app

COPY go.mod go.sum ./

RUN go mod download

COPY . .

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o backend

FROM alpine:latest

RUN apk add --no-cache ca-certificates

COPY --from=build /app/backend /backend


RUN chmod +x /backend

EXPOSE 8080

CMD ["/backend"]
