FROM node:13.12.0-alpine

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install
RUN npm install react-router-dom

COPY . . 

EXPOSE 3000

CMD [ "npm", "start" ]
