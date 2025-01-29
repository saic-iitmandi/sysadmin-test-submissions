
FROM node:14.1-alpine AS build

WORKDIR /app

COPY package*.json ./

RUN npm install -g yarn --force

COPY . .

RUN yarn install

RUN yarn run build || { echo "Build failed"; exit 1; }


FROM nginx:alpine

COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
