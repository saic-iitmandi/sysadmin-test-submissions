FROM node:20

WORKDIR /app

COPY . .

RUN npm install
RUN npm install next-themes   # <-- ADD THIS LINE

EXPOSE 3000

CMD ["npm","run","dev"]
