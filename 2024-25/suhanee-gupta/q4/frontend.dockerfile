FROM node:18 AS builder
WORKDIR /public #might have to change to /src or /app even, judgement severeley limited by the fact that i dont know what im doing
COPY ./frontend/package.json ./frontend/package-lock.json ./
RUN npm install
COPY ./frontend ./
RUN npm run build

FROM nginx:alpine
COPY --from=builder ./public/build /usr/share/nginz/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]