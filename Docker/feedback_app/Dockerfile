FROM node:14

WORKDIR /app

COPY package.json .

ENV PORT 80

ARG DEFAULT_PORT=8090

RUN npm install

Copy . .

Expose $PORT



CMD ["node","server.js"]