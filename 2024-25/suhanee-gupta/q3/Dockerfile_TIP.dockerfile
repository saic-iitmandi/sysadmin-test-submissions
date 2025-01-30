#node.js
FROM node:18

WORKDIR /app
#package.json copy
COPY package*.json ./

RUN npm ci
COPY . .
#build
RUN npm run build

# same internal port as nutrient-tracker, will make mapping different
EXPOSE 3000

CMD ["npm", "start"]