FROM node:12.10.0-alpine

WORKDIR /usr/src/app

ENV PATH /usr/src/app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /usr/src/app/package.json
COPY package-lock.json /usr/src/app/package-lock.json

RUN npm ci
RUN npm install react-scripts@3.1.2 -g --silent

# start app
CMD ["npm", "start"]
